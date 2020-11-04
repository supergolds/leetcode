class Solution:
    def isValid(self, s: str) -> bool:
        big, mid, small = [], [], []
        for i in s:
            if i == '(':
                small.append(i)
            elif i == '[':
                mid.append(i)
            elif i == '{':
                big.append(i)
            elif i == ')':
                if '(' not in small:
                    return False
                else:
                    small.pop()
            elif i == ']':
                if '[' not in mid:
                    return False
                else:
                    mid.pop()
            elif i == '}':
                if '{' not in big:
                    return False
                else:
                    big.pop()
        return True

sol = Solution()
s = "([)]"
print(sol.isValid(s))