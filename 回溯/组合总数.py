"""
Author: ByronVon
Date: 2023-08-16 20:45:26
FilePath: /leetcode/回溯/组合总数.py
Description: 
"""


def combinationSum3(k, n):
    # 从数组k中找出所有和为n的组合数
    # 只有1-9数字；每个数字最多使用一次
    result = []

    def helper(current_combination, next_digit):
        # 只添加符合条件的结果
        if len(current_combination) == k:
            if sum(current_combination) == n:
                result.append(list(current_combination))
            return  # 停止遍历

        for d in range(next_digit, 10):
            current_combination.append(d)
            helper(current_combination, d + 1)
            current_combination.pop()  # 回溯，删除刚才的数字，检查下个

    helper([], 1)
    return result


if __name__ == "__main__":
    print(combinationSum3(3, 7))
