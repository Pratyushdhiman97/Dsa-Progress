class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        def rev(nums,start,end):
   
         while start < end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        rev(nums,0,len(nums)-1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)
       
        return nums
 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna