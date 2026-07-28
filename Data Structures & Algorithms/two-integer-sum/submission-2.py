class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        valMap = {value: index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in valMap and valMap[complement] != i:
                return [i, valMap[complement]]
