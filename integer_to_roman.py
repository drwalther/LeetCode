# Нужно преобразовать целое цисло к римскому числу


class Solution:
    def int_to_roman(self, num: int) -> str:
        result = ""
        roman_nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        for i in roman_nums:
            while roman_nums[i] <= num:
                num -= roman_nums[i]
                result += i

        return result


# Немного измененный вариант
# class Solution:
#     def int_to_roman(self, num: int) -> str:
#         result = ""
#         roman_nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#
#         for key, value in roman_nums.items():
#             while value <= num:
#                 num -= value
#                 result += key
#
#         return result


if __name__ == "__main__":
    a = Solution()
    b = 58
    c = 3568
    print(a.int_to_roman(b))
    print(a.int_to_roman(c))
