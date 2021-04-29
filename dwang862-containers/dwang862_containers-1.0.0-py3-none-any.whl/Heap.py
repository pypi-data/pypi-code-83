'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with
an *explicit* vector implementation,
so the code in the book is likely to be less helpful
than the code for the other data structures.
The book's implementation is the traditional implementation
because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help you get more
practice with OOP-style programming and classes.
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
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that
        can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"
        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap
        will have a correct implementation of __repr__, and that
        they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure, the first thing to do
        is to implement a function that checks whether the
        structure obeys all of its laws.
        This makes it possible to automatically test whether
        insert/delete functions are actually working.
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
        if node.left:
            left = node.value <= node.left.value and\
                Heap._is_heap_satisfied(node.left)
        if node.right:
            right = node.value <= node.right.value and\
                Heap._is_heap_satisfied(node.right)
        return left and right

    def insert(self, value):
        '''
        Inserts value into the heap.
        FIXME:
        Implement this function.
        HINT:
        The pseudo code is
        1. Find the next position in the tree using the
        binary representation of the total number of nodes
            1. You will have to explicitly store the size of your heap in a
            variable (rather than compute it) to maintain the O(log n) runtime
            1. See https://stackoverflow.com/questions/18241192/implement-heap
            -using-a-binary-tree for hints
        1. Add `value` into the next position
        1. Recursively swap value with its parent until the
        heap property is satisfied
        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the
        BST and AVLTree insert functions.
        '''
        if self.root:
            node_size = self.__len__()
            path = "{0:b}".format(node_size + 1)
            self.root = Heap._insert(self.root, value, path[1:])
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, path):
        if path[0] == '1':
            if not node.right:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, value, path[1:])
        if path[0] == '0':
            if not node.left:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, value, path[1:])
        if path[0] == '1':
            if node.right.value < node.value:
                var = node.value
                node.value = node.right.value
                node.right.value = var
                return node
            else:
                return node
        if path[0] == '0':
            if node.left.value < node.value:
                var = node.value
                node.value = node.left.value
                node.left.value = var
                return node
            else:
                return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for i in list(xs):
            self.insert(i)

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
        3. "trickle down" the root node: recursively swap it
        with its largest child
        until the heap property is satisfied
        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a
        single helper (or no helper at all),
        but I personally found dividing up the code
        into two made the most sense.
        '''
        if not self.root:
            pass
        else:
            nodes = self.__len__()
            path = "{0:b}".format(nodes)[1:]
            rem_value, self.root = Heap._remove_bottom_right(self.root, path)
            if self.root:
                self.root.value = rem_value
            print(str(self.root))
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, path):
        rem_value = ""
        if len(path) == 0:
            return None, None
        if path[0] == '1':
            if len(path) == 1:
                rem_value = node.right.value
                node.right = None
            else:
                rem_value, node.right = Heap._remove_bottom_right(
                    node.right, path[1:])
        if path[0] == '0':
            if len(path) == 1:
                rem_value = node.left.value
                node.left = None
            else:
                rem_value, node.left = Heap._remove_bottom_right(
                    node.left, path[1:])
        print(rem_value, str(node))
        return rem_value, node

    @staticmethod
    def _trickle(node):
        if Heap._is_heap_satisfied(node):
            pass
        else:
            if not node.right and node.left:
                var = node.value
                node.value = node.left.value
                node.left.value = var
                node.left = Heap._trickle(node.left)
            elif not node.left and node.right:
                var = node.value
                node.value = node.right.value
                node.right.value = var
                node.right = Heap._trickle(node.right)
            elif node.left.value >= node.right.value:
                var = node.value
                node.value = node.right.value
                node.right.value = var
                node.right = Heap._trickle(node.right)
            elif node.left.value <= node.right.value:
                var = node.value
                node.value = node.left.value
                node.left.value = var
                node.left = Heap._trickle(node.left)
            else:
                pass
        return node
