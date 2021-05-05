'''
This file implements the AVL Tree data structure.
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

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        self.xs = xs
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
        '''
        if self.root:
            return AVLTree._is_avl_satisfied(self.root)
        else:
            return True

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ranges = [-1, 0, 1]
        boolean = True
        if node:
            if AVLTree._balance_factor(node) not in ranges:
                return False
        if node.left:
            if AVLTree._balance_factor(node.left) not in ranges:
                boolean = False
            else:
                boolean &= AVLTree._is_avl_satisfied(node.left)
        if node.right:
            if AVLTree._balance_factor(node.right) not in ranges:
                boolean = False
            else:
                boolean &= AVLTree._is_avl_satisfied(node.right)
        return boolean

    @staticmethod
    def _copy_nodes(node):
        if node:
            copy = Node(node.value, AVLTree._copy_nodes(node.left),
                        AVLTree._copy_nodes(node.right))
        else:
            return None
        return copy

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        copiednode = AVLTree._copy_nodes(node)
        newnode = copiednode.right
        keep = newnode.left
        newnode.left = copiednode
        copiednode.right = keep
        return newnode

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        copiednode = AVLTree._copy_nodes(node)
        newnode = copiednode.left
        keep = newnode.right
        newnode.right = copiednode
        copiednode.left = keep
        return newnode

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        and the textbook provides full python code.
        however, so you will have to adapt their code.

        HINT:
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is not None:
            AVLTree._insert(value, self.root)
            rebalance = AVLTree._rebalance(self.root)
            self.root = rebalance
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left:
                AVLTree._insert(value, node.left)
                rebalance = AVLTree._rebalance(node.left)
                node.left = rebalance
            else:
                node.left = Node(value)
                rebalance = AVLTree._rebalance(node.left)
                node.left = rebalance
        if value > node.value:
            if node.right:
                AVLTree._insert(value, node.right)
                rebalance = AVLTree._rebalance(node.right)
                node.right = rebalance
            else:
                node.right = Node(value)
                rebalance = AVLTree._rebalance(node.right)
                node.right = rebalance

    def insert_list(self, xs):
        if xs is not None:
            for x in xs:
                self.insert(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                right = AVLTree._right_rotate(node.right)
                node.right = right
                left = AVLTree._left_rotate(node)
                node = left
            else:
                left = AVLTree._left_rotate(node)
                node = left
            return node
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                left = AVLTree._left_rotate(node.left)
                node.left = left
                right = AVLTree._right_rotate(node)
                node = right
            else:
                right = AVLTree._right_rotate(node)
                node = right
            return node
        else:
            return node
