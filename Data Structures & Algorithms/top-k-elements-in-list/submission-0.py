class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        toReturn = [item for item, count in counts.most_common(k)]

        return toReturn