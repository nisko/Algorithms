class Node:

    def __init__(self, parent, left, right, key: float):
        self.parent = parent
        self.right = right
        self.left = left
        self.key = key


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, node: Node, root: Node) -> None:
        if root is None:
            self.root = node
            return
        if node.key >= root.key:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self.insert(node, root.right)
        else:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self.insert(node, root.left)

    @staticmethod
    def in_order_traversal(root: Node, keys: list) -> None:
        if root is None:
            return
        BinaryTree.in_order_traversal(root.left, keys)
        keys.append(root.key)
        BinaryTree.in_order_traversal(root.right, keys)

    @staticmethod
    def pre_order_traversal(root: Node, keys: list) -> None:
        if root is None:
            return
        keys.append(root.key)
        BinaryTree.pre_order_traversal(root.left, keys)
        BinaryTree.pre_order_traversal(root.right, keys)

    @staticmethod
    def search_max(root: Node) -> object:
        while root is not None:
            if root.right is None:
                return root
            else:
                root = root.right
        return None

    @staticmethod
    def search_min(root: Node) -> object:
        while root is not None:
            if root.left is None:
                return root
            else:
                root = root.left
        return None

    @staticmethod
    def search(root: Node, key: float) -> bool:
        while root is not None:
            if root.key == key:
                return True
            if key > root.key:
                root = root.right
            else:
                root = root.left
        return False

    def transplant(self, old_node: Node, new_node: Node) -> None:
        if old_node.parent is None:
            self.root = new_node
        elif old_node.parent.left is old_node:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        if new_node is not None:
            new_node.parent = old_node.parent

    def delete_node(self, del_node: Node) -> None:
        if del_node.left is None:
            self.transplant(del_node, del_node.right)
        elif del_node.right is None:
            self.transplant(del_node, del_node.left)
        else:
            min_node = BinaryTree.search_min(del_node.right)
            if min_node.parent is not del_node:
                self.transplant(min_node, min_node.right)
                min_node.right = del_node.right
                min_node.right.parent = min_node
            self.transplant(del_node, min_node)
            min_node.left = del_node.left
            min_node.left.parent = min_node
