class Solution(object):
    def singleNumber(self, nums):
        xorr = 0

        
        for num in nums:
            xorr ^= num

        return xorr
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna