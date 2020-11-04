class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        ans = 2 ** 31

        size = len(nums)
        nums.sort()
        for i in range(size - 2):
            l, r = i + 1, size - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                temp = abs(target - s)
                if temp == 0:
                    return s
                elif s > target:
                    if temp < abs(target - ans):
                        ans = s
                    r -= 1
                elif s < target:
                    if temp < abs(target - ans):
                        ans = s
                    l += 1

        return ans

sol = Solution()
print(sol.threeSumClosest([0, 2, 1, -3], 1))