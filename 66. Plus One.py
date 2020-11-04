class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[len(digits)-1] += 1
        return digits

sol = Solution()
test = [9]
print(type(test))
print(sol.plusOne(test))