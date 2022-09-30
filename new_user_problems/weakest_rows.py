from ast import List

class Solution:
    
    ## naive matrix approach
    #def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #army = np.array(mat) #bts army woooooooooooooooo (jk)
        
        ## multiply matrix by 1s vector
        ## i guess you could use sum over the 0 axis too.. yeah thats 1 line instead of 3.  
        #ones = np.ones_like(army[0])
        #num_soldiers = army.dot(ones)
        
        ## sort soldiers and get top k 
        ## here im actually unsure how to do it so i'll use native python.. 
        #enum = [(i, v) for v, i in enumerate(num_soldiers)]
        #return [v for i, v in sorted(enum)[:k]]
    
    # using lists this time 
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        # list comprehension goes brrrrrrrrrr
        num_soldiers = []
        for i, lst in enumerate(mat): 
            num_soldiers.append((sum(lst), i))
        num_soldiers.sort()

        #num_soldiers = sorted([(sum(lst), i) for i, lst in enumerate(mat)])
        return [x[1] for x in num_soldiers[:k]]
        