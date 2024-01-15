# Вернуть количество вхождений элемента в массив. Размер итогового массива неважен
# Первыми в итоговом массиве должны быть элементы, отличные от val
# Нельзя создавать новый массив
class Solution:
    def remove_element(self, nums: list[int], val: int) -> tuple[int, list[int]]:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k, nums


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    s = Solution()
    print(s.remove_element(nums, val))
