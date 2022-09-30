from ast import List

class Solution:

    ## naive matrix approach. very similar to @weakest_rows.py
    #def maximumWealth(self, accounts: List[List[int]]) -> int:
        ## multiply by 1s vector to sum rows
        ## again, summing over 0th axis works too
        #accs = np.array(accounts) 
        #ones = np.ones_like(accs[0])
        #return accs.dot(ones).max()
    
    # using lists this time 
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(l) for l in accounts])
    