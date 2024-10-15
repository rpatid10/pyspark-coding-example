from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs) :
        # Initialize a default dictionary of lists
        anagrams = defaultdict(list)

        # Process each string
        for s in strs:
            # Sort the string to get the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list in the hash map
            anagrams[sorted_str].append(s)

        # Convert the hash map values to a list of lists
        return list(anagrams.values())


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(sol.groupAnagrams([""]))  # Output: [['']]
    print(sol.groupAnagrams(["a"]))  # Output: [['a']]
