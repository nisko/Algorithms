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
        tree.in_order_traversal(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)

    def test_in_order_traversal(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)

    def test_pre_order_traversal(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        e = BinaryTree.Node(None, None, None, 0)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        tree.insert(e, tree.root)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [5, 1, 0, 2, 7]
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
        max_node = tree.search_max(tree.root)
        self.assertEqual(max_node.key, 7)

    def test_search_min(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        min_node = tree.search_min(tree.root)
        self.assertEqual(min_node.key, 1)

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

    def test_delete(self):
        a = BinaryTree.Node(None, None, None, 5)
        tree = BinaryTree.BinaryTree(a)
        b = BinaryTree.Node(None, None, None, 1)
        c = BinaryTree.Node(None, None, None, 7)
        d = BinaryTree.Node(None, None, None, 2)
        tree.insert(b, tree.root)
        tree.insert(c, tree.root)
        tree.insert(d, tree.root)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [1, 2, 5, 7]
        self.assertListEqual(true_keys, keys)
        tree.delete_node(b)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [2, 5, 7]
        self.assertListEqual(true_keys, keys)
        tree.delete_node(a)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [2, 7]
        self.assertListEqual(true_keys, keys)
        tree.delete_node(c)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = [2]
        self.assertListEqual(true_keys, keys)
        tree.delete_node(d)
        keys = []
        tree.in_order_traversal(tree.root, keys)
        true_keys = []
        self.assertListEqual(true_keys, keys)
