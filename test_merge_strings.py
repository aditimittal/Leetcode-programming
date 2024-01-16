import pytest
from merge_strings import Solution
import unittest

class MyTestCase(unittest.TestCase):
    def test_mergeAlternately(self)->None:
        obj = Solution()
        result = obj.mergeAlternately("abc", "pqr")
        self.assertEqual("apbqcr", result)
    def test_mergeAlternately_unequal_len(self)->None:
        obj = Solution()
        result = obj.mergeAlternately("abcd", "pqr")
        self.assertEqual("apbqcrd", result)
        result = obj.mergeAlternately("abc", "pqrs")
        self.assertEqual("apbqcrs", result)
