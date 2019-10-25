from BinaryTree import BinaryTree


class RBNode(BinaryTree.Node):
    def __init__(self, parent, left, right, key: float, color: str):
        super().__init__(parent, left, right, key)
        self.color = color


class RBTree(BinaryTree.BinaryTree):
    def __init__(self, root: RBNode):
        super().__init__(root)

    def left_rotate(self, pivot_node: RBNode):
        if pivot_node.right is None:
            raise NameError('uncorrected node for left rotate')
        right_node = pivot_node.right

        pivot_node.right = right_node.left
        if right_node.left is not None:
            right_node.left.parent = pivot_node

        right_node.parent = pivot_node.parent
        if pivot_node.parent is None:
            self.root = right_node
        elif pivot_node is pivot_node.parent.left:
            pivot_node.parent.left = right_node
        else:
            pivot_node.parent.right = right_node

        right_node.left = pivot_node
        pivot_node.parent = right_node

    def right_rotate(self, pivot_node: RBNode):
        if pivot_node.left is None:
            raise NameError('uncorrected node for right rotate')
        left_node = pivot_node.left

        pivot_node.left = left_node.right
        if left_node.right is not None:
            left_node.right.parent = pivot_node

        left_node.parent = pivot_node.parent
        if pivot_node.parent is None:
            self.root = left_node
        elif pivot_node is pivot_node.parent.left:
            pivot_node.parent.left = left_node
        else:
            pivot_node.parent.right = left_node

        left_node.right = pivot_node
        pivot_node.parent = left_node

    def rb_insert_fixup(self, new_node: RBNode):
        while new_node.parent.colot == "Red":
            if new_node.parent is new_node.parent.parent.left:
                fix_node = new_node.parent.parent.right
                if fix_node.color == "Red":
                    new_node.parent.color = "Black"
                    fix_node.color = "Black"
                    new_node.parent.parent.color = "Red"
                    new_node = new_node.parent.parent
                elif new_node is new_node.parent.right:
                    new_node = new_node.parent
                    self.left_rotate(new_node)

                new_node.parent.color = "Black"
                new_node.parent.parent.color = "Red"
                self.right_rotate(new_node.parent.parent)
            else:
                fix_node = new_node.parent.parent.right
                if fix_node.color == "Red":
                    new_node.parent.color = "Black"
                    fix_node.color = "Black"
                    new_node.parent.parent.color = "Red"
                    new_node = new_node.parent.parent
                elif new_node is new_node.parent.right:
                    new_node = new_node.parent
                    self.right_rotate(new_node)

                new_node.parent.color = "Black"
                new_node.parent.parent.color = "Red"
                self.left_rotate(new_node.parent.parent)

    def rb_insert(self, new_node: RBNode):
        node_y = None
        node_x = self.root
        while node_x is not None:
            node_y = node_x
            if new_node.key < node_x.key:
                node_x = node_x.left
            else:
                node_x = node_x.right
        new_node.parent = node_y
        if node_y is None:
            self.root = new_node
        elif new_node.key < node_y.key:
            node_y.left = new_node
        else:
            node_y.right = new_node
        new_node.left = None
        new_node.right = None
        new_node.color = "Red"
        self.rb_insert_fixup(new_node)
