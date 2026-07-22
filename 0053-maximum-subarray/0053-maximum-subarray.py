class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        sum=0
        for el in nums:
            sum = sum + el
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum=0
        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna