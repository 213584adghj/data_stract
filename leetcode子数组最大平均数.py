class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, cur_sum = 0, k, sum(nums[:k])          # 初始化左右指针和当前滑窗中的元素和
        max_sum = cur_sum                                   # 定义当前最大值
        while right < len(nums):                            # 遍历滑窗
            cur_sum = cur_sum + nums[right] - nums[left]    # 获得当前滑窗中的元素和
            max_sum = max(max_sum, cur_sum)                 # 更新当前最大和
            left, right = left + 1, right + 1               # 左右指针右移
        return max_sum / k                                  # 返回最大均值