class Solution:
    def longestCommonPrefix(self, strs) -> str:
        idx, size, T = 0, len(strs), 0
        answer = ""

        while T is not size - 1:
            for i in range(size-1):
                if strs[idx] == strs[idx+1]:
                    answer += strs[idx+1]
                else:
                    idx += 1
                    break
            T += 1

        return answer
sol = Solution()
test = ["flower","flow","flight"]
print(sol.longestCommonPrefix(test))