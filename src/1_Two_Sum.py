class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        for i, num in enumerate(nums):
            if target - num in summ:
                return [summ[target - num], i]
            summ[num] = i
