class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        for char in range(len(strs[0])):
            for word in strs:
                if not word.startswith(prefix + strs[0][char]):
                    return prefix
            prefix += strs[0][char]
        return prefix
