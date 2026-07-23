class Solution(object):
    def maxProfit(self, prices):
        max = 0
        min = float('inf')
        
        for el in prices:
            if el < min:
                min = el
            elif el - min > max:
                max = el - min
                
        # Move this return statement outside the loop!
        return max
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna