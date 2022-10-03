class Solution:

    # naive sketch + overflow checking from 'reverse_int'
    def myAtoi(self, s: str) -> int:
        # strip spaces 
        s = s.lstrip(' ')
        if not len(s): 
            return 0

        # determine sign if exists
        # 1 for negative, 0 otherwise
        sign = 0
        if s[0] in ['-', '+']:
            if s[0] == '-': 
                sign = 1
            s = s[1:]

        # values for overflow test
        max_val = 2**31
        max_dig = 7 + sign

        # translate to int
        result = 0 
        for index in range(len(s)):

            # kill if not digit 
            if not s[index].isdigit(): 
               break 

            digit = int(s[index])
            # clamp to edges if overflowed
            if result > max_val//10 or (result == max_val//10 and  digit > max_dig):
                return -max_val if sign else max_val - 1
            
            # append to result
            result = result*10 + digit 

        return -result if sign else result
