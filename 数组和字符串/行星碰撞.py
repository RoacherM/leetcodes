"""
Author: ByronVon
Date: 2023-08-09 11:11:44
FilePath: /leetcode/数组和字符串/行星碰撞.py
Description: https://leetcode.cn/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
"""


def asteroidCollision(asteroids):
    # 类似消消乐的程序，需要连环消除
    # x<0: 左；x>0: 右
    queues = []
    for i in range(len(asteroids)):
        # print(i, queues, [asteroids[i]])
        if queues:
            if asteroids[i] * queues[-1] < 0:
                # [-x, y]不会相撞
                if asteroids[i] > queues[-1]:
                    queues.append(asteroids[i])
                # 考虑以下三种情况: [3, -3], [3, -5], [3, -1]
                elif asteroids[i] + queues[-1] == 0:  # 不会相撞
                    queues.pop()
                elif asteroids[i] + queues[-1] < 0:
                    # 但是需要继续检查是否还会相撞
                    queues[-1] = asteroids[i]
                    queues = asteroidCollision(queues)
            else:
                queues.append(asteroids[i])
        else:
            queues.append(asteroids[i])
    if i == len(asteroids) - 1:
        print(f"result: {queues}")
    return queues


if __name__ == "__main__":
    asteriods_0 = [5, 10, -5]
    asteriods_1 = [8, -8]
    asteriods_2 = [10, 2, -5]
    asteriods_3 = [-1, -2, 2, 1]
    asteriods_4 = [3, 3, 2, 1, -1, -2, -4]
    asteriods_5 = [1, -1, -2, 2]
    asteriods_6 = [1, -1, -2, -2]
    asteriods_7 = [-2, 2]

    asteroidCollision(asteriods_0)
    asteroidCollision(asteriods_1)
    asteroidCollision(asteriods_2)
    asteroidCollision(asteriods_3)
    asteroidCollision(asteriods_4)
    asteroidCollision(asteriods_5)
    asteroidCollision(asteriods_6)
    asteroidCollision(asteriods_7)
