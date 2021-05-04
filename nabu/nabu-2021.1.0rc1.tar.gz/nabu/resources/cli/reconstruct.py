#!/usr/bin/env python

from ... import version
from ...io.config import NabuConfigParser, validate_nabu_config
from .utils import parse_params_values
from ..utils import is_hdf5_extension
from .cli_configs import ReconstructConfig


def update_reconstruction_start_end(conf_dict, user_indices):
    if len(user_indices) == 0:
        return
    rec_cfg = conf_dict["reconstruction"]
    err = None
    if user_indices in ["first", "middle", "last"]:
        start_z = user_indices
        end_z = user_indices
    elif user_indices == "all":
        start_z = 0
        end_z = -1
    elif "-" in user_indices:
        try:
            start_z, end_z = user_indices.split("-")
            start_z = int(start_z)
            end_z = int(end_z)
        except Exception as exc:
            err = "Could not interpret slice indices '%s': %s" % (user_indices, str(exc))
    else:
        err = "Could not interpret slice indices: %s" % user_indices
    if err is not None:
        print(err)
        exit(1)
    rec_cfg["start_z"] = start_z
    rec_cfg["end_z"] = end_z


def get_log_file(arg_logfile, legacy_arg_logfile, forbidden=None):
    default_arg_val = ""
    # Compat. log_file --> logfile
    if legacy_arg_logfile != default_arg_val:
        logfile = legacy_arg_logfile
    else:
        logfile = arg_logfile
    #
    if forbidden is None:
        forbidden = []
    for forbidden_val in forbidden:
        if logfile == forbidden_val:
            print("Error: --logfile argument cannot have the value %s" % forbidden_val)
            exit(1)
    if logfile == "":
        logfile = True
    return logfile


def main():
    args = parse_params_values(
        ReconstructConfig,
        parser_description="Perform a tomographic reconstruction.",
        program_version="nabu " + version
    )

    # Imports are done here, otherwise "nabu --version" takes forever
    from ...resources.processconfig import ProcessConfig
    from ...cuda.utils import __has_pycuda__
    if __has_pycuda__:
        from ...app.local_reconstruction import FullFieldReconstructor, FullRadiosReconstructor
    else:
        print("Error: need cuda and pycuda for reconstruction")
        exit(1)
    from ..logger import Logger
    #

    # A crash with scikit-cuda happens only on PPC64 platform if and nvidia-persistenced is running.
    # On such machines, a warm-up has to be done.
    import platform
    if platform.machine() == "ppc64le":
        from silx.math.fft.cufft import CUFFT
    #

    logfile = get_log_file(
        args["logfile"], args["log_file"], forbidden=[args["input_file"]]
    )
    conf_dict = NabuConfigParser(args["input_file"]).conf_dict
    update_reconstruction_start_end(conf_dict, args["slice"].strip())

    proc = ProcessConfig(conf_dict=conf_dict, create_logger=logfile)
    logger = proc.logger

    logger.info(
        "Going to reconstruct slices (%d, %d)"
        % (proc.nabu_config["reconstruction"]["start_z"], proc.nabu_config["reconstruction"]["end_z"])
    )

    # (hopefully) temporary patch
    if "phase" in proc.processing_steps:
        if args["energy"] > 0:
            logger.warning("Using user-provided energy %.2f keV" % args["energy"])
            proc.dataset_infos.dataset_scanner._energy = args["energy"]
            proc.processing_options["phase"]["energy_kev"] = args["energy"]
        if proc.dataset_infos.energy  < 1e-3 and proc.nabu_config["phase"]["method"] != None:
            msg = "No information on energy. Cannot retrieve phase. Please use the --energy option"
            logger.fatal(msg)
            raise ValueError(msg)
    #

    # Determine which reconstructor to use
    reconstructor_cls = FullFieldReconstructor
    phase_method = None
    if "phase" in proc.processing_steps:
        phase_method = proc.processing_options["phase"]["method"]
    rotate_projections = ("rotate_projections" in proc.processing_steps)
    if phase_method == "CTF" or rotate_projections:
        reconstructor_cls = FullRadiosReconstructor

    # Get extra options
    extra_options = {
        "gpu_mem_fraction": args["gpu_mem_fraction"],
        "cpu_mem_fraction": args["cpu_mem_fraction"],
    }
    if reconstructor_cls is FullFieldReconstructor:
        extra_options.update({
            "use_phase_margin": args["use_phase_margin"],
            "max_chunk_size": args["max_chunk_size"] if args["max_chunk_size"] > 0 else None,
            "phase_margin": args["phase_margin"],
        })
    else:
        extra_options.update({
            "max_group_size": args["max_chunk_size"] if args["max_chunk_size"] > 0 else None,
        })


    R = reconstructor_cls(
        proc,
        logger=logger,
        extra_options=extra_options
    )

    R.reconstruct()
    R.merge_data_dumps()
    if is_hdf5_extension(proc.nabu_config["output"]["file_format"]):
        R.merge_hdf5_reconstructions()
    R.merge_histograms()



if __name__ == "__main__":
    main()
