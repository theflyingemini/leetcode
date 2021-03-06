'''
https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent
array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor
of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to
the root.

Example:
Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
Output:
[null,1,0,-1]
Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor

Constraints:
1 <= k <= n <= 5*10^4
parent[0] == -1 indicating that 0 is the root node.
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5*10^4 queries.
'''

# Approach 1
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        p = [[-1] * n for _ in range(16)]
        p[0] = parent
        for i in range(1, 16):
            for j in range(n):
                if p[i - 1][j] != -1:
                    p[i][j] = p[i - 1][p[i - 1][j]]
        self.p = p

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(15, -1, -1):
            if k >= 2 ** i:
                node = self.p[i][node]
                if node == -1:
                    return -1
                k -= 2 ** i
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# Approach 2
class TreeAncestor:

    step = 15
    def __init__(self, n: int, parent: List[int]):
        A = dict(enumerate(parent))
        self.jump = [A]

        for _ in range(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            self.jump.append(B)
            A = B

    def getKthAncestor(self, node: int, k: int) -> int:
        step = self.step
        res = node
        for i in range(step, -1, -1):
            if k >= 1 << i:
                res = self.jump[i].get(res, -1)
                if res == -1:
                    return -1
                k -= 1 << i
        return res


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
