class Solution:
    def search(self, nums, target) -> bool:
        try:
            start = nums.index(target)
            temp = -1
            for i in range(start, len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
                temp = nums[i + 1]

            for i in range(start):
                if temp > nums[i]:
                    return False
                temp = nums[i]

            return True

        except:
            return False

sol = Solution()
print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))