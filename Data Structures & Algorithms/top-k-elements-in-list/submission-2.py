import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        # Push each number into a min-heap based on frequency
        # If heap grows bigger than k, pop the smallest
        # At the end, the heap contains the k most frequent elements
        count = Counter(nums)

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for count, num in heap:
            result.append(num)
        return result

        
        