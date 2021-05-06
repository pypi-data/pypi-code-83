import tbridge
import tbridge.plotting as plotter
import time
import multiprocessing as mp
from pebble import ProcessPool

from numpy import transpose, round, array, ndarray
from numpy.random import choice
import sys
from concurrent.futures import TimeoutError


def pipeline(config_values, max_bins=None, separate_mags=None, provided_bgs=None, provided_psfs=None,
             progress_bar=False, multiprocess_level='obj'):
    """
    Runs the entire simulation pipeline assuming certain data exists.
    :param config_values: Values from properly loaded configuration file.
    :param max_bins: The number of bins to process (useful if running tests).
    :param separate_mags: Optional array of magnitudes.
    :param provided_bgs: A set of provided background cutouts [OPTIONAL].
    :param provided_psfs: A set of provided PSFs related to the provided backgrounds [OPTIONAL].
    :param progress_bar: Have a TQDM progress bar.
    :param multiprocess_level: Where in the simulations to divide into cores
        'obj'  - Divide at the object level, where each core handles a single object in each bin.
        'bin'  - Divide at the bin level, so each core is responsible for a single bin
        'none' - Do not do any multiprocessing at all (SLOW).

        The object level is less memory intensive, but bins are processed one by one instead of simultaneously.

    EXAMPLE USAGE:

    config_values = tbridge.load_config_file("path/to/config/file.tbridge")
    tbridge.pipeline(config_values, max_bins=10)

    """

    binned_objects = tbridge.bin_catalog(config_values)
    max_bins = len(binned_objects) if max_bins is None else max_bins

    verbose = config_values["VERBOSE"]
    if verbose:
        print(max_bins, "bins to process.")

    if config_values["SAME_BGS"] and provided_bgs is None:
        provided_bgs, provided_psfs = tbridge.get_backgrounds(config_values, n=50)

    if multiprocess_level == 'bin':
        pool = mp.Pool(processes=config_values["CORES"])
        results = [pool.apply_async(_process_bin, (b, config_values, separate_mags, provided_bgs,
                                                   progress_bar, False))
                   for b in binned_objects[:max_bins]]
        [res.get() for res in results]
    elif multiprocess_level == 'obj':
        for b in binned_objects[:max_bins]:
            _process_bin(b, config_values, separate_mags=separate_mags,
                         provided_bgs=provided_bgs, progress_bar=progress_bar, multiprocess=True)

    tbridge.config_to_file(config_values, filename=config_values["OUT_DIR"] + "tbridge_config.txt")


def _process_bin(b, config_values, separate_mags=None, provided_bgs=None,
                        progress_bar=False, multiprocess=False, profiles_per_row=3):
    """
        Process a single bin of galaxies. (Tuned for pipeline usage but can be used on an individual basis.
        :param b: Bin to obtain full profiles from.
        :param config_values: Values from properly loaded configuration file.
        :param separate_mags: Optional array of magnitudes.
        :param provided_bgs: Array of provided backgrounds
        :param progress_bar: Use a TQDM progress bar (note with multithreading this might get funky).
        :param multiprocess: Run in multiprocessing mode.
            This means both the model creation AND the
        :return:
        """
    t_start = time.time()
    verbose = config_values["VERBOSE"]

    # Load in bin information, and prepare all necessary structural parameters.
    keys, columns = b.return_columns()
    mags, r50s, ns, ellips = tbridge.pdf_resample(tbridge.structural_parameters(keys, columns), resample_size=1000)
    if separate_mags is not None:
        mags = tbridge.pdf_resample(separate_mags, resample_size=len(r50s))[0]

    # Simulate the model rows, using multiprocessing to speed things up######################
    if verbose:
        print("Processing", config_values["N_MODELS"], "models for: ", b.bin_params)

    # Prepare containers for simulations
    job_list = []
    full_profile_list, mask_infolist = [[] for i in range(profiles_per_row)], []
    masked_cutouts, unmasked_cutouts = [], []

    models = tbridge.simulate_sersic_models(mags, r50s, ns, ellips,
                                            config_values, n_models=config_values["N_MODELS"])

    # Run multithreaded simulation code
    with ProcessPool(max_workers=config_values["CORES"]) as pool:
        for i in range(len(models)):
            job_list.append(pool.schedule(_process_model,
                                          args=(models[i], config_values, provided_bgs),
                                          timeout=config_values["ALARM_TIME"]))
    # Collect the results
    for i in range(len(job_list)):
        try:
            result = job_list[i].result()
            profiles = result["PROFILES"]
            if len(profiles) != profiles_per_row:
                continue
            for i in range(len(full_profile_list)):
                full_profile_list[i].append(profiles[i])
            mask_infolist.append(result["MASK_DATA"])
            masked_cutouts.append(result["MASKED_CUTOUT"])
            unmasked_cutouts.append(result["UNMASKED_CUTOUT"])

        except Exception as error:
            print(error.args, i)

    bg_info = [[], [], []]
    for i in range(0, len(mask_infolist)):
        bg_info[0].append(mask_infolist[i]["BG_MEAN"])
        bg_info[1].append(mask_infolist[i]["BG_MEDIAN"])
        bg_info[2].append(mask_infolist[i]["BG_STD"])

    # Subtract the median values from the bgadded profiles
    bg_sub_profiles = tbridge.subtract_backgrounds(full_profile_list[2], bg_info[1])
    full_profile_list.append(bg_sub_profiles)

    # Save the profiles to the required places
    tbridge.save_profiles(full_profile_list,
                          bin_info=b.bin_params,
                          out_dir=config_values["OUT_DIR"],
                          keys=["bare", "noisy", "bgadded", "bgsub"],
                          bg_info=bg_info)

    # Save images if demanded by the user
    image_output_filename = config_values["OUT_DIR"] + tbridge.generate_file_prefix(b.bin_params)
    image_indices = choice(len(unmasked_cutouts),
                     size=int(len(unmasked_cutouts) * config_values["CUTOUT_FRACTION"]),
                     replace=False)
    # This is just to avoid an issue if the indices list is too small
    if len(image_indices) == 1:
        image_indices.append(0)

    masked_cutouts, unmasked_cutouts = array(masked_cutouts)[image_indices], array(unmasked_cutouts)[image_indices]

    if config_values["SAVE_CUTOUTS"].lower() == 'stitch':
        tbridge.cutout_stitch(unmasked_cutouts, masked_cutouts=masked_cutouts,
                              output_filename=image_output_filename + "stitch.fits")
    if config_values["SAVE_CUTOUTS"].lower() == 'mosaic':
        plotter.view_cutouts(masked_cutouts, output=image_output_filename + ".png", log_scale=False)
    if config_values["SAVE_CUTOUTS"].lower() == 'fits':
        output_filename = config_values["OUT_DIR"] + tbridge.generate_file_prefix(b.bin_params) + ".png"
        tbridge.save_cutouts(masked_cutouts, output_filename=output_filename)

    if verbose:
        print("Finished", b.bin_params, "-- Time Taken:", round((time.time() - t_start) / 60, 2), "minutes.")
        print()


def _process_model(sersic_model, config, provided_bgs=None):
    """
    Run processing for a single model.

    :param sersic_model: The input model to process
    :param config: Configuration values loaded from config file
    :param provided_bgs: OPTIONAL --- set of provided backgrounds
    """
    # First make the input models
    if provided_bgs is None:
        bg_added_model, convolved_model = tbridge.add_to_background(sersic_model, config)
    else:
        convolved_model = tbridge.convolve_models(sersic_model)
        bg_added_model = tbridge.add_to_provided_backgrounds(convolved_model, provided_bgs)

    noisy_model = tbridge.add_to_noise(convolved_model)
    masked_model, mask_data = tbridge.mask_cutout(bg_added_model, config=config)

    model_row = [convolved_model, noisy_model, masked_model]

    # Then extract everything we can
    profile_extractions = []
    for i in range(0, len(model_row)):
        try:
            extraction = tbridge.isophote_fitting(model_row[i], config=config)
            profile_extractions.append(extraction.to_table())
        except Exception as error:
            print(error.args)
            continue

    # put the results into a dictionary format and return that
    return {"PROFILES": profile_extractions,
            "MASK_DATA": mask_data,
            "UNMASKED_CUTOUT": bg_added_model,
            "MASKED_CUTOUT": masked_model}
