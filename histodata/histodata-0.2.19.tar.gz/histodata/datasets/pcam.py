from typing import Callable
from typing import Optional as O
from typing import Sequence
from typing import Union as U

import os
from h5py import File
import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose

from ..base.histo_dataset import HistoDataset
from ..base import data_readers, df_creators, df_manipulators
# TODO change to HistoDataset API


def pcam_patches(
    root: str,  # '/data/ldap/histopathologic/original_read_only/PCAM_extracted'
    transformation: O[U[Callable, Sequence[Callable]]] = None,
    #   pre_transformation: O[U[Callable, Sequence[Callable]]] = None, # pretrans not possible yet
    subset: O[str] = "train",
) -> Dataset:
    """
    Creates the PCAM dataset and returns it as type HistoDataset, which inherits from torch.utils.data.Dataset.

    Data and further information can be found at https://humanunsupervised.github.io/humanunsupervised.com/pcam/pcam-cancer-detection.html

    Arguments:
        root: Absolute path to the dataset files.
        transformation: A callable or a list of callable transformations.
        subset: Which part of the dataset should be used.
                One of {"train", "validation", "test"}

    Returns:
        torch.utils.data.Dataset:
            The dataset that loads the pcam patches. You can use this
            as normal pytorch dataset. If you call it, the data will
            be returned as dictionary with structure:
            dict['images': torch.Tensor, 'labels': torch.Tensor].
    """
    if subset:
        subset = subset.lower()
    if subset.startswith("tr"):
        imgs_hdf5_filepath = root + "/camelyonpatch_level_2_split_train_x.h5"
        labels_hdf5_filepath = root + "/camelyonpatch_level_2_split_train_y.h5"
        return PCAM(
            imgs_hdf5_filepath=imgs_hdf5_filepath,
            labels_hdf5_filepath=labels_hdf5_filepath,
            transform=transformation,
        )
    elif subset.startswith("val"):
        imgs_hdf5_filepath = root + "/camelyonpatch_level_2_split_valid_x.h5"
        labels_hdf5_filepath = root + "/camelyonpatch_level_2_split_valid_y.h5"
        return PCAM(
            imgs_hdf5_filepath=imgs_hdf5_filepath,
            labels_hdf5_filepath=labels_hdf5_filepath,
            transform=transformation,
        )
    elif subset.startswith("te"):
        imgs_hdf5_filepath = root + "/camelyonpatch_level_2_split_test_x.h5"
        labels_hdf5_filepath = root + "/camelyonpatch_level_2_split_test_y.h5"
        return PCAM(
            imgs_hdf5_filepath=imgs_hdf5_filepath,
            labels_hdf5_filepath=labels_hdf5_filepath,
            transform=transformation,
        )
    # TODO use case not possible yet
    # elif subset == 'all':
    #     pass
    else:
        raise NotImplementedError(
            'The parameter "subset" needs to be one of ["train", "validation", "test"].'
        )


class PCAM(Dataset):
    """
    Creates the PCAM dataset and returns it as type HistoDataset, which inherits from torch.utils.data.Dataset.

    Data and further information can be found at https://humanunsupervised.github.io/humanunsupervised.com/pcam/pcam-cancer-detection.html
    """

    def __init__(
        self,
        imgs_hdf5_filepath: str,
        labels_hdf5_filepath: str,
        imgs_key: str = "x",
        labels_key: str = "y",
        transform: O[Compose] = None,
    ):
        """
        Initializes dataset.
        """

        self.imgs_hdf5_filepath = imgs_hdf5_filepath
        self.labels_hdf5_filepath = labels_hdf5_filepath
        self.imgs_key = imgs_key
        self.labels_key = labels_key

        self.transform = transform
        self.loaded_images = None
        self.loaded_labels = None
        
    def __len__(self):
        """
        Returns length of dataset
        """
        with File(self.labels_hdf5_filepath, "r") as db:
            lens = len(db[self.labels_key])

        return lens

    def preload(self):
        with File(self.imgs_hdf5_filepath, "r") as db:
            self.loaded_images = db[self.imgs_key][::]
        with File(self.labels_hdf5_filepath, "r") as db:
            self.loaded_labels = db[self.labels_key][::]
        

    def get_feature_for_all_rows(self):
        labels = []
        with File(self.labels_hdf5_filepath, "r") as db:
            for idx in range(len(self)):
                label = db[self.labels_key][idx][0][0][0]  # TODO make it nice
                labels.append(label)
        return {"feature": labels}

    def __getitem__(self, idx: int) -> dict:
        """
        TODO
        """

        if self.loaded_images is None:
            # get images
            with File(self.imgs_hdf5_filepath, "r") as db:
                image = db[self.imgs_key][idx]
            # get labels
            with File(self.labels_hdf5_filepath, "r") as db:
                label = db[self.labels_key][idx][0][0][0]  # TODO make it nice
        else:
            image = self.loaded_images[idx]
            label = self.loaded_labels[idx][0][0][0]

        # transform data
        if self.transform:
            image = self.transform(image)

        return {"data": image, "feature": torch.as_tensor(label).type(torch.LongTensor)}

    
def pcam_patches_preprocessed(
    root: str,  # '/data/ldap/histopathologic/original_read_only/PCAM_extracted_images'
    transformation: O[U[Callable, Sequence[Callable]]] = None,
    pre_transformation: O[U[Callable, Sequence[Callable]]] = None,
    subset: O[str] = "train",
    seed: O[int] = None,
) -> HistoDataset:
    """
    Creates the midog dataset and returns it as type HistoDataset, which inherits from torch.utils.data.Dataset.

    Data and further information can be found at TODO

    Arguments:
        root: absolute path to the dataset files.
                transformation (Callable): A callable or a list of
                       callable transformations.
        pre_transformation (Callable): A callable or a list of
                       callable transformations. "pre_transformation"
                       is called before "transformation". The transformation
                       is called with a seed and will give always the same
                       result.
        subset: Which part of the dataset should be used.
                One of {"train", "valid", "test"}
        seed:   The seed that is used for the "pre_transformation" and the
                "transformation". If the seed is set, the "pre_transformation"
                will always use the same seed for a data row. If the seed is
                set, the "transformation" will use always the same seed
                depending on the call position.

    Returns:
        HistoDataset:
            The dataset that loads the bach patches. You can use this
            as normal pytorch dataset. If you call it, the data will
            be returned as dictionary.
    """
    if subset:
        subset = subset.lower()
    if subset.startswith("tr"):
        path_to_dataset = os.path.join(root, "train")
    elif subset.startswith("val"):
        path_to_dataset = os.path.join(root, "valid")
    elif subset.startswith("test"):
        path_to_dataset = os.path.join(root, "test")
    else:
        raise NotImplementedError(
            'The parameter "subset" needs to be one of ["train", "valid", "test"].'
        )

    path_to_csv = os.path.join(path_to_dataset, "features.csv")
    # create HistoDataset object and pass relevant attributes
    ds = HistoDataset(
        df_creators.CreateDFFromCSV(path_to_csv),
        path_to_dataset,
        data_readers="data/{id}.tiff",
        feature_readers=data_readers.ReadValueFromCSV(r"{feature}", encoded_values=["0", "1"]),
        seed=seed,
        pre_transfs=pre_transformation,
        da_transfs=transformation,
    )
    return ds