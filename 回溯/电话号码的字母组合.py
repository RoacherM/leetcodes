"""
Author: ByronVon
Date: 2023-08-16 19:36:41
FilePath: /leetcode/回溯/电话号码的字母组合.py
Description: 
"""

maps = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def letterCombinations(digits):
    # 返回所有的字母组合
    if not digits:
        return []
    results = []  # 存储最终的组合
    current_combination = ""  # 存储当前的组合

    backtrace(digits, 0, current_combination, results)
    print("*" * 100)
    return results


def backtrace(digits, index, current_combination, results):
    # 说明已经到头
    if len(current_combination) == len(digits):
        results.append(current_combination)
        return

    current_letters = maps[digits[index]]
    print(current_letters, results)

    # 不断的组合
    for letter in current_letters:
        print(letter)
        backtrace(digits, index + 1, current_combination + letter, results)


def letterCombinations2(digits):
    result = []

    def helper(current_combination, next_digits):
        if not next_digits:
            result.append(current_combination)
        else:
            for letter in maps[next_digits[0]]:
                helper(current_combination + letter, next_digits[1:])

    if digits:
        helper("", digits)
    return result


if __name__ == "__main__":
    print(letterCombinations2(["2", "3"]))
    print(letterCombinations2(""))
    print(letterCombinations2(["2", "3", "9"]))
