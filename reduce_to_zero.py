class Solution:

    ## naive divide by 2 until you can't
    #def numberOfSteps(self, num: int) -> int:
        #count = 0

        ## big dum, using not number theory.. 
        #while num: 
            #num = (num//2) if num%2 == 0 else (num-1)
            #count += 1
        #return count
    
    # a bit smarter using bitwise.. 
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num: 
            num = (num>>1) if (num&1) == 0 else (num-1)
            count += 1
        return count
