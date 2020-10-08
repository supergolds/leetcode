"""
1. 이 코드는 각 케이스를 하나하나 씩 비교해가며 정답을 찾는 그리디 알고리즘
그러나 시간이 너무 오래걸려서 오답이 떴다.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        size = len(height)
        for i in range(size):
            chk = height[i]
            for j in range(i + 1, size):
                cmp = height[j]
                if chk <= cmp:
                    tmp = (j - i) * chk
                    if tmp > answer:
                        answer = tmp
                else:
                    tmp = (j - i) * cmp
                    if tmp > answer:
                        answer = tmp

        return answer
"""

