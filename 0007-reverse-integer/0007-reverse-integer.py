class Solution(object):
    def reverse(self, x):
       rnum=0
       if x>0:
        while x > 0:
            n = x % 10 #  this gives us the last digit
            x = x//10 # this removes the last digit
            rnum = (rnum*10)+ n
        ans=rnum 
        
       else:
        a=-x
        while a > 0:
            n = a % 10 #  this gives us the last digit
            a = a//10 # this removes the last digit
            rnum = (rnum*10)+ n
        ans=-rnum
        
       if ans<- 2**31 or ans> 2**31 -1:
        return 0
       else:
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna