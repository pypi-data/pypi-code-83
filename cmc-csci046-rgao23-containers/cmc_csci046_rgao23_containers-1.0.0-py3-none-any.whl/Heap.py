'''
This file implements the Heap data structure as a subclass of the BinaryTree.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            self.insert_list(list(xs))

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        left = True
        right = True
        if node is None:
            return True
        if node.left is not None:
            if node.value > node.left.value:
                return False
            else:
                left = Heap._is_heap_satisfied(node.left)
        if node.right is not None:
            if node.value > node.right.value:
                return False
            else:
                right = Heap._is_heap_satisfied(node.right)
        return left and right

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is

        HINT:
        Create a @staticmethod helper function,
        '''
        if self.root is not None:
            leng = self.__len__()
            binary_num = "{0:b}".format(leng + 1)[1:]
            self.root = Heap._insert(value, self.root, binary_num)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, node, binary_num):
        if binary_num[0] == '0':
            if node.left is not None:
                node.left = Heap._insert(value, node.left, binary_num[1:])
            else:
                node.left = Node(value)

        if binary_num[0] == '1':
            if node.right is not None:
                node.right = Heap._insert(value, node.right, binary_num[1:])
            else:
                node.right = Node(value)

        if binary_num[0] == '0':
            if node.left.value < node.value:
                swap = node.value
                node.value = node.left.value
                node.left.value = swap
                return node
            else:
                return node

        if binary_num[0] == '1':
            if node.right.value < node.value:
                swap = node.value
                node.value = node.right.value
                node.right.value = swap
                return node
            else:
                return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right

        HINT:
        '''
        if self.root is None:
            pass
        else:
            leng = self.__len__()
            binary_num = "{0:b}".format(leng)[1:]
            last, self.root = Heap._remove_bottom_right(self.root, binary_num)
            if self.root:
                self.root.value = last
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, binary_num):
        tobedeleted = ""
        if len(binary_num) == 0:
            return None, None

        if binary_num[0] == '0':
            if len(binary_num) == 1:
                tobedeleted = node.left.value
                node.left = None
            else:
                tobedeleted, node.left = Heap._remove_bottom_right(
                    node.left, binary_num[1:])

        if binary_num[0] == '1':
            if len(binary_num) == 1:
                tobedeleted = node.right.value
                node.right = None
            else:
                tobedeleted, node.right = Heap._remove_bottom_right(
                    node.right, binary_num[1:])

        return tobedeleted, node

    @staticmethod
    def _trickle(node):
        if Heap._is_heap_satisfied(node):
            pass
        else:
            if node.left is None and node.right is not None:
                swap = node.value
                node.value = node.right.value
                node.right.value = swap
                node.right = Heap._trickle(node.right)
            elif node.left is not None and node.right is None:
                swap = node.value
                node.value = node.left.value
                node.left.value = swap
                node.left = Heap._trickle(node.left)
            elif node.left.value <= node.right.value:
                swap = node.value
                node.value = node.left.value
                node.left.value = swap
                node.left = Heap._trickle(node.left)
            elif node.left.value >= node.right.value:
                swap = node.value
                node.value = node.right.value
                node.right.value = swap
                node.right = Heap._trickle(node.right)
            else:
                pass
        return node
