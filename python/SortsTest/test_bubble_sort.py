from unittest import TestCase
from Sorts import BubbleSort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        test_list = [2, 1, 3, 2, 5, 0]
        BubbleSort.bubble_sort(test_list)
        sorted_list = [0, 1, 2, 2, 3, 5]
        self.assertListEqual(test_list, sorted_list)
