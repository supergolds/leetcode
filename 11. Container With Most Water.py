class Solution:
    def maxArea(self, height) -> int:
        answer, area = 0, 0
        big = max(height)
        gap = big
        start = height.index(max(height))
        end = len(height)

        for idx in range(0, start):
            gap = idx - start
            if height[idx] < big:
                wall = height[idx]
            else:
                wall = big
            area = wall * gap
            if answer < area:
                answer = area

        for idx in range(start, end):
            gap = idx - start
            if height[idx] < big:
                wall = height[idx]
            else:
                wall = big
            area = wall * gap
            if answer < area:
                answer = area

        return area


sol = Solution()
test = [1, 2, 1]
print(sol.maxArea(test))