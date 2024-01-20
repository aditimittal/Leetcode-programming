import pytest
from product_except_itself import Solution
import unittest

class MyTestCase(unittest.TestCase):
    def test_productExceptSelf(self)->None:
        obj = Solution()
        result = obj.productExceptSelf([1,2,3,4])
        self.assertEqual([24,12,8,6], result)
    
    