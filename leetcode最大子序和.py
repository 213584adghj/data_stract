class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        for i in range(len(dp)):
            if(i==0):
                dp[i]=nums[i]
            else:
                if(dp[i-1]+nums[i]>nums[i]):
                    dp[i]=dp[i-1]+nums[i]
                else:
                    dp[i]=nums[i]
        return(max(dp))