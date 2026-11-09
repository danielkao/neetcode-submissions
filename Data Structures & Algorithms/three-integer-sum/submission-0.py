class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = nums[i] * -1
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] in res:
                        k -= 1
                        j += 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        k -= 1
                        j += 1
        return res