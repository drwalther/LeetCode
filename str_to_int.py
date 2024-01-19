# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def my_atoi(self, s: str) -> int:
        i = 0
        sign = 1
        result = 0
        length = len(s)
        # Если попадаем на пробел
        while i < length and s[i] == " ":
            i += 1

        if i < length and s[i] == "-":
            sign *= -1
            i += 1
        elif i < length and s[i] == "+":
            i += 1

        while i < length and s[i].isdigit():
            # отработало быстрее чем обращение к словарю типа ""2": 2"
            result = result * 10 + int(s[i])
            i += 1

        result = result * sign
        # работает быстрее чем return min(max(result, -2 ** 31), 2 ** 31 - 1)
        if result < -(2**31):
            return -(2**31)
        elif result > 2**31 - 1:
            return 2**31 - 1
        return result
