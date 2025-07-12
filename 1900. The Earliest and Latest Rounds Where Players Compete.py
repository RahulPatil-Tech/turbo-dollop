'''
1900. The Earliest and Latest Rounds Where Players Compete
Hard
Topics
premium lock icon
Companies
Hint
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

 

Example 1:

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.
 

Constraints:

2 <= n <= 28
1 <= firstPlayer < secondPlayer <= n
'''
# Solution 
import functools
from itertools import product

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        firstPlayer -= 1
        secondPlayer -= 1

        @functools.lru_cache(None)
        def dp(n, i, j):
            if i + j == n - 1:
                return (1, 1)
            
            min_r, max_r = float('inf'), float('-inf')
            
            for positions in self.gen_next_positions(n, i, j):
                ni, nj = positions
                e, l = dp((n + 1) // 2, ni, nj)
                min_r = min(min_r, e + 1)
                max_r = max(max_r, l + 1)

            return (min_r, max_r)

        return dp(n, min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer))

    def gen_next_positions(self, n, i, j):
        pairs = []
        mid = -1
        for a in range(n // 2):
            b = n - 1 - a
            pairs.append((a, b))

        if n % 2 == 1:
            mid = n // 2

        def next_idx(pos, winners):
            return sorted(winners).index(pos)

        result = set()

        for outcome in product([0, 1], repeat=len(pairs)):
            winners = set()
            for k, (a, b) in enumerate(pairs):
                if (a == i or a == j) or (b == i or b == j):
                    continue

                winners.add(pairs[k][outcome[k]])

            if mid != -1:
                winners.add(mid)
            winners.add(i)
            winners.add(j)

            ni = next_idx(i, winners)
            nj = next_idx(j, winners)
            if ni < nj:
                result.add((ni, nj))
            else:
                result.add((nj, ni))

        return result


print(Solution().earliestAndLatest(11, 2, 4))
print(Solution().earliestAndLatest(5, 1, 5))