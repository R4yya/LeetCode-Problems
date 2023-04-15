class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0, nums.count(val)):
            nums.remove(val)

        return len(nums)
