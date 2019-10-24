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
