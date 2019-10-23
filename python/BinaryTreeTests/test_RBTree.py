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
        tree.in_order_traversal_rec(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)
