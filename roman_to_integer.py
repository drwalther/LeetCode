# Нужно преобразовать число из римских цифр в число из арабских цифр


class Solution:
    def roman_to_int(self, roman_integer: str) -> int:
        result = 0
        nums_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(roman_integer)):
            if (
                i + 1 < len(roman_integer)
                and nums_dict[roman_integer[i]] < nums_dict[roman_integer[i + 1]]
            ):
                result -= nums_dict[roman_integer[i]]
            else:
                result += nums_dict[roman_integer[i]]

        return result


if __name__ == "__main__":
    b = "LVIII"
    a = Solution()
    print(a.roman_to_int(b))
