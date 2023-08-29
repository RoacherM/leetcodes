"""
Author: ByronVon
Date: 2023-08-15 15:27:07
FilePath: /leetcode/数据结构/投票.py
Description: 
"""

from collections import deque

# def predictPartyVictory(senate):
#     # 因为每个人只能禁止下一位的票，因此有
#     # R->R;RD->R;RR->R
#     # D->D;DR->D;DD->D
#     ## 写的有问题，不是只禁止下一位，而是禁止下一个不同阵营的议员
#     ## 如'RRDD'->'R'
#     status = {"R": "Radiant", "RD": "Radiant", "RR": "Radiant", "D": "Dire", "DR": "Dire", "DD": "Dire"}
#     ans = ""
#     temp = ""
#     for s in senate:
#         temp += s
#         ans = status[temp[-2:]]
#     return ans


def predictPartyVictory(senate):
    # 可以考虑：维护两个队列，分别为R和D
    # 每次投票开始时，分别从R、D的头部取出一个议员
    # index较小的议员拥有投票权，index大的议员只能参与下一轮投票
    # 如果某个阵营的队列为空，则该阵营输
    R = deque()
    D = deque()
    for i, s in enumerate(senate):
        if s == "R":
            R.append((i))
        else:
            D.append((i))
    while R and D:
        # 开始投票
        r = R.popleft()
        d = D.popleft()
        if r < d:
            R.append(r + len(senate))
        else:
            D.append(d + len(senate))
    print(f"R: {R}, D: {D}")
    return "R" if R else "D"


if __name__ == "__main__":
    print(predictPartyVictory("RD"))
    print(predictPartyVictory("RDD"))
    print(predictPartyVictory("RDRRDD"))
