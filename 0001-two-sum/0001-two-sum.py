class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in nMap:
                return [nMap[complement], i]
            nMap[nums[i]] = i
        return False