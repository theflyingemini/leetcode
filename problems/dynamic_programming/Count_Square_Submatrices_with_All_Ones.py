'''
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''

# Approach 1: DP --- O(n ^ 2)
# Similar problem: https://leetcode.com/problems/maximal-square/

class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        f = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                f[i][j] = 1 if A[i][j] == 1 else 0
                if i > 0 and j > 0 and A[i][j] == 1:
                    f[i][j] += min(f[i - 1][j], f[i - 1][j - 1], f[i][j - 1])
                res += f[i][j]
        return res
