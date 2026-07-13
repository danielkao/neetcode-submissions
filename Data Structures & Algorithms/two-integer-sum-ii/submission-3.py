class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []

        def bs(complement, s, e):
            if s > e:
                return False
                
            mid = (s + e) // 2
                
            if numbers[mid] == complement:
                solution.append(mid + 1)
                return True
            elif numbers[mid] > complement:
                return bs(complement, s, mid - 1)
            else:
                return bs(complement, mid + 1, e)
        
        for i in range(len(numbers)):
            complement = target - numbers[i]

            if bs(complement, 0, len(numbers) - 1):
                solution.append(i + 1)
                break
            
        solution.sort()
        return solution
                # For every element in numbers
                # perform a binary search to find its complement