from unittest import TestCase
from Sorts import CountingSort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        test_list = [2, 1, 3, 2, 5, 0]
        result_list = CountingSort.counting_sort(test_list, max(test_list) + 1)
        sorted_list = [0, 1, 2, 2, 3, 5]
        self.assertListEqual(result_list, sorted_list)
