#  Copyright (c) 2020 Caliber Data Labs.
#  All rights reserved.
#

import re
from typing import Optional

from shared.external.clients.asset_manager_client import AssetManagerClient
from shared.external.constants import (AnnotationMediaTypes,
                                       AnnotationProviders, AnnotationTypes)
from shared.external.custom_exceptions import InvalidAnnotationError
from shared.external.models.annotation import Annotation, AnnotationEntity
from shared.external.tools import time_utils


class ScaleAnnotation(Annotation):
    def __init__(
            self,
            asset_manager_client: Optional[AssetManagerClient],
            scale_response: dict,
            version: Optional[str] = None):

        self.scaleapi_annotations = scale_response.get(
            'response', {}).get('annotations', {})

        self.scaleapi_task = scale_response.get('task', {})

        self.scaleapi_type = self.scaleapi_task.get('type')
        self.scaleapi_params = self.scaleapi_task.get('params', {})
        self.metadata = self.scaleapi_task.get('metadata', {})

        self.scale_response = scale_response
        self.scaleapi_annotations = scale_response.get(
            'response', {}).get('annotations', {})
        self._version = version

        if self.scaleapi_task.get('status') != 'completed':
            raise InvalidAnnotationError(
                'status {} is not completed'.format(
                    self.scaleapi_task.get('status')))

        super().__init__(
            asset_manager_client=asset_manager_client,
            annotation_meta=scale_response)

    def set_id(self):
        self.id = self.scale_response.get('task_id') + ".ann"

    def set_ground_truth(self):
        self.ground_truth = 'true'

    def set_version(self):
        self.version = self._version

    def set_timestamp(self, asset_manager_client: Optional[AssetManagerClient] = None):
        self.timestamp = time_utils.string_to_datetime(
            self.scaleapi_task.get('created_at'))

    def set_asset_id(self):
        print(self.metadata)
        self.asset_id = self.metadata.get("asset_id")

    def set_media_type(self):
        if self.scaleapi_type == 'lidarannotation':
            self.media_type = AnnotationMediaTypes.LIDAR
        else:
            self.media_type = AnnotationMediaTypes.IMAGE

    def set_provider(self):
        self.provider = AnnotationProviders.SCALE

    def set_annotation_type(self):
        if self.scaleapi_type == 'annotation':
            self.annotation_type = AnnotationTypes.TWO_D_BOUNDING_BOX
        elif self.scaleapi_type == 'segmentannotation':
            self.annotation_type = AnnotationTypes.SEMANTIC_SEGMENTATION
        elif self.scaleapi_type == 'polygonannotation':
            self.annotation_type = AnnotationTypes.POLYGON
        elif self.scaleapi_type == 'imageannotation':
            self.annotation_type = AnnotationTypes.LINE
        elif self.scaleapi_type == 'lidarannotation':
            self.annotation_type = AnnotationTypes.CUBOID
        else:
            raise InvalidAnnotationError(
                'invalid annotation type {}'.format(
                    self.scaleapi_type))

    def set_annotation_entities(self):
        if self.scaleapi_type == 'annotation':
            self.__set_bounding_box_annotation_entities()
        elif self.scaleapi_type == 'segmentannotation':
            self.__set_semantic_segmentation_annotation_entities()
        elif self.scaleapi_type == 'polygonannotation':
            self.__set_polygon_annotation_entities()
        elif self.scaleapi_type == 'imageannotation':
            self.__set_line_annotation_entities()
        elif self.scaleapi_type == 'lidarannotation':
            self.__set_lidar_annotation_entities()
        else:
            raise InvalidAnnotationError(
                'invalid annotation type {}'.format(
                    self.scaleapi_type))

    def set_set_membership(self):
        self.sets = [self.metadata.get("output_set_id")]

    def __set_bounding_box_annotation_entities(self):

        self.annotation_entities = []

        if not isinstance(self.scaleapi_annotations, list):
            raise InvalidAnnotationError(
                'bounding box annotation is expected to be list')

        for scaleapi_annotation in self.scaleapi_annotations:
            try:
                width = scaleapi_annotation['width']
                height = scaleapi_annotation['height']
                left = scaleapi_annotation['left']
                top = scaleapi_annotation['top']
                label = scaleapi_annotation['label']
            except KeyError as e:
                raise InvalidAnnotationError(str(e))

            coordinates = [
                {
                    'x': left,
                    'y': top
                },
                {
                    'x': left + width,
                    'y': top
                },
                {
                    'x': left + width,
                    'y': top + height
                },
                {
                    'x': left,
                    'y': top + height
                }
            ]
            self.annotation_entities.append(AnnotationEntity(
                {
                    'label': label,
                    'annotation_type': 'two_d_bounding_box',
                    'coordinates': coordinates,
                    'attributes': scaleapi_annotation.get('attributes')
                }, annotation_uid=self.id
            ))

    def __set_semantic_segmentation_annotation_entities(self):

        if not isinstance(self.scaleapi_annotations, dict):
            raise InvalidAnnotationError(
                'bounding box annotation is expected to be dict')

        self.annotation_entities = []

        if 'unlabeled' in self.scaleapi_annotations:
            self.annotation_entities.append(AnnotationEntity({
                'label': 'unlabeled',
                'annotation_type': 'semantic_segmentation',
                'url': self.scaleapi_annotations['unlabeled']
            }, annotation_uid=self.id))

        labeled_dic = self.scaleapi_annotations.get('labeled', {})
        for label in labeled_dic:
            value = labeled_dic[label]
            if isinstance(value, list):
                for url in value:
                    self.annotation_entities.append(AnnotationEntity({
                        'label': label,
                        'annotation_type': 'semantic_segmentation',
                        'url': url
                    }, annotation_uid=self.id))
            else:
                self.annotation_entities.append(AnnotationEntity({
                    'label': label,
                    'annotation_type': 'semantic_segmentation',
                    'url': value
                }, annotation_uid=self.id))

    def __set_polygon_annotation_entities(self):
        self.annotation_entities = []

        if not isinstance(self.scaleapi_annotations, list):
            raise InvalidAnnotationError(
                'polygon annotation is expected to be list')

        for scaleapi_annotation in self.scaleapi_annotations:
            try:
                coordinates = scaleapi_annotation['vertices']
                key = scaleapi_annotation.get('key')
                label = scaleapi_annotation['label']
            except KeyError as e:
                raise InvalidAnnotationError(str(e))

            self.annotation_entities.append(AnnotationEntity(
                {
                    'label': label,
                    'annotation_type': 'polygon',
                    'coordinates': coordinates,
                    'attributes': scaleapi_annotation.get('attributes'),
                    'uid': key
                }, annotation_uid=self.id
            ))

    def __set_line_annotation_entities(self):
        self.annotation_entities = []

        if not isinstance(self.scaleapi_annotations, list):
            raise InvalidAnnotationError(
                'line annotation is expected to be list')

        for scaleapi_annotation in self.scaleapi_annotations:
            try:
                coordinates = scaleapi_annotation['vertices']
                key = scaleapi_annotation['key']
                label = scaleapi_annotation['label']
            except KeyError as e:
                raise InvalidAnnotationError(str(e))

            self.annotation_entities.append(AnnotationEntity(
                {
                    'label': label,
                    'annotation_type': 'line',
                    'coordinates': coordinates,
                    'attributes': scaleapi_annotation.get('attributes'),
                    'uid': key
                }, annotation_uid=self.id
            ))

    def __set_lidar_annotation_entities(self):

        self.annotation_entities = []

        if not isinstance(self.scaleapi_annotations, list):
            raise InvalidAnnotationError(
                'lidar annotation is expected to be list')

        for scaleapi_annotation in self.scaleapi_annotations:
            try:
                width = scaleapi_annotation['width']
                height = scaleapi_annotation['height']
                left = scaleapi_annotation['left']
                top = scaleapi_annotation['top']
                label = scaleapi_annotation['label']
            except KeyError as e:
                raise InvalidAnnotationError(str(e))

            coordinates = [
                {
                    'x': left,
                    'y': top
                },
                {
                    'x': left + width,
                    'y': top
                },
                {
                    'x': left + width,
                    'y': top + height
                },
                {
                    'x': left,
                    'y': top + height
                }
            ]
            self.annotation_entities.append(AnnotationEntity(
                {
                    'label': label,
                    'annotation_type': 'cuboid',
                    'coordinates': coordinates,
                    'attributes': scaleapi_annotation.get('attributes')
                }, annotation_uid=self.id
            ))
