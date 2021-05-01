from io import FileIO
import os
import numpy as np
import numpy.testing as npt
# import pytest
import logging
import quilt3
from aicsimageio import AICSImage

from src.contact_sites_result import ContactSitesResult
from src.contact_sites_provider import ContactSitesProvider


log = logging.getLogger(__name__)

images_save_dir = "{}\\images".format(os.getcwd())
results_save_dir = "{}\\results".format(os.getcwd())
if not os.path.exists(results_save_dir):
    os.makedirs(results_save_dir)
# predictions
images = {
    "internal_segmentations":[
        #{"file_name":"0_Cells_seg.tiff", "legend":"Cell_region"},
        # {"file_name":"0_Membrane_seg.tiff", "legend":"Membrane"},
        {"file_name":"0_Nuc_seg.tiff", "legend":"Nuc"},
        {"file_name":"0_ER_seg.tiff", "legend":"ER"},
        {"file_name":"0_Golgi_seg.tiff", "legend":"Golgi"},
        {"file_name":"0_Mito_seg.tiff", "legend":"Mito"}
    ]
}
# golgi GT
# images = {
#     "membrane_segmentations":[
#         {"file_name":"c6a1fabe_3500001250_100X_20170829_1-Scene-02-P2-E04.czi_cellWholeIndexImageScale.tiff", "legend":"Membrane"}
#     ],
#     "structure_segmentations":[
#         {"file_name":"4d24c4c8_3500001250_100X_20170829_1-Scene-02-P2-E04_struct_segmentation.tiff", "legend":"Golgi"}
#     ],
#     "dna_segmentations":[
#         {"file_name":"e1b5b589_3500001250_100X_20170829_1-Scene-02-P2-E04.czi_nucWholeIndexImageScale.tiff", "legend":"DNA"}
#     ]
# }
# ER GT
# images = {
#     "membrane_segmentations": [
#         {"file_name": "1e4f61b8_3500001130_100X_20170728_1-Scene-37-P37-F05.czi_cellWholeIndexImageScale.tiff", "legend": "Membrane"}
#     ],
#     "structure_segmentations": [
#         {"file_name": "f20fdc94_3500001130_100X_20170728_1-Scene-37-P37-F05_struct_segmentation.tiff", "legend": "ER"}
#     ],
#     "dna_segmentations": [
#         {"file_name": "8f5246c4_3500001130_100X_20170728_1-Scene-37-P37-F05.czi_nucWholeIndexImageScale.tiff", "legend": "DNA"}
#     ]
# }

images_repo = quilt3.Package.browse(
    "aics/pipeline_integrated_cell", registry="s3://allencell")

num_images = 0
for repo_internal_path in images.keys():
    images_objs = images.get(repo_internal_path)
    num_images += len(images_objs)


def fetch_images() -> None:

    #  if images doesnot exist, then create it
    if not os.path.exists(images_save_dir):
        os.makedirs(images_save_dir)

    for repo_internal_path in images.keys():
        images_objs = images.get(repo_internal_path)
        for image_obj in images_objs:
            image_file_name = image_obj.get("file_name")

            # construct intire repo path
            image_repo_path = "{}\\{}".format(
                repo_internal_path, image_file_name)

            # construct image target path
            image_target_path = "{}\\{}".format(
                images_save_dir, image_file_name)

            # if image exists continue, otherwise fetch it
            if os.path.exists(image_target_path):
                continue
            try:
                images_repo[image_repo_path].fetch(image_target_path)
            except OSError:
                pass


def test_provider() -> None:
    fetch_images()

    contact_sites_images = []
    
    for repo_internal_path in images.keys():
        images_objs = images.get(repo_internal_path)
        for image_obj in images_objs:
            image_file_name = "{}\\{}".format(
                images_save_dir, image_obj.get("file_name"))
            with AICSImage(image_file_name) as img:
                z_slice = round(img.size_c / 2)
                contact_sites_images.append({"data": img, "legend_name": image_obj.get("legend")})

    provider = ContactSitesProvider()
    # pridiction pipe
    result = provider.run_pipe(contact_sites_images,"Nuc_ER_Golgi_Mito_predictions", image_to_ndarray=lambda image:_image_to_ndarray(image,"CYX"), unifier=False)

    # GT pipe
    # result = provider.run_pipe(contact_sites_images, "result_Mem_ER_DNA_GT",image_to_ndarray=lambda image: _image_to_ndarray(image, "ZYX"), unifier=False)

    print(result.get_metadata())
    image_target_path_png = "{}\\result_Nuc_ER_Golgi_Mito_predictions.png".format(
        results_save_dir)
    result.save_figure(image_target_path_png, image_to_legend_ratio=1)
    image_target_path_tiff = "{}\\result_Nuc_ER_Golgi_Mito_predictions.tiff".format(
        results_save_dir)
    result.save_tiff(image_target_path_tiff)
    image_gs_target_path_tiff = "{}/result_gs.tiff".format(images_save_dir)
    # result.save_greyscale_tiff(image_gs_target_path_tiff)
    # organelle_distribuation_path_fig = "{}\\Nuc_ER_Golgi_Mito_predictions_z_slices_organelle_distribuation.png".format(
    #     results_save_dir)
    # result.save_distribuation_figure(0, organelle_distribuation_path_fig, "Z slices")
    # organelle_distribuation_path_fig = "{}\\Nuc_ER_Golgi_Mito_predictions_x_slices_organelle_distribuation.png".format(
    #     results_save_dir)
    # result.save_distribuation_figure(1, organelle_distribuation_path_fig, "X slices")
    # organelle_distribuation_path_fig = "{}\\Nuc_ER_Golgi_Mito_predictions_y_slices_organelle_distribuation.png".format(
    #     results_save_dir)
    # result.save_distribuation_figure(2, organelle_distribuation_path_fig, "Y slices")


def _image_to_ndarray(image, pattern="CYX"):
    return image.get_image_data(pattern)


test_provider()
