# Minimum Rounds to Complete - Medium
"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the
difficulty level of a task. In each round, you can complete either 2 or 3
tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is
not possible to complete all the tasks.
"""
from collections import Counter
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:

        tasks = Counter(tasks)

        if 1 in tasks.values(): return -1

        ans = 0
        for n in tasks.values():
            ans += n // 3 + bool(n % 3)

        return ans

arr = [2,2,3,3,2,4,4,4,4,4]
obj = Solution()
print(obj.minimumRounds(arr))

