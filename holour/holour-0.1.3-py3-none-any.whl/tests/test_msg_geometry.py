from unittest import TestCase

from holour import json_encode, json_decode
from holour.msg import Vector3, Pose, Poses


class Test(TestCase):

    def test_vector3(self):
        vector3 = Vector3(1, 2, 3)
        vector3_string = json_encode(vector3)

        assert type(vector3_string) == str
        assert vector3_string == '{"_type": "vector3", "x": 1, "y": 2, "z": 3}', f"Got: {vector3_string}"

        vector3_decoded = json_decode(vector3_string)
        assert type(vector3_decoded) == Vector3
        assert vector3_decoded.x == 1
        assert vector3_decoded == vector3

    def test_vector3_equals(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(1, 2, 3)
        v3 = Vector3(3000, 2, 3)

        assert v1 == v2
        assert v1 != v3
        assert v1 != "hej"

    def test_pose(self):
        name = "waypoint_1"
        position = Vector3(1, 2, 3)
        orientation = Vector3(-1.1, -1.2, 1.3)
        pose = Pose(position, orientation, name)
        pose_string = json_encode(pose)

        assert type(pose_string) == str
        assert pose_string == '{"_type": "pose", "name": "waypoint_1", ' \
                              '"position": {"_type": "vector3", "x": 1, "y": 2, "z": 3}, ' \
                              '"orientation": {"_type": "vector3", "x": -1.1, "y": -1.2, "z": 1.3}}'

        pose_decoded: Pose = json_decode(pose_string)
        assert type(pose_decoded) == Pose, f"Expected object of type {Pose}"
        assert pose_decoded.name == name
        assert pose_decoded.position == position
        assert pose_decoded.orientation == orientation
        assert pose_decoded == pose

    def test_pose_equals(self):
        pose1 = Pose(Vector3(1, 2, 3), Vector3(-1.1, -1.2, 1.3))
        pose2 = Pose(Vector3(1, 2, 3), Vector3(-1.1, -1.2, 1.3))
        pose3 = Pose(Vector3(1, 2, 3), Vector3(-1.1, -1.2, 1.3), "some name")

        assert pose1 == pose2
        assert pose1 != pose3
        assert pose1 != "hej"

    def test_poses(self):
        list_of_poses = [
            Pose(Vector3(1, 1, 1), Vector3(-1.1, -1.2, 1.3), "waypoint_1"),
            Pose(Vector3(2, 2, 2), Vector3(-1.2, -1.1, 1.3), "waypoint_2"),
            Pose(Vector3(3, 3, 3), Vector3(-1.3, -1.2, 1.1), "waypoint_3"),
            Pose(Vector3(3, 3, 3), Vector3(-1.3, -1.2, 1.1), "waypoint_4"),
        ]
        poses = Poses(list_of_poses)

        poses_string = json_encode(poses)
        assert type(poses_string) == str
        assert "connected" in poses_string
        assert "poses" in poses_string

        poses_decoded: Poses = json_decode(poses_string)
        assert type(poses_decoded) == Poses, f"Got: {type(poses_decoded)}. Expected {Poses}"
        assert len(poses_decoded.poses) == len(list_of_poses)
        assert poses_decoded.poses == list_of_poses
        assert poses_decoded == poses, "The decoded object must be equal to the encoded"

    def test_poses_equals(self):
        list_of_poses = [
            Pose(Vector3(1, 1, 1), Vector3(-1.1, -1.2, 1.3), "waypoint_1"),
            Pose(Vector3(2, 2, 2), Vector3(-1.2, -1.1, 1.3), "waypoint_2"),
        ]
        poses1 = Poses(list_of_poses)
        poses2 = Poses(list_of_poses)
        poses3 = Poses(list_of_poses, connected=True)

        assert poses1 == poses2
        assert poses1 != poses3
        assert poses1 != list_of_poses

    def test_poses_add(self):
        pose = Pose(Vector3(1, 1, 1), Vector3(-1.1, -1.2, 1.3), "waypoint_1")
        poses = Poses([])
        poses.add(pose)

        assert len(poses.poses) == 1
        assert pose in poses.poses
