class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(nums==[0]):
            return 1
        d=len(nums)
        return int(d*(d+1)/2-sum(nums))