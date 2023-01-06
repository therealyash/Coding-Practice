# Maximum IcreCream Bars
"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of
length n, where costs[i] is the price of the ith ice cream bar in coins.
The boy initially has coins to spend, and he wants to buy as many
ice cream bars as possible.

Return the maximum number of ice cream bars the boy can buy with coins coins.
Note: The boy can buy the ice cream bars in any order.
"""


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i] # Buy the ith iceream
            if coins < 0: # check if we can afford more
                return i
        #if we bought all icecreams and still got coins
        return len(costs)

costs = [1,3,2,4,1]
coins = 7
sol = Solution()
print(sol.maxIceCream(costs,coins))