'''
This file implements the Binary Search Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        self.xs = xs
        self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        t1 = self.to_list('inorder')
        t2_ordered = t2.to_list('inorder')
        if t1 == t2_ordered:
            return True
        else:
            return False

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        '''
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        '''
        if self.root:
            return BST._insert(value, self.root)
        self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is not None:
                BST._insert(value, node.left)
            else:
                node.left = Node(value)
        if value > node.value:
            if node.right is not None:
                BST._insert(value, node.right)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        '''
        if xs is not None:
            for n in xs:
                self.insert(n)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root is None:
            return False
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is not None:
            if value > node.value:
                return BST._find(value, node.right)
            elif value < node.value:
                return BST._find(value, node.left)
            else:
                return True
        else:
            return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:

        HINT:
        Use a recursive helper function.
        '''
        if value in self:
            if self.root.value == value:
                if self.root.right:
                    swap = BST._find_smallest(self.root.right)
                    self.root.value = swap
                    self.root.right = BST._remove(self.root.right, swap)
                    return self.root
                elif self.root.left:
                    swap = BST._find_largest(self.root.left)
                    self.root.value = swap
                    self.root.left = BST._remove(self.root.left, swap)
                    return self.root
                else:
                    self.root = None
                    return self.root
            else:
                return BST._remove(self.root, value)
        else:
            pass

    @staticmethod
    def _remove(root, value):
        if root is None:
            return root
        elif value < root.value:
            root.left = BST._remove(root.left, value)
        elif value > root.value:
            root.right = BST._remove(root.right, value)
        else:
            if root.left is None:
                change = root.right
                root = None
                return change
            elif root.right is None:
                change = root.left
                root = None
                return change
            else:
                change = BST._find_largest(root.left)
                root.value = change
                root.left = BST._remove(root.left, change)
        return root

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
        for x in xs:
            self.remove(x)
