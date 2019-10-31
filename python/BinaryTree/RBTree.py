from BinaryTree import BinaryTree


class RBNode(BinaryTree.Node):
    def __init__(self, parent, left, right, key: float, color: str):
        super().__init__(parent, left, right, key)
        self.color = color


class RBTree(BinaryTree.BinaryTree):
    @staticmethod
    def in_order_traversal(root: RBNode, keys: list) -> None:
        if root is None:
            return
        RBTree.in_order_traversal(root.left, keys)
        keys.append(root.key)
        RBTree.in_order_traversal(root.right, keys)

    @staticmethod
    def pre_order_traversal(root: RBNode, keys: list) -> None:
        if root is None:
            return
        keys.append(root.key)
        RBTree.pre_order_traversal(root.left, keys)
        RBTree.pre_order_traversal(root.right, keys)

    def __init__(self):
        self.root = None

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
        while new_node.parent and new_node.parent.color == "Red":
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
        self.root.color = "Black"

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

    def rb_transplant(self, node_u: RBNode, node_v: RBNode):
        if node_u.parent is None:
            self.root = node_v
        elif node_u is node_u.parent.left:
            node_u.parent.left = node_v
        else:
            node_u.parent.right = node_v
        node_v.parent = node_u.parent

    def rb_delete_fixup(self, node_x: RBNode):
        while node_x is not self.root and node_x.color == "Black":
            if node_x is node_x.parent.left:
                node_w = node_x.parent.right
                if node_w.color == "Red":
                    node_w.color = "Black"
                    node_x.parent.color = "Red"
                    self.left_rotate(node_x.parent)
                    node_w = node_x.parent.right
                if node_w.left.color == "Black" and node_w.right.color == "Black":
                    node_w.color = "Red"
                    node_x = node_x.parent
                elif node_w.right.color == "Black":
                    node_w.left.color = "Black"
                    node_w.color = "Red"
                    self.right_rotate(node_w)
                    node_w = node_x.parent.right
                node_w.color = node_x.parent.color
                node_x.parent.color = node_x.parent.color
                node_x.parent.color = "Black"
                node_w.right.color = "Black"
                self.left_rotate(node_x.parent)
                node_x = self.root
            else:
                node_w = node_x.parent.right
                if node_w.color == "Red":
                    node_w.color = "Black"
                    node_x.parent.color = "Red"
                    self.right_rotate(node_x.parent)
                    node_w = node_x.parent.right
                if node_w.left.color == "Black" and node_w.right.color == "Black":
                    node_w.color = "Red"
                    node_x = node_x.parent
                elif node_w.right.color == "Black":
                    node_w.left.color = "Black"
                    node_w.color = "Red"
                    self.left_rotate(node_w)
                    node_w = node_x.parent.right
                node_w.color = node_x.parent.color
                node_x.parent.color = node_x.parent.color
                node_x.parent.color = "Black"
                node_w.right.color = "Black"
                self.right_rotate(node_x.parent)
                node_x = self.root
        node_x.color = "Black"

    def rb_delete(self, delete_node: RBNode):
        node_y = delete_node
        y_original_color = node_y.color
        if delete_node.left is None:
            node_x = delete_node.right
            self.rb_transplant(delete_node, delete_node.right)
        elif delete_node.right is None:
            node_x = delete_node.right
            self.rb_transplant(delete_node, delete_node.left)
        else:
            node_y = BinaryTree.search_min(delete_node.right)
            y_original_color = node_y.color
            node_x = node_y.right
            if node_y.parent is delete_node:
                node_x.parent = node_y
            else:
                self.rb_transplant(node_y, node_y.right)
                node_y.right = delete_node.right
                node_y.right.parent = node_y
            self.rb_transplant(delete_node, node_y)
            node_y.left = delete_node.left
            node_y.left.parent = node_y
            node_y.color = delete_node.color
        if y_original_color == "Black":
            self.rb_delete_fixup(node_x)

