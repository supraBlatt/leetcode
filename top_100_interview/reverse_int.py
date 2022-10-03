class Solution:
    
    ## a shit hacked together iterative thought process one
    #def reverse(self, x: int) -> int:
        
        #a = x if x >= 0 else -x
        #sign = -1 if x < 0 else 1
        
        ## transform to string, reverse and then back to integer
        #result = sign * int(str(a)[::-1])
        
        #if result >= 2**31 or result <= -2**31:
            #return 0
        #return result
    
    ## subtle fixes to it
    ## still very very naive.. does it have arch specific issues?
    #def reverse(self, x: int) -> int: 
        ## transform to string and reverse 
        ## wouldn't this get fucked if we were to have an overflow?
        #result = int(str(abs(x))[::-1])
        
        ## need to check only one side as we are working with positive
        #if result >= 2**31:
            #return 0
        #return result if x >= 0 else -result

    ## another change
    #def reverse(self, x: int) -> int: 
        
        #result = 0
        #n = abs(x)
        #while n > 0: 
            ## i believe this would get fucked too if it were to overflow..
            ## should check with intmax before assignment?
            #result = result*10 + n%10
            #n = n // 10 
        
        ## need to check only one side as we are working with positive
        #if result >= 2**31:
            #return 0
        #return result if x >=0 else -result

    # another change
    def reverse(self, x: int) -> int: 
        result = 0        
        n = abs(x)

        # we would like to see if (res * 10 + n%10) overflows and abort before assignment
        # crutch values
        max_val = 2**31 // 10  
        max_dig = 7 if x > 0 else 8
        while n:

            # - (2**31-1) is 2147483647 
            # - there are two viable ways I've seen that could lead to overflow. 

            # - 1.  if res > 214748364 then multiplying it by 10 would overflow. 
            # - 2.  if the digit causes the tipover we're also big rip
            # --    that would be when res == 214748364 and digit > 7 so combining them would be more than 2147483647

            # these 2 options apply for (-2**31) as well which is -2147483648, but the critical digit is 8 instead
            digit = n%10
            if result > max_val or (result == max_val and digit > max_dig):
                return 0
            result = result*10 + digit
            n = n // 10

        return result if x>0 else -result       
