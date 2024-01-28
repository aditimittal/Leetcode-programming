import pytest
from move_zeroes import Solution
import unittest

def test_moveZeroes():
    nums = [0,1,0,3,12]
    obj= Solution()
    move_zeroes=obj.moveZeroes(nums)
    assert([1,3,12,0,0], move_zeroes)