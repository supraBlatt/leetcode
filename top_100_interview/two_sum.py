from ast import List

class Solution:

    ## naive 2 pointer approach
    #def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## list of tuples (value, index) 
        #s = sorted([(v, i) for i,v in enumerate(nums)])
        #left = 0 
        #right = len(s)-1 

        ## move both pointers to each other as necessary
        #while left < right: 
            #sum = s[left][0] + s[right][0] 
            #if sum == target: 
                #return [s[left][1], s[right][1]] 
            #if sum > target:
                #right -= 1
            #else: 
                #left += 1
        #return []
    
    # ultra naive dictionary approach.
    # O(n) time, O(m) memory. m - amount of different letters
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_seen = {}
        
        for i, num in enumerate(nums): 
            # if seen the complement, return its index
            if (target-num) in last_seen:
                return [last_seen[target-num], i]
            # update last seen 
            last_seen[num] = i
            
        return []

