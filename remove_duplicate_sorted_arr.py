# Нужно вернуть число уникальных элементов массива


class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == "__main__":
    s = Solution()
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.remove_duplicates(a))
