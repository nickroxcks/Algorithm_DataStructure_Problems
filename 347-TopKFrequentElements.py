import heapq
from collections import Counter
from typing import List

'''
n = number of elements inside nums
k = k

Time complexity:
    Building the frequency counter takes O(n) time since dictionary inserts are constant time
    Building a heap, insert = O(logn) time, thus building heap for n elements takes O(nlogn) time
    Building output: Accessing priority elements takes O(1) time, so accessing top k elements
    takes O(k) time
    
    Overall: O(n + nlogn + k) time
    
Memory Complexity:
    Frequency counter worst case can take O(n) space where each element in nums is unique
    Heap storing the full heap 
'''
class MySolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = []
        freq = {}
        heap = []

        # Build the frequency counter
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        # Build a Min Heap with negative priority que
        for value, count in freq.items():
            heapq.heappush(heap, (-count, value))

        # Output the solution
        for i in range(k):
            count, value = heapq.heappop(heap)
            sol.append(value)

        return sol

'''

Efficient Leetcode solution fully leveraging python heapq built in methods

Time complexity:
O(n + nlogk) time

Memory Complexity:
O(n + k) memory
'''
class EfficientSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)