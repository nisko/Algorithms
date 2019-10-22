from unittest import TestCase
from BinaryTree import BinaryTree


class TestBinaryTree(TestCase):

    def test_insert(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        keys = []
        tree.in_order_traversal_rec(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)

    def test_search_max(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        max = tree.search_max(tree.root)
        self.assertEqual(max, 7)

    def test_search_min(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        min = tree.search_min(tree.root)
        self.assertEqual(min, 1)

    def test_search(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        self.assertFalse(tree.search(tree.root, 8))
        self.assertTrue(tree.search(tree.root, 2))
