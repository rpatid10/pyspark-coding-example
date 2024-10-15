import math
from typing import List

class Solution:
    def findFactors(self, n: int) -> List[int]:
        factors = set()
        # Iterate from 1 to the square root of n
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:  # i is a factor
                factors.add(i)
                factors.add(n // i)  # n // i is also a factor
        return sorted(factors)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findFactors(28))  # Output: [1, 2, 4, 7, 14, 28]
    print(sol.findFactors(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]


