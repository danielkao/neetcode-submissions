class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []
        i = 0
        j = len(numbers) - 1
        while j > i:
            sum = numbers[i] + numbers[j]
            if target > sum:
                i += 1
                continue
            elif sum > target:
                j -= 1
                continue
            else:
                solution.append(i + 1)
                solution.append(j + 1)
                break
        return solution