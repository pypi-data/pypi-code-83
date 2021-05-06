"""Tracking module"""
import abc
import uuid
from collections import deque, OrderedDict
import cv2
import dlib
import numpy
from .utils import bbox_center, rect_to_bbox, iou, bbox_to_rect


class BaseTracker(object):
    """BaseTracker class"""
    __metaclass__ = abc.ABCMeta

    def __init__(
            self, threshold=10.0, min_feats=1, track_movements=0,
            max_steps=20):
        """
        Args:
            threshold (float): default 10, value between 0 and 30
            min_feats (integer): minimum number of features to keep, used for multi frame inference
            track_movements (integer): value between 0 and 1, records movement of objects
            max_steps (integer): number of movements to keep in tracked object
        """
        self.tracked_objects = OrderedDict()
        self.threshold = float(threshold)
        self.min_feats = min_feats
        self.track_movements = track_movements
        self.max_steps = max_steps

    def draw_motion_tracks(self, frame):
        """
        draw motion tracks on frame
        Args:
            frame: numpy/opencv frame to draw movements on
        """
        for oid in self.tracked_objects.keys():
            if len(self.tracked_objects[oid]['movements']) > 3:
                for idx, centerpoint in enumerate(
                        self.tracked_objects[oid]['movements']):
                    if idx == 0:
                        continue
                    thickness = int(numpy.sqrt(20 / float(idx + 1)) * 2.5)
                    cv2.line(
                        frame,
                        self.tracked_objects[oid]['movements'][int(idx - 1)],
                        self.tracked_objects[oid]['movements'][int(idx)],
                        (0, 0, 255), thickness)
                    if idx == self.max_steps:
                        break

    def remove_unknown_identities(self):
        """
        removes unknown identities that haven't been identitied and that reached the max feature count
        """
        for oid in self.tracked_objects.keys():
            identity_is_none = self.tracked_objects[oid]['identity'] is None
            min_feats_reached = len(
                self.tracked_objects[oid]['features']) > self.min_feats
            if identity_is_none and min_feats_reached:
                self.tracked_objects.pop(oid)

    @abc.abstractmethod
    def track(
            self, object_to_track, image, identity, chip=None,
            related_object=None):
        """Abstract method"""

    @abc.abstractmethod
    def update(self, bboxes, frame, chips=None, features=None):
        """Abstract method"""

    def clean(self):
        """clean tracked objects, removes idenities that fell below the threshold"""
        tracked_objects = self.tracked_objects.copy()
        for oid in tracked_objects.keys():
            tracker_quality = self.tracked_objects[oid].get('quality')
            if (isinstance(tracker_quality, bool) and not tracker_quality) \
                or (isinstance(tracker_quality, float) and
                        tracker_quality < float(self.threshold)):
                for _oid in self.tracked_objects.keys():
                    if self.tracked_objects[_oid]['related_object'] == oid:
                        self.tracked_objects[_oid]['related_object'] = None
                self.tracked_objects.pop(oid, None)

    @abc.abstractmethod
    def find_tracked_object(self, bbox, image):
        """Abstract method"""


class CVObjectTracker(BaseTracker):
    """A Tracking class that exposes 8 Opencv Trackers"""
    def __init__(
            self, threshold, min_feats=1, track_movements=0, max_steps=20,
            tracker_type='KCF'):
        """
        Args:
            threshold (float): default 10, value between 0 and 30
            min_feats (integer): minimum number of features to keep, used for multi frame inference
            track_movements (integer): value between 0 and 1, records movement of objects
            max_steps (integer): number of movements to keep in tracked object
            tracker_type (str): one of the following choices (BOOSTING, MIL, TLD, MEDIANFLOW, GOTURN, MOSSE, CSRT)
        """
        super(CVObjectTracker, self).__init__(
            threshold, min_feats, track_movements)
        self.tracker_type = tracker_type
        self.track_movements = track_movements

    def track(
            self, object_to_track, image, identity, chip=None, features=None,
            related_object=None):
        """
        track object
        Args:
            object_to_track (list): rectangle containing object to track
            image: numpy or opencv image
            identity: identity label if avaliable
            chip: extracted face chip, used in face averaging and multi frame inference
            features: face recognition features, used in multi frame inference
            related_object: related tracked object
        """
        bbox = rect_to_bbox(object_to_track)
        if self.tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if self.tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if self.tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if self.tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if self.tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if self.tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if self.tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if self.tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()

        success = tracker.init(image, bbox)
        object_id = uuid.uuid4()
        self.tracked_objects[object_id] = {
            'quality': success,
            'tracker': tracker,
            'identity': identity,
            'bbox': bbox,
            'chip': chip,
            'features': [features, ],
            'related_object': related_object}

        if self.track_movements > 0:
            self.tracked_objects[object_id]['movements'] = deque(
                maxlen=self.track_movements)
            self.tracked_objects[object_id]['movements'].appendleft(
                bbox_center(bbox))

        return object_id

    def find_tracked_object(self, obj, frame):
        """
        Matches passed obj to a tracked obj
        Args:
            object: bounding box of object to find
            frame: numpy of opencv frame
        returns:
            found: boolean
            matched_oid: id of matched object in the tracked object array
            bbox: bounding box of matched object
        """
        matched_oid = None
        found = False
        bbox = None

        x, y, w, h = rect_to_bbox(obj)

        x_bar = x + 0.5 * w
        y_bar = y + 0.5 * h

        for oid in self.tracked_objects.keys():
            found, bbox = self.tracked_objects[oid]['tracker'].update(frame)

            t_x = int(bbox[0])
            t_y = int(bbox[1])
            t_w = int(bbox[2])
            t_h = int(bbox[3])

            t_x_bar = t_x + 0.5 * t_w
            t_y_bar = t_y + 0.5 * t_h
            if ((t_x <= x_bar <= (t_x + t_w)) and
                    (t_y <= y_bar <= (t_y + t_h)) and
                    (x <= t_x_bar <= (x + w)) and
                    (y <= t_y_bar <= (y + h))):
                matched_oid = oid

        return found, matched_oid, bbox

    def update(self, bboxes, frame, chips=[], features=[]):
        """
        updates tracked object positions
        Args:
            bounding boxes
            frame: numpy/opencv frame
            chips (numpy/opencv image): optional, chips to store in tracked objects
            features (array): optional, features to store in tracked object

        Returns:
            an array of known_objects and unknown_objects
        """
        known_objects = dict()
        unknown_objects = []
        #if not bboxes.shape[0]:
        if not bboxes:
            return known_objects, unknown_objects
        for bbox, chip, feats in zip(bboxes, chips, features):
            identity = None
            if self.tracked_objects:
                success, identity, object_box = self.find_tracked_object(
                    bbox, frame)
            if identity and object_box:
                known_objects[identity] = object_box
                self.tracked_objects[identity]['quality'] = success
                self.tracked_objects[identity]['bbox'] = object_box
                self.tracked_objects[identity]['chip'] = chip
                if not self.tracked_objects[identity]['related_object']:
                    self.tracked_objects[identity]['features'].append(feats)
            else:
                unknown_objects.append({
                    'chip': chip,
                    'bounding_box': bbox,
                    'features': feats})

        return known_objects, unknown_objects


class COObjectTracker(BaseTracker):
    """A tracker class utilizing a correlation based tracker
    Args:
        threshold (float): default 10, value between 0 and 30
        min_feats (integer): minimum number of features to keep, used for multi frame inference
        track_movements (integer): value between 0 and 1, records movement of objects
        max_steps (integer): number of movements to keep in tracked object
    """
    def __init__(
            self, threshold, min_feats=1, track_movements=0, max_steps=20):
        super(COObjectTracker, self).__init__(
            threshold, min_feats, track_movements)
        self.track_movements = track_movements

    def track(
            self, object_to_track, image, identity=None, chip=None,
            features=None, related_object=None):
        """
        Initiates the tracking of a obj
        Args:
            object_to_track (list): rectangle containing object to track
            image: numpy or opencv image
            identity: identity label if available
            chip: extracted face chip, used in face averaging and multi frame inference
            features: face recognition features, used in multi frame inference
            related_object: related tracked object

        """
        bbox = rect_to_bbox(object_to_track)

        x_object, y_object, w_object, h_object = bbox

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        tracker = dlib.correlation_tracker()
        tracker.start_track(image, dlib.rectangle(
            int(x_object),
            int(y_object),
            int(x_object + w_object),
            int(y_object + h_object)))

        object_id = uuid.uuid4()
        self.tracked_objects[object_id] = {
            'tracker': tracker,
            'identity': identity,
            'bbox': bbox,
            'chip': chip,
            'features': [features, ],
            'related_object': related_object}

        if self.track_movements > 0:
            self.tracked_objects[object_id]['movements'] = deque(
                maxlen=self.track_movements)
            self.tracked_objects[object_id]['movements'].appendleft(
                bbox_center(bbox))

        return object_id

    def update_trackers(self, frame):
        """
        update bounding box positions of trackers
        Args:
        frame: numpy/opencv frame

        """
        if self.tracked_objects:
            for oid in self.tracked_objects.keys():
                self.tracked_objects[oid]['quality'] = \
                    self.tracked_objects[oid]['tracker'].update(frame)

                tracked_position = \
                    self.tracked_objects[oid]['tracker'].get_position()
                t_x = int(tracked_position.left())
                t_y = int(tracked_position.top())
                t_w = int(tracked_position.width())
                t_h = int(tracked_position.height())
                bbox = [t_x, t_y, t_w, t_h]
                self.tracked_objects[oid]['bbox'] = bbox

    def update(self, bboxes, frame, chips=None, features=None):
        """
        updates tracked object returning known and unkown objects in the frame
        Args:
            bounding boxes
            frame: numpy/opencv frame
            chips (numpy/opencv image): optional, chips to store in tracked
            objects
            features (array): optional, features to store in tracked object

        Returns:
            an array of known_objects and unknown_objects
        """

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.update_trackers(frame)
        known_objects = dict()
        unknown_objects = []
        if not bboxes:
            return known_objects, unknown_objects

        #for bbox, chip, feats in zip(bboxes, chips, features):
        for i, bbox in enumerate(bboxes):
            identity = None
            # if self.tracked_objects.size > 0:
            (left, top, right, bottom) = bbox_to_rect(bbox)
            _, identity, object_box = self.find_tracked_object(
                bbox_to_rect(bbox), frame)
            if identity:
                known_objects[identity] = object_box
                self.tracked_objects[identity]['bbox'] = bbox
                self.tracked_objects[identity]['tracker'].start_track(frame,
                                                                      dlib.rectangle(left, top, right, bottom))
                if chips:
                    self.tracked_objects[identity]['chip'] = chips[i]
                if not self.tracked_objects[identity]['related_object']:
                    if features:
                        self.tracked_objects[identity]['features'].append(
                            features[i])
                    if self.track_movements > 0:
                        self.tracked_objects[identity]['movements'].appendleft(
                            bbox_center(object_box))
            else:
                feats = None
                chip = None
                if features is not None:
                    feats = features[i]
                if chips is not None:
                    chip = chips[i]
                unknown_objects.append({
                    'chip': chip,
                    'bounding_box': bbox,
                    'features': feats})

        return known_objects, unknown_objects


    def find_tracked_object(self, obj, frame, track_movements=False, method=2,
                            iou_threshold=0.6):
        """
        Matches passed obj to a tracked obj
        Args:
            obj: rectangle containing tracked object to find from face detect call
            frame: opencv/numpy frame

        returns:
            quality: quality  measure that can be compared against the threshold
            matched_oid: id of matched object in the tracked object array
            bbox: bounding box of matched tracked object
        """
        matched_oid = None
        containing_oids = []
        quality = None
        tracked_bbox = None
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        x, y, w, h = rect_to_bbox(obj)

        x_bar = x + 0.5 * w
        y_bar = y + 0.5 * h
        matches_ids = []
        matches = []

        if method == 1:
            for oid in self.tracked_objects.keys():
                tracked_bbox = \
                    self.tracked_objects[oid]['bbox']
                t_x, t_y, t_w, t_h = tracked_bbox
                matches.append(iou(obj, (t_x, t_y, t_x+t_w, t_y+t_h)))
                matches_ids.append(oid)
            if matches:
                max_match = numpy.max(matches)
                print(max_match)
                if max_match > 0.4:
                    matched_oid = matches_ids[matches.index(max_match)]
                return max_match, matched_oid, tracked_bbox
        else:
            for oid in self.tracked_objects.keys():
                tracked_bbox = self.tracked_objects[oid]['bbox']
                t_x, t_y, t_w, t_h = tracked_bbox
                t_x_bar = t_x + 0.5 * t_w
                t_y_bar = t_y + 0.5 * t_h
                # check if search object centroid is contained in tracked
                # object box
                if ((t_x <= x_bar <= (t_x + t_w)) and
                    (t_y <= y_bar <= (t_y + t_h))):
                    # check if tracked object centroid is also contained in
                    # search object box, the object are closely related
                    if ((x <= t_x_bar <= (x + w)) and
                       (y <= t_y_bar <= (y + h))):
                        # it's a match
                        matched_oid = oid
                        break
                    else:
                        # search object center is inside the tracked object
                        # box but the center of the tracked object is not
                        # within the search box (this is the case when you
                        # want  to associate a face to a person whose
                        # bounding box is much bigger than the face. The
                        # center  of the person box is not inside face
                        # bounding box.
                        containing_oids.append(oid)

                    if matched_oid:
                        break
            # if we have a close match, great. If we don't then go with the
            # smallest box that contains the search object
            if not matched_oid and len(containing_oids) > 0:
                # find the smallest containing object
                bboxes = [self.tracked_objects[oid]['bbox'] for oid in
                          containing_oids]
                # calculate width*height for each bbox
                areas = [bbox[2]*bbox[3] for bbox in bboxes]
                smallest_index = areas.index(min(areas))
                matched_oid = containing_oids[smallest_index]

            if matched_oid and 'quality' in self.tracked_objects[matched_oid]:
                quality = self.tracked_objects[matched_oid]['quality']
                if track_movements:
                    self.tracked_objects[matched_oid]['movements'].appendleft(
                        bbox_center(tracked_bbox))
            return quality, matched_oid, tracked_bbox