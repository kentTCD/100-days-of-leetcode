class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common()
        return [counts[i][0] for i in range(k)]