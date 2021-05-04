'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in
the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, root=None, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a
        balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        lft = AVLTree._is_avl_satisfied(node.left)
        rght = AVLTree._is_avl_satisfied(node.right)
        return AVLTree._balance_factor(node) in [-1, 0, 1] and lft and rght

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None:
            return node
        if node.right is None:
            return node
        pholder = Node(node.right.value)
        pholder.right = node.right.right
        lnode = Node(node.value)
        lnode.left = node.left
        lnode.right = node.right.left
        pholder.left = lnode
        return pholder

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is
        fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None:
            return node
        if node.left is None:
            return node
        pholder = Node(node.left.value)
        pholder.left = node.left.left
        rnode = Node(node.value)
        rnode.right = node.right
        rnode.left = node.left.right
        pholder.right = rnode
        return pholder

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview
        of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your
        insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
            return
        if value == self.root.value:
            return
        else:
            self._insert(value, self.root)
            if self.is_avl_satisfied() is False:
                self.root = self.rebalance(self.root)
                if self.is_avl_satisfied() is False:
                    self.root = self.rebalance(self.root)
            return

    @staticmethod
    def _insert(value, node):
        if value == node.value:
            return
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
                return
            elif node.right is not None:
                return AVLTree._insert(value, node.right)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            elif node.left is not None:
                return AVLTree._insert(value, node.left)

    def rebalance(self, i):
        if i is None:
            return
        if self._balance_factor(i) in [-2, 2]:
            i = self._rebalance(i)
        else:
            i.left = self.rebalance(i.left)
            i.right = self.rebalance(i.right)
        return i

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node is None:
            return
        bf = AVLTree._balance_factor(node)
        if bf > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            elif AVLTree._balance_factor(node.left) >= 0:
                node = AVLTree._right_rotate(node)
            return node
        elif bf < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            elif AVLTree._balance_factor(node.right) <= 0:
                node = AVLTree._left_rotate(node)
            return node
        else:
            pass
