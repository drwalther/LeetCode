class Solution(object):
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_nums:
                return [dict_nums[complement], i]
            else:
                dict_nums[num] = i


# Если гарантируется, что массив чисел всегда упорядочен, то можно решить так:


# class Solution(object):
#     def two_sum(self, nums: list[int], target: int) -> list[int]:
#         start_pointer = 0
#         end_pointer = -1
#
#         while nums[start_pointer] + nums[end_pointer] != target:
#             if nums[start_pointer] + nums[end_pointer] < target:
#                 start_pointer += 1
#             else:
#                 end_pointer += -1
#
#         return [start_pointer, nums.index(nums[end_pointer])]
#
#
if __name__ == "__main__":
    n = [1, 2, 4, 6, 8, 11, 14]
    t = 13
    solution = Solution()
    print(solution.two_sum(n, t))
