from unittest import TestCase
from Sorts import QuickSort


class TestQuickSort(TestCase):
    def test_quick_sort(self):
        test_list = [2, 1, 3, 2, 5, 0]
        test_list = QuickSort.quick_sort(test_list)
        sorted_list = [0, 1, 2, 2, 3, 5]
        self.assertListEqual(test_list, sorted_list)
