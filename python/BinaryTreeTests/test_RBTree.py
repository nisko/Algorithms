from unittest import TestCase
from BinaryTree import RBTree


class TestBinaryTree(TestCase):

    def test_rb_insert(self):
        tree = RBTree.RBTree()
        tree.rb_insert(RBTree.RBNode(None, None, None, 11, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 2, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 14, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 1, None))
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [11, 2, 1, 14]
        self.assertListEqual(true_keys, keys)

        tree.rb_insert(RBTree.RBNode(None, None, None, 7, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 15, None))
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [11, 2, 1, 7, 14, 15]
        self.assertListEqual(true_keys, keys)

        tree.rb_insert(RBTree.RBNode(None, None, None, 5, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 8, None))
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [11, 2, 1, 7, 5, 8, 14, 15]
        self.assertListEqual(true_keys, keys)

        tree.rb_insert(RBTree.RBNode(None, None, None, 4, None))
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [7, 2, 1, 5, 4, 11, 8, 14, 15]
        self.assertListEqual(true_keys, keys)

    def test_rb_delete(self):
        tree = RBTree.RBTree()
        tree.rb_insert(RBTree.RBNode(None, None, None, 11, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 2, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 14, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 1, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 7, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 15, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 5, None))
        tree.rb_insert(RBTree.RBNode(None, None, None, 8, None))
        z = RBTree.RBNode(None, None, None, 4, None)
        tree.rb_insert(z)
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [7, 2, 1, 5, 4, 11, 8, 14, 15]
        self.assertListEqual(true_keys, keys)

        tree.delete_node(z)
        keys = []
        RBTree.RBTree.pre_order_traversal(tree.root, keys)
        true_keys = [7, 2, 1, 5, 11, 8, 14, 15]
        self.assertListEqual(true_keys, keys)


    def test_right_rotate(self):
        tree = RBTree.RBTree()
        a = RBTree.RBNode(None, None, None, 3, None)
        b = RBTree.RBNode(None, None, None, 1, None)
        c = RBTree.RBNode(None, None, None, 5, None)
        d = RBTree.RBNode(None, None, None, 0, None)
        e = RBTree.RBNode(None, None, None, 2, None)
        tree.rb_insert(a)
        tree.rb_insert(b)
        tree.rb_insert(c)
        tree.rb_insert(d)
        tree.rb_insert(e)
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
        tree = RBTree.RBTree()
        a = RBTree.RBNode(None, None, None, 1, None)
        b = RBTree.RBNode(None, None, None, 0, None)
        c = RBTree.RBNode(None, None, None, 3, None)
        d = RBTree.RBNode(None, None, None, 2, None)
        e = RBTree.RBNode(None, None, None, 5, None)
        tree.rb_insert(a)
        tree.rb_insert(b)
        tree.rb_insert(c)
        tree.rb_insert(d)
        tree.rb_insert(e)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [1, 0, 3, 2, 5]
        self.assertListEqual(true_keys, keys)
        tree.left_rotate(a)
        keys = []
        tree.pre_order_traversal(tree.root, keys)
        true_keys = [3, 1, 0, 2, 5]
        self.assertListEqual(true_keys, keys)
