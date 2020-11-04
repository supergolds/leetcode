class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size)

"""
회전 전의 열 번호와 행 번호가 일치한다.
그리고 회전 후의 열은 N-1에서 회전 전의 행을 뺀 값과 같다.
"""