class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)

        toReturn = []

        for i in range(len(nums) + 1):
            if i not in set_nums:
                toReturn.append(i)
    
        if toReturn:
            return toReturn[0]
        else:
            return -1