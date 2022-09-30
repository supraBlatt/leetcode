class Solution:

    ## didn't finish but it's a good exercise?
    #def is_valid_roman(self, s: str) -> bool: 
        #return True 

    ## initial sketch.. 
    #def romanToInt(self, s: str) -> int:

        ## so there are multiple approaches to this.. 
        ## i'll try to use the most simple one
        #symbol_to_int = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        #prev = result = 0
        #for symbol in s: 

            ## translate symbol to int 
            #cur = symbol_to_int[symbol]
            #result += cur 

            ## i couldn't find a way to do it with one pass.
            ## effectively there are 2 passes on the array. 
            #if prev > 0 and cur > prev: 
                #result -= 2 * prev 
            #prev = cur  

        #return result

    # actually does it in one pass? 
    def romanToInt(self, s: str) -> int:
        symbol_to_int = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        
        prev = result = 0
        # go over the string backwards
        for symbol in s[::-1]:
            cur = symbol_to_int[symbol]
            
            if cur < prev: 
                result -= cur 
            else: 
                result += cur 
            prev = cur 
        return result 

    ## a numpy approach.. seems like it has some problems tho
    #def romanToInt(self, s: str) -> int:
        #symbol_to_int = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        #to_int = np.vectorize(lambda x: symbol_to_int[x])
        #n = to_int(np.array(list(s)))
        #big = n[1:] > n[:-1]
        ## fancy dot products
        #return np.dot(n[:-1], ~big) - np.dot(n[:-1], big) + n[-1]
