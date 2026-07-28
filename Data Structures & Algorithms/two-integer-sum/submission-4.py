class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        valMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in valMap:
                valMap[nums[i]] = i
            else:
                return [valMap[complement], i]
