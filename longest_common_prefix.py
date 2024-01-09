# Вернуть общую для всех строк в списке подстроку, либо пустую строку, если ее нет
class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        prefix = min(strs)

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


if __name__ == "__main__":
    s = Solution()
    b = ["dog", "racecar", "car"]
    с = ["flower", "flow", "flight"]
    print(s.longest_common_prefix(b))
    print(s.longest_common_prefix(с))
