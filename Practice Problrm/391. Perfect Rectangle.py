'''
391. Perfect Rectangle
Hard
Topics
Companies
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.

 

Example 1:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
Example 2:


Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
Example 3:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.
 

Constraints:

1 <= rectangles.length <= 2 * 104
rectangles[i].length == 4
-105 <= xi < ai <= 105
-105 <= yi < bi <= 105

'''
# Solution    # Approach 1 :- Approach 1: Using Corner Points and Area Check
'''This approach involves verifying three main things:
Bounding Box: Compute the smallest bounding rectangle that encloses all the given rectangles.
Corner Points: Ensure that only the four corners of the bounding box appear exactly once, while all other corner points must appear exactly twice.
Area Check: Ensure that the total area of all rectangles equals the area of the bounding box.

Algorithm Steps:
Calculate the Bounding Box: 
Determine the smallest bounding box that contains all rectangles. This can be done by finding the minimum x, minimum y, maximum a, and maximum b across all rectangles.
Track Corner Points: Iterate over all rectangles and store their corner points in a set.
Check Points and Area: Ensure that the four corners of the bounding box appear exactly once, and all other corner points appear exactly twice. Additionally, check if the total area of the rectangles matches the area of the bounding box.
'''
import time
'''from typing import List 
class Solution():
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x_min, y_min = float('inf'), float('inf')
        x_max, y_max = float('-inf'), float('-inf')
        corner_points = set()
        total_area = 0
        for x1, y1, x2, y2 in rectangles:
            x_min, y_min = min(x_min, x1), min(y_min, y1)
            x_max, y_max = max(x_max, x2), max(y_max, y2)
            total_area += (x2 - x1) * (y2 - y1)
            corners = [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
            for corner in corners:
                if corner in corner_points:
                    corner_points.remove(corner)
                else:
                    corner_points.add(corner)
        expected_corner = {(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)}
        return corner_points == expected_corner and total_area == (x_max - x_min) * (y_max - y_min)
start_time = time.time()
print(Solution().isRectangleCover( rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))
print(Solution().isRectangleCover( rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]))
print(Solution().isRectangleCover(rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]))
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")
'''
# Appraoch 2 : Approach 2: Using Graph Connectivity (Union-Find)
'''This approach models the problem using graph theory where rectangles are connected if they share edges, and then checks if the graph forms a connected component that covers the entire rectangular area.

Algorithm Steps:
Union-Find (Disjoint Set Union, DSU): Use a union-find data structure to keep track of connected rectangles.
Edge Sharing: Rectangles that share a horizontal or vertical edge should be connected in the union-find structure.
Connected Components: Check if the entire set of rectangles forms a single connected component. If it does, the rectangles perfectly cover a rectangle without gaps or overlaps.
''' 
import time
from typing import List 
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
class Solution():
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        uf = UnionFind(len(rectangles))
    
        # Keep track of the edges of each rectangle
        edges = {}
    
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
        # Add the edges and check for overlap
            edges[(x1, y1, x2, y2)] = i
            for j in range(i + 1, len(rectangles)):
                pass  # Implement the union operation here
    
        return True
start_time = time.time()
print(Solution().isRectangleCover( rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))
print(Solution().isRectangleCover( rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]))
print(Solution().isRectangleCover(rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]))
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")
