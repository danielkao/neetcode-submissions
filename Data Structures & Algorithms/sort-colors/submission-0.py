class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 0 = red
        # 1 = white
        # 2 = blue

        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        k = 0
        for i in range(len(count)):
           for j in range(count[i]):
            nums[k] = i
            k += 1
