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
                return root
            else:
                root = root.right
        return None

    @staticmethod
    def search_min(root):
        while not (root is None):
            if root.left is None:
                return root
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

    def transplant(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        elif old_node.parent.left is old_node:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        if not (new_node is None):
            new_node.parent = old_node.parent

    def delete_node(self, del_node):
        if del_node.left is None:
            self.transplant(del_node, del_node.right)
        elif del_node.right is None:
            self.transplant(del_node, del_node.left)
        else:
            min_node = BinaryTree.search_min(del_node.right)
            if not (min_node.parent is del_node):
                self.transplant(min_node, min_node.right)
                min_node.right = del_node.right
                min_node.right.parent = min_node
            self.transplant(del_node, min_node)
            min_node.left = del_node.left
            min_node.left.parent = min_node
