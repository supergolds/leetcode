class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        result = ""
        size = len(s)
        notPalin = False

        for i in range(size):
            for j in range(i, size):
                temp = ""
                idx = j
                for k in range(i, j // 2 + 1):
                    if s[k] != s[idx]:
                        notPalin = True
                        break
                    idx -= 1

                if notPalin:
                    notPalin = False
                else:
                    for l in range(i, j + 1):
                        temp = "{}%s".format(temp) % s[l]
                    if longest < len(temp):
                        longest = len(temp)
                        result = temp

        return result

sol = Solution()
print(sol.longestPalindrome("aacabdkacaa"))