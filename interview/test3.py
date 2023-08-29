"""
Author: ByronVon
Date: 2023-08-11 10:22:04
FilePath: /leetcode/面试/test3.py
Description: 
"""
# 跳格子游戏

# Robot Navigation

# A robot needs move from top left corner to bottom right corner in a 2D map. In this map, there are 0s and 1s. 0 means the robot can pass and 1 means the wall.

# Please write a function that returns True or False, given at most k number of walls to demolish.

# Example 1:

# Input: grid = [[0, 1 0], [0, 1, 0]], k = 0
# Output: False
# Explanation: The robot cannot demolish any wall due to k == 0, the robot cannot reach the bottom right corner.

# Example 2:

# Input: grid = [[0, 1 0], [0, 1, 0]], k = 1
# Output: True
# Explanation: The robot can demolish the wall (0, 1) or (1, 1) to reach the destination.

# The function interface should be:


def robot_navigation(grid, k):
    m = len(grid)
    n = len(grid[0])

    queue = [(0, 0, 0)]
    visited = set()

    while queue:
        i, j, walls = queue.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == m - 1 and j == n - 1:
            return True

        dirs = [(0, 1), (1, 0)]
        for di, dj in dirs:
            new_i = i + di
            new_j = j + dj
            if 0 <= new_i < m and 0 <= new_j < n:
                if grid[new_i][new_j] == 0:
                    queue.append((new_i, new_j, walls))
                elif walls < k:
                    queue.append((new_i, new_j, walls + 1))

    return False


if __name__ == "__main__":
    print(robot_navigation([[0, 1, 0, 0], [0, 1, 0, 1]], k=1))
