class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        # Initial conditions
        hold[0] = -prices[0]
        sell[0] = 0
        cooldown[0] = 0

        for i in range(1, n):
            # Update states based on transitions
            hold[i] = max(hold[i - 1], cooldown[i - 1] - prices[i])
            sell[i] = hold[i - 1] + prices[i]
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])

        # Maximum profit will be in the sell state of the last day
        return sell[-1]


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 2, 3, 0, 2]))  # Output: 3
    print(sol.maxProfit([1]))  # Output: 0
    print(sol.maxProfit([1,1,1,1,-2]))
