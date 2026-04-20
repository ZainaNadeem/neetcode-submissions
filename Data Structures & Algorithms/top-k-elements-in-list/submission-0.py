import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        # Push each number into a min-heap based on frequency
        # If heap grows bigger than k, pop the smallest
        # At the end, the heap contains the k most frequent elements
        freq = Counter(nums)
        min_heap = []

        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]

        