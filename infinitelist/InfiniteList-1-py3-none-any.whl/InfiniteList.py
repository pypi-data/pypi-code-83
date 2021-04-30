"""
This file contains code for the data type "InfiniteList".
Author: GlobalCreativeCommunityFounder
"""


# Importing necessary libraries


import copy
# import sys
from mpmath import *
mp.pretty = True


# Creating InfiniteList class


class InfiniteList:
    """
    This class contains attributes of an infinite list.
    """

    def __init__(self, elements=None):
        # type: (list) -> None
        self.list_count: int = 0  # initial value
        self.MAX_SUBLIST_SIZE: int = 50  # a reasonable number of elements allowed per
        # sublist to ensure that the data type runs fast and is good for storing many elements

        if elements is None:
            elements = []

        # Transferring all elements from 'elements' list to this infinite list.
        num_lists: int = 1 + (len(elements) // self.MAX_SUBLIST_SIZE)  # The number of sub lists required
        for i in range(num_lists):
            self.__add_sublist()
            curr_list: list = elements[0:self.MAX_SUBLIST_SIZE] if len(elements) >= self.MAX_SUBLIST_SIZE \
                else elements
            self.__setattr__("list" + str(i + 1), curr_list)

    def copy(self):
        # type: () -> InfiniteList
        return copy.deepcopy(self)

    def count(self, elem):
        # type: (object) -> int
        result: int = 0
        for i in range(self.__len__()):
            if self.__getitem__(i) == elem:
                result += 1

        return result

    def index(self, elem):
        # type: (object) -> int
        for i in range(self.__len__()):
            if self.__getitem__(i) == elem:
                return i

        return -1

    def reverse(self):
        # type: () -> None
        reversed_infinite_list: InfiniteList = InfiniteList()  # initial value
        saved_list_count: int = self.list_count  # saving the initial value of 'self.list_count'
        for i in range(self.list_count, 0, -1):
            curr_list: list = self.__getattribute__("list" + str(i))
            curr_list.reverse()
            reversed_infinite_list.extend(curr_list)

        self.clear()
        for i in range(saved_list_count):
            self.__add_sublist()
            self.__setattr__("list" + str(i + 1), reversed_infinite_list.__getattribute__("list" + str(i + 1)))

    def sort(self):
        # type: () -> None
        for i in range(self.__len__()):
            minimum_index: int = i
            for j in range(i + 1, self.__len__()):
                if self.__getitem__(minimum_index) > self.__getitem__(j):
                    minimum_index = j

            temp1 = self.__getitem__(i)
            temp2 = self.__getitem__(minimum_index)
            self.__setitem__(minimum_index, temp1)
            self.__setitem__(i, temp2)

    def min(self):
        # type: () -> object
        return min(min(self.__getattribute__("list" + str(i))) for i in range(1, self.list_count + 1))

    def max(self):
        # type: () -> object
        return max(max(self.__getattribute__("list" + str(i))) for i in range(1, self.list_count + 1))

    def sum(self):
        # type: () -> mpf
        return mpf(sum(sum(self.__getattribute__("list" + str(i))) for i in range(1, self.list_count + 1)))

    def extend(self, a_list):
        # type: (list) -> None
        for elem in a_list:
            self.append(elem)

    def insert(self, pos, elem):
        # type: (int, object) -> None
        if pos < 0 or pos >= self.__len__():
            raise Exception("InfiniteList index out of range!")
        else:
            last_list: list = self.__getattribute__("list" + str(self.list_count))
            last_elem: object = last_list[len(last_list) - 1]
            if len(last_list) == self.MAX_SUBLIST_SIZE:
                self.__add_sublist()
            for index in range(self.__len__() - 1, pos, -1):
                self.__setitem__(index, self.__getitem__(index - 1))

            self.__setitem__(pos, elem)
            self.append(last_elem)

    def append(self, elem):
        # type: (object) -> None
        last_list: list = self.__getattribute__("list" + str(self.list_count))
        if len(last_list) < self.MAX_SUBLIST_SIZE:
            last_list.append(elem)
        else:
            self.__add_sublist()
            last_list = self.__getattribute__("list" + str(self.list_count))
            last_list.append(elem)

    def delete(self, index):
        # type: (int) -> None
        if index < 0 or index >= self.__len__():
            raise Exception("InfiniteList index out of range!")

        for curr_index in range(index, self.__len__() - 1):
            self.__setitem__(curr_index, self.__getitem__(curr_index + 1))

        last_list: list = self.__getattribute__("list" + str(self.list_count))
        last_list.remove(last_list[len(last_list) - 1])

        if self.list_count > 1:
            before_last_list: list = self.__getattribute__("list" + str(self.list_count - 1))

            # Remove the last list if it is empty and the previous list is not full
            if len(last_list) == 0 and len(before_last_list) < self.MAX_SUBLIST_SIZE:
                self.__remove_sublist()
        else:
            if len(last_list) == 0:
                self.__remove_sublist()

    def remove(self, elem):
        # type: (object) -> bool
        elem_index: int = -1  # initial value
        for index in range(self.__len__()):
            if self.__getitem__(index) == elem:
                elem_index = index
                break

        if elem_index == -1:
            return False

        for index in range(elem_index, self.__len__() - 1):
            self.__setitem__(index, self.__getitem__(index + 1))

        last_list: list = self.__getattribute__("list" + str(self.list_count))
        last_list.remove(last_list[len(last_list) - 1])

        if self.list_count > 1:
            before_last_list: list = self.__getattribute__("list" + str(self.list_count - 1))

            # Remove the last list if it is empty and the previous list is not full
            if len(last_list) == 0 and len(before_last_list) < self.MAX_SUBLIST_SIZE:
                self.__remove_sublist()
        else:
            if len(last_list) == 0:
                self.__remove_sublist()

        return True

    def clear(self):
        # type: () -> None
        for i in range(1, self.list_count + 1):
            self.__setattr__("list" + str(i), [])

        for i in range(self.list_count):
            self.__remove_sublist()

    def __len__(self):
        # type: () -> InfiniteList
        if self.list_count == 0:
            return 0

        last_list: list = self.__getattribute__("list" + str(self.list_count))
        return self.MAX_SUBLIST_SIZE * (self.list_count - 1) + len(last_list)

    def __getitem__(self, index):
        # type: (int) -> object
        if index < 0 or index >= self.__len__():
            raise Exception("InfiniteList index out of range!")
        else:
            list_number: int = 1 + (index // self.MAX_SUBLIST_SIZE)
            list_index: int = index % self.MAX_SUBLIST_SIZE
            curr_list: list = self.__getattribute__("list" + str(list_number))
            return curr_list[list_index]

    def __setitem__(self, index, value):
        # type: (int, object) -> None
        if index < 0 or index >= self.__len__():
            raise Exception("InfiniteList index out of range!")
        else:
            list_number: int = 1 + (index // self.MAX_SUBLIST_SIZE)
            list_index: int = index % self.MAX_SUBLIST_SIZE
            curr_list: list = self.__getattribute__("list" + str(list_number))
            curr_list[list_index] = value
        
    def __add_sublist(self):
        # type: () -> None
        self.__setattr__("list" + str(self.list_count + 1), [])
        self.list_count += 1

    def __remove_sublist(self):
        # type: () -> None
        self.__delattr__("list" + str(self.list_count))
        self.list_count -= 1

    def __str__(self):
        # type: () -> str
        if self.__len__() == 0:
            return "[]"

        res: str = "["  # initial value
        for i in range(1, self.list_count + 1):
            curr_list = self.__getattribute__("list" + str(i))
            for j in range(len(curr_list)):
                if i == self.list_count and j == len(curr_list) - 1:
                    res += str(curr_list[j]) + "]"
                else:
                    res += str(curr_list[j]) + ", "

        return res
