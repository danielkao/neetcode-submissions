class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for key in frequencies:
            if frequencies[key] > len(nums) / 2:
                return key
            