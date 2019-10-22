class Node:

    def __init__(self, parent, left, right, key):
        self.parent = parent
        self.right = right
        self.left = left
        self.key = key


class BinaryTree:

    def __init__(self, root):
        self.root = root

    @staticmethod
    def insert(node, root):
        if node.key >= root.key:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                BinaryTree.insert(node, root.right)
        else:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                BinaryTree.insert(node, root.left)

    @staticmethod
    def in_order_traversal_rec(root, keys):
        if root is None:
            return
        BinaryTree.in_order_traversal_rec(root.left, keys)
        keys.append(root.key)
        BinaryTree.in_order_traversal_rec(root.right, keys)

    @staticmethod
    def search_max(root):
        while not (root is None):
            if root.right is None:
                return root.key
            else:
                root = root.right
        return None

    @staticmethod
    def search_min(root):
        while not (root is None):
            if root.left is None:
                return root.key
            else:
                root = root.left
        return None

    @staticmethod
    def search(root, key):
        while not (root is None):
            if root.key == key:
                return True
            if key > root.key:
                root = root.right
            else:
                root = root.left
        return False
