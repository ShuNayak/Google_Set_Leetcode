from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        halfLen = len(nums)//2
        res = []
        for i in range(halfLen):
            j = i+halfLen
            res.append(nums[i])
            res.append(nums[j])
        return res