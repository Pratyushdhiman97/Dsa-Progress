class Solution(object):
    def majorityElement(self, nums):
        # using moores voting algo
        el=0
        cnt=0
        for i in range(len(nums)):
           if cnt==0:
             el=nums[i]
             cnt+=1
           elif el==nums[i]:
             cnt+=1
           else:
             cnt-=1
        return el
        




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna