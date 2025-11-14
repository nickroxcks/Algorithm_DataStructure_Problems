'''
My solution:
O(n) time
O(n) memory

Scan twice algorithm.

First scan is to build a hashmap from all elements in the list
Second scan for each element num,  check if there is a num-1 and num+1 and store the current longest sequence
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums) # O(n) operation

        longest = 0
        for num in dic:  # Iterating in the set prevents iterating through duplciate numbers
            if num - 1 not in dic:
                cur_longest = 1
                while num + 1 in dic:
                    cur_longest = cur_longest + 1
                    num = num + 1
                longest = max(longest, cur_longest)
        return longest
