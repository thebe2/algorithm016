# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9162 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            try:
                # 注意重复的数字，从idx+1开始查找
                next_idx = nums.index(target-num, idx+1)
                return [idx, next_idx]
            except ValueError as e:
                pass
        return []

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    testcases = [
        ([3,3], 6),
        ([2, 7, 11, 15], 9)
    ]
    s1 = Solution()
    for testcase in testcases:
        print(testcase, s1.twoSum(testcase[0], testcase[1]))

