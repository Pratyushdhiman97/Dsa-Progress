class Solution(object):
    def nextPermutation(self, nums):
        
        i=len(nums)-2
        idx=-1
        while i >= 0:
            if nums[i] < nums[i+1]: #we found breaking point the el on the left should be smaller
               idx=i
               break
            i-=1


        if idx == -1:
            # Reverse whole list
            nums.reverse()
            return

        for j in range(len(nums)-1,idx,-1):

            if nums[j] > nums[i] :
                #we swap the number and breaking point 
                nums[idx],nums[j]=nums[j],nums[idx]
                break
            #   now we reverse the array

        nums[idx + 1:] = reversed(nums[idx + 1:])

        return nums



     
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna