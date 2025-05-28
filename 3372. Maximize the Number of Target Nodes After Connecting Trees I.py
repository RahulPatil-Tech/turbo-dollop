'''
3372. Maximize the Number of Target Nodes After Connecting Trees I
Medium
There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000'''
# Solution() : DFS()
from collections import deque


class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def build_graph(edges, num_nodes):
            graph = [[] for _ in range(num_nodes)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def get_reachable_count(graph, start_node, max_dist):
            if max_dist < 0:
                return 0
            
            count = 0
            visited = [False] * len(graph)
            queue = deque([(start_node, 0)])
            visited[start_node] = True

            while queue:
                u, dist = queue.popleft()

                if dist > max_dist:
                    continue
                
                count += 1

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append((v, dist + 1))
            return count

        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = build_graph(edges1, n)
        graph2 = build_graph(edges2, m)

        max_reachable_in_tree2 = 0
        if k > 0:
            for i in range(m):
                max_reachable_in_tree2 = max(max_reachable_in_tree2, get_reachable_count(graph2, i, k - 1))
        
        answer = []
        for i in range(n):
            reachable_in_tree1 = get_reachable_count(graph1, i, k)
            answer.append(reachable_in_tree1 + max_reachable_in_tree2)
            
        return answer

print(Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))
print(Solution().maxTargetNodes( edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1))