# Проверить, является ли число палиндромом


class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        new_int = 0

        while x > new_int:
            new_int = new_int * 10 + x % 10
            x = x // 10

        return x == new_int or x == new_int // 10


# Первое решение, неоптимальное
# class Solution:
#     def is_palindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]

# Потом решил так, но тоже неоптимально
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num_to_str = str(x)
#         for i in range(len(num_to_str)):
#             if num_to_str[i] != num_to_str[-1 - i]:
#                 return False
#
#         return True

if __name__ == "__main__":
    a = Solution()
    b = 0
    c = 121
    d = 12321
    print(a.is_palindrome(b))
    print(a.is_palindrome(c))
    print(a.is_palindrome(d))
