class Solution(object):
    def rearrangeArray(self, nums):
        ans=[0]*int(len(nums))
        a=1
        b=0
        for i in range(len(nums)):
  
           if nums[i] < 0 :
            ans[a]=nums[i]
            a += 2
           else:
            ans[b]=nums[i]
            b+=2

        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna