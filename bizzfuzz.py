from typing import List

class Solution:
    
    ## initial sketch.. very very naive
    #def fizzBuzz(self, n: int) -> List[str]:
        #bizzfuzz = list(map(str, range(1, n+1)))
        #five = three = 0 

        ## iterate over numbers. update modulus 
        #for i in range(1, n+1): 

            ## update 
            #three = (three + 1) % 3
            #five = (five + 1) % 5 

            ## test for fizzbuzz
            #if five == 0: 
                #if three == 0: 
                    #bizzfuzz[i-1] = "FizzBuzz"
                #else: 
                    #bizzfuzz[i-1] = "Buzz"
            #elif three == 0:
                #bizzfuzz[i-1] = "Fizz" 

        #return bizzfuzz


    ## a bit better.. big fat question mark
    #import numpy as np 
    #def fizzBuzz(self, n: int) -> List[str]:
        #bizz = np.vectorize(lambda x: "FizzBuzz" if x%15==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else str(x)) 
        #return bizz(np.arange(1, n+1))

    # naive number 2
    def fizBuzz(self, n: int) -> List[str]: 
        # without a big fat list at the start
        bizz = []

        for i in range(1, n+1): 
            if i%15 == 0: 
                bizz.append('FizzBuzz')
            elif i%3 == 0:
                bizz.append('Fizz')
            elif i%5 == 0: 
                bizz.append('Buzz')
            else: 
                bizz.append(str(i))
        return bizz

