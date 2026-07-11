class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(s, e):
            if s > e:
                return -1

            mid = (s + e) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs(s, mid - 1)
            else:
                return bs(mid + 1, e)
            
        return bs(0, len(nums) - 1)