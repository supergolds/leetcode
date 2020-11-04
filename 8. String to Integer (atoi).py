import sys

def check(str: str) -> int:
    maxInt = 2 ** 31 - 1
    minInt = -2 ** 31
    try:
        answer = int(str)
        if answer > maxInt:
            return maxInt
        elif answer < minInt:
            return minInt
        return answer
    except ValueError:
        return 0

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str):
            return 0


        answer = ""
        words = str.split()

        for char in words[0]:
            if not char.isalpha() and char is not '.':
                answer = "{}%s".format(answer) % char

            elif char is not '-' and (char.isalpha() or char is '.'):
                if len(answer) == 0:
                    return 0
                print(check(answer))
                return

        print(check(answer))

sol = Solution()
test1 = '42'
test2 = '    -42'
test3 = '4193 with words'
test4 = 'words and 987'
test5 = '-91283472332'
test6 = '3.14159'
test7 = '    -0012a42' # -12
test8 = '+-12' # 0
test9 = '00000-42a1234' # 0
test10 = '   +0 123' # 0
test11 = '    -88827   5655  U'
test12 = '-5-'

print(sol.myAtoi(test10))