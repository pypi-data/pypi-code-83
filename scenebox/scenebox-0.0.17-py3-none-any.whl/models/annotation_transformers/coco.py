#  Copyright (c) 2020 Caliber Data Labs.
#  All rights reserved.
#

import os
from datetime import datetime
from typing import List, Optional, Union

from shared.external.clients.asset_manager_client import AssetManagerClient
from shared.external.constants import (AnnotationMediaTypes,
                                       AnnotationProviders, AnnotationTypes)
from shared.external.custom_exceptions import InvalidAnnotationError
from shared.external.models.annotation import Annotation, AnnotationEntity
from shared.external.tools import misc, time_utils


class CocoAnnotation(Annotation):
    def __init__(
        self,
        asset_manager_client: Optional[AssetManagerClient],
        image_dict: dict,
        annotations_dict: List[dict],
        categories_dict: List[dict],
        annotation_type: AnnotationTypes,
        set_name: Optional[str] = None,
        provider: Optional[Union[AnnotationProviders, str]] = None,
        version: Optional[str] = None,
        ground_truth: Optional[str] = 'true'
    ):

        self.image_dict: dict = image_dict
        self.annotations_dict: List[dict] = annotations_dict
        self.categories_dict: List[dict] = categories_dict
        # cannot set self.annotation_type here because super().__init__ sets it
        # to None and then calls self.set_annotation_type()
        self._annotation_type: AnnotationTypes = annotation_type
        self.set_name: Optional[str] = set_name
        self._provider: Optional[Union[AnnotationProviders, str]] = provider
        self._version: str = version
        self._ground_truth = ground_truth

        metadata = {"image": image_dict, "categories": categories_dict}
        super().__init__(
            asset_manager_client=asset_manager_client, annotation_meta=metadata
        )

    def set_id(self):
        self.id = misc.get_guid()

    def set_ground_truth(self):
        self.ground_truth = self._ground_truth

    def set_version(self):
        self.version = self._version

    def set_timestamp(
            self,
            asset_manager_client: Optional[AssetManagerClient] = None):
        if "date_captured" in self.image_dict:
            self.timestamp = time_utils.string_to_datetime(
                self.image_dict["date_captured"]
            )
        else:
            super().set_timestamp(asset_manager_client=asset_manager_client)

    def set_asset_id(self):
        self.asset_id = self.image_dict.get("file_name")

    def set_media_type(self):
        self.media_type = AnnotationMediaTypes.IMAGE

    def set_provider(self):
        self.provider = self._provider

    def set_annotation_type(self):
        if self._annotation_type not in [
            AnnotationTypes.SEMANTIC_SEGMENTATION,
            AnnotationTypes.TWO_D_BOUNDING_BOX,
        ]:
            raise InvalidAnnotationError(
                f"invalid annotation type {self._annotation_type}"
            )
        self.annotation_type = self._annotation_type

    def set_annotation_entities(self):
        if self._annotation_type == AnnotationTypes.TWO_D_BOUNDING_BOX:
            self.__set_bounding_box_annotation_entities()
        elif self._annotation_type == AnnotationTypes.SEMANTIC_SEGMENTATION:
            self.__set_semantic_segmentation_annotation_entities()
        else:
            raise InvalidAnnotationError(
                f"invalid annotation type {self._annotation_type}"
            )

    def set_set_membership(self):
        if self.set_name:
            self.sets = [self.set_name]
        else:
            self.sets = []

    def __set_bounding_box_annotation_entities(self):

        self.annotation_entities = []

        if not isinstance(self.annotations_dict, list):
            raise InvalidAnnotationError(
                "bounding box annotation is expected to be list"
            )

        for annotation in self.annotations_dict:
            try:
                category_id = annotation["category_id"]
                left = float(annotation["bbox"][0])
                top = float(annotation["bbox"][1])
                width = float(annotation["bbox"][2])
                height = float(annotation["bbox"][3])
            except KeyError as e:
                raise InvalidAnnotationError(str(e))

            coordinates = [
                {"x": left, "y": top},
                {"x": left + width, "y": top},
                {"x": left + width, "y": top + height},
                {"x": left, "y": top + height},
            ]
            label = next(
                filter(lambda x: x["id"] == category_id, self.categories_dict)
            )["name"]
            self.annotation_entities.append(
                AnnotationEntity(
                    {
                        "label": label,
                        "category_id": category_id,
                        "annotation_type": AnnotationTypes.TWO_D_BOUNDING_BOX,
                        "coordinates": coordinates,
                    },
                    annotation_uid=self.id,
                )
            )

    def __set_semantic_segmentation_annotation_entities(self):
        if not isinstance(self.annotations_dict, list):
            raise InvalidAnnotationError(
                "bounding box annotations are expected to be a list"
            )

        self.annotation_entities = []

        for annotation in self.annotations_dict:
            category_id = int(annotation["category_id"])
            label = next(
                filter(
                    lambda x: int(
                        x["id"]) == category_id,
                    self.categories_dict))["name"]
            self.annotation_entities.append(
                AnnotationEntity(
                    {
                        "label": label,
                        "category_id": category_id,
                        "annotation_type": AnnotationTypes.SEMANTIC_SEGMENTATION,
                        "resource": annotation["segmentation"],
                    },
                    annotation_uid=self.id,
                ))
