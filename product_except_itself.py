#238. Product of Array Except Self
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        suffix_product = 1
        res = [0]*n
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= suffix_product
            suffix_product *= nums[i]
        print(res)
        return res
