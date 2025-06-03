'''
3373. Maximize the Number of Target Nodes After Connecting Trees II
Hard
Topics
premium lock icon
Companies
Hint
There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

Output: [8,7,7,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]

Output: [3,6,6,6,6]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.'''
# Tree
# Depth-First Search
# Breadth-First Search
# Solution () 
from collections import deque
from typing import List

class Solution():
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # Helper function to build adjacency list for a tree
        def build_graph(n, edges):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        # Helper function to compute depths of all nodes using BFS
        def compute_depth_parity(graph, n):
            depth = [-1] * n
            if n == 0: # Handle empty graph case, though constraints say n, m >= 2
                return []
            
            queue = deque([0])
            depth[0] = 0
            
            # BFS to calculate depths
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if depth[neighbor] == -1: # If not visited
                        depth[neighbor] = depth[node] + 1
                        queue.append(neighbor)
            return depth

        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = build_graph(n, edges1)
        graph2 = build_graph(m, edges2)

        depth1 = compute_depth_parity(graph1, n)
        depth2 = compute_depth_parity(graph2, m)

        # Count nodes with even and odd depths for tree1
        even1 = 0
        odd1 = 0
        for d in depth1:
            if d % 2 == 0:
                even1 += 1
            else:
                odd1 += 1
        
        # Count nodes with even and odd depths for tree2
        even2 = 0
        odd2 = 0
        for d in depth2:
            if d % 2 == 0:
                even2 += 1
            else:
                odd2 += 1
        
        # Calculate the maximum possible contribution from tree2
        # We can always choose connection points (c1, c2) such that
        # the number of target nodes from tree2 is max(even2, odd2)
        max_from_tree2 = max(even2, odd2)

        answer = []
        for i in range(n):
            if depth1[i] % 2 == 0: # If node i has even depth in tree1
                # Target nodes in tree1 are those with even depth
                # Target nodes in tree2 are those with parity chosen to maximize (max_from_tree2)
                answer.append(even1 + max_from_tree2)
            else: # If node i has odd depth in tree1
                # Target nodes in tree1 are those with odd depth
                # Target nodes in tree2 are those with parity chosen to maximize (max_from_tree2)
                answer.append(odd1 + max_from_tree2)
        
        return answer
print(Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))
print(Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]))