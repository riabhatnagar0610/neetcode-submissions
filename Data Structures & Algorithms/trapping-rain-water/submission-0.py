class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 1
        right = n - 2
        leftMax = height[left - 1]
        rightMax = height[right + 1]
        ans = 0
        while left <= right:
            if leftMax >= rightMax:
                ans += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
            else:
                ans += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left +=1
        return ans