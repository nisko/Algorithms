from unittest import TestCase
from BinaryTree import RBTree


class TestBinaryTree(TestCase):

    def test_insert(self):
        a = RBTree.RBNode(None, None, None, 5, None)
        tree = RBTree.RBTree(a)
        b = RBTree.RBNode(None, None, None, 1, None)
        c = RBTree.RBNode(None, None, None, 7, None)
        d = RBTree.RBNode(None, None, None, 2, None)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)

    def test_right_rotate(self):
        a = RBTree.RBNode(None, None, None, 3, None)
        tree = RBTree.RBTree(a)
        b = RBTree.RBNode(None, None, None, 1, None)
        c = RBTree.RBNode(None, None, None, 5, None)
        d = RBTree.RBNode(None, None, None, 0, None)
        e = RBTree.RBNode(None, None, None, 2, None)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        tree.insert(e, tree.root)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [3, 1, 0, 2, 5]
        self.assertListEqual(true_keys, keys)
        tree.right_rotate(a)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [1, 0, 3, 2, 5]
        self.assertListEqual(true_keys, keys)

    def test_left_rotate(self):
        a = RBTree.RBNode(None, None, None, 1, None)
        tree = RBTree.RBTree(a)
        b = RBTree.RBNode(None, None, None, 0, None)
        c = RBTree.RBNode(None, None, None, 3, None)
        d = RBTree.RBNode(None, None, None, 2, None)
        e = RBTree.RBNode(None, None, None, 5, None)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        tree.insert(e, tree.root)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [1, 0, 3, 2, 5]
        self.assertListEqual(true_keys, keys)
        tree.left_rotate(a)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [3, 1, 0, 2, 5]
        self.assertListEqual(true_keys, keys)

