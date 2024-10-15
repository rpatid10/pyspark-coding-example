from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Dictionaries to store frequency, first and last index
        freq = defaultdict(int)
        first_pos = {}
        last_pos = {}

        # Traverse the array to fill freq, first_pos and last_pos
        for i, num in enumerate(nums):
            if num not in first_pos:
                first_pos[num] = i
            last_pos[num] = i
            freq[num] += 1

        # Determine the degree of the array
        degree = max(freq.values())

        # Find the minimum length of subarray with the same degree
        min_length = float('inf')
        for num, count in freq.items():
            if count == degree:
                min_length = min(min_length, last_pos[num] - first_pos[num] + 1)

        return min_length


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findShortestSubArray([1, 2, 2, 3, 1]))  # Output: 2
    print(sol.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))  # Output: 6
