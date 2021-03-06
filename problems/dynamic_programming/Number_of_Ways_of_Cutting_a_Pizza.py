'''
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

Given a rectangular pizza represented as a rows x cols matrix containing the following
characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut
the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then you choose a cut
position at the cell boundary and cut the pizza into two pieces. If you cut the pizza
vertically, give the left part of the pizza to a person. If you cut the pizza horizontally,
give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least
one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces
must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:
1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
'''

# Approach 1: DP ---> O(mnk)
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        apples = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] += 1 if pizza[i][j] == 'A' else 0
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    apples[i][j] += apples[i][j + 1]
                elif j == n - 1:
                    apples[i][j] += apples[i + 1][j]
                else:
                    apples[i][j] += apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]

        f = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                f[i][j][1] = 1 if apples[i][j] > 0 else 0

        MOD = 10 ** 9 + 7
        for l in range(2, k + 1):
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if (m - i) * (n - j) < l:
                        continue
                    for r in range(i, m - 1):
                        if apples[i][j] - apples[r + 1][j] > 0:
                            f[i][j][l] += f[r + 1][j][l - 1]
                            f[i][j][l] %= MOD
                    for c in range(j, n - 1):
                        if apples[i][j] - apples[i][c + 1] > 0:
                            f[i][j][l] += f[i][c + 1][l - 1]
                            f[i][j][l] %= MOD
        return f[0][0][k] % MOD

# Approach 2: DP ---> O(mnk)
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        apples = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = 1 if pizza[i][j] == 'A' else 0
                if i < m - 1 and j < n - 1:
                    apples[i][j] += apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                elif i < m - 1:
                    apples[i][j] += apples[i + 1][j]
                elif j < n - 1:
                    apples[i][j] += apples[i][j + 1]

        MOD = 10 ** 9 + 7
        f = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for l in range(1, k + 1):
                    if l == 1:
                        f[i][j][l] += 1 if apples[i][j] > 0 else 0
                        continue

                    for r in range(i + 1, m):
                        if apples[i][j] - apples[r][j] > 0:
                            f[i][j][l] += f[r][j][l - 1]
                            f[i][j][l] %= MOD

                    for c in range(j + 1, n):
                        if apples[i][j] - apples[i][c] > 0:
                            f[i][j][l] += f[i][c][l - 1]
                            f[i][j][l] %= MOD

        return f[0][0][k]
