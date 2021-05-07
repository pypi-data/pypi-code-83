from typing import List


class Vector3:

    def __init__(self, x: float, y: float, z: float, _type: str = ''):
        self._type = 'vector3'
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector3):
            return other.x == self.x and other.y == self.y and other.z == self.z
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


class Pose:

    def __init__(self, position: Vector3, orientation: Vector3, name: str = '', _type: str = ''):
        self._type = 'pose'
        self.name = name
        self.position = position
        self.orientation = orientation

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Pose):
            return other.name == self.name and other.position == self.position and other.orientation == self.orientation
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


class Poses:

    def __init__(self, poses: List[Pose], connected: bool = False, _type: str = ''):
        self._type = 'poses'
        self.connected = connected
        self.poses = poses

    def add(self, pose: Pose):
        self.poses.append(pose)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Poses):
            return other.connected == self.connected and other.poses == self.poses
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
