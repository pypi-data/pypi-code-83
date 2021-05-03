from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the
    class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        if node is None:
            return True
        elif node.left is None and node.right is None:
            return True
        elif node.right is None:
            return node.value <= node.left.value
        elif node.value <= node.left.value and node.value <= node.right.value:
            new_left = Heap._is_heap_satisfied(node.left)
            new_right = Heap._is_heap_satisfied(node.right)
            return new_left and new_right
        else:
            return False

    def insert(self, value):
        '''
        Inserts value into the heap.
        FIXME:
        Implement this function.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return
        if node.left and node.right:
            node.left = Heap._insert(node.left, value)
            if node.value > node.left.value:
                return Heap._swap(node, value)
        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._swap(node, value)
        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._swap(node, value)
        return node

    @staticmethod
    def _swap(node, value):
        if Heap._is_heap_satisfied(node) is True:
            return node
        if node.left and node.left.value > node.value:
            node.left = Heap._swap(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._swap(node.right, value)
        if node.right:
            if node.right.value == value:
                new_parent = node.right.value
                new_right = node.value
                node.value = new_parent
                node.right.value = new_right
        if node.left:
            if node.left.value == value:
                new_parent = node.left.value
                new_left = node.value
                node.value = new_parent
                node.left.value = new_left
        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for x in list(xs):
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
        2. replace the root node with what was
        formerly the bottom right
        3. "trickle down" the root node: recursively swap
        it with its largest child until the heap
        property is satisfied
        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a
        single helper (or no helper at all),
        but I personally found dividing up the
        code into two made the most sense.
        '''
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            old_right = Heap._bottom_right(self.root)
            self.root = Heap._remove(self.root)
            if old_right == self.root.value:
                return
            else:
                self.root.value = old_right
            if Heap._is_heap_satisfied(self.root) is False:
                return Heap._trickle(self.root)

    @staticmethod
    def _remove(node):
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None
        return node

    @staticmethod
    def _bottom_right(node):
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._bottom_right(node.right)
        elif node.left:
            return Heap._bottom_right(node.left)

    @staticmethod
    def _trickle(node):
        if node.left is None and node.right is None:
            return node
        if node.right and (node.left is None or node.right.value <= node.left.value):
            if node.right.value < node.value:
                new_parent = node.right.value
                new_right = node.value
                node.value = new_parent
                node.right.value = new_right
            node.right = Heap._trickle(node.right)
        elif node.left and (node.right is None or node.left.value <= node.right.value):
            if node.left.value < node.value:
                new_parent = node.left.value
                new_left = node.value
                node.value = new_parent
                node.left.value = new_left
            node.left = Heap._trickle(node.left)
        return node
