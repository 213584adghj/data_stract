class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, cur_sum = 0, k, sum(nums[:k])          # ��ʼ������ָ��͵�ǰ�����е�Ԫ�غ�
        max_sum = cur_sum                                   # ���嵱ǰ���ֵ
        while right < len(nums):                            # ��������
            cur_sum = cur_sum + nums[right] - nums[left]    # ��õ�ǰ�����е�Ԫ�غ�
            max_sum = max(max_sum, cur_sum)                 # ���µ�ǰ����
            left, right = left + 1, right + 1               # ����ָ������
        return max_sum / k                                  # ��������ֵ