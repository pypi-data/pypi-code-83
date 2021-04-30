# Importing necessary libraries


from InfiniteList import *
from timeit import default_timer as timer
import random


def main():
    # Creating the files to store data of tests.

    tests_append_data_file = open("InfiniteList_versus_list_append.txt", "w+")
    tests_append_data_file.write("Test Number, InfiniteList, list\n")
    tests_sort_data_file = open("InfiniteList_versus_list_sort.txt", "w+")
    tests_sort_data_file.write("Test Number, InfiniteList, list\n")

    # Implementing 100 tests

    for i in range(100):
        # Test 1: Adding 100 random numbers

        # a. Using InfiniteList
        start_append1 = timer()
        inf_list: InfiniteList = InfiniteList()
        for k in range(100):
            inf_list.append(random.random())

        end_append1 = timer()
        InfiniteList_append_time = end_append1 - start_append1

        # b. Using list
        start_append2 = timer()
        a_list: list = []
        for k in range(100):
            a_list.append(random.random())

        end_append2 = timer()
        list_append_time = end_append2 - start_append2
        tests_append_data_file.write(str(i + 1) + ", " + str(InfiniteList_append_time) + " seconds, " +
                                     str(list_append_time) + " seconds\n")

        # Test 2: Sorting a list of 100 random numbers

        # a. Using InfiniteList
        start_sort1 = timer()
        inf_list.sort()
        end_sort1 = timer()
        InfiniteList_sort_time = end_sort1 - start_sort1

        # b. Using list
        start_sort2 = timer()
        a_list.sort()
        end_sort2 = timer()
        list_sort_time = end_sort2 - start_sort2
        tests_sort_data_file.write(str(i + 1) + ", " + str(InfiniteList_sort_time) + " seconds, " +
                                     str(list_sort_time) + " seconds\n")

        # print(sys.getsizeof(a_list))  # 920
        # print(sys.getsizeof(inf_list))  # 48


if __name__ == '__main__':
    main()
