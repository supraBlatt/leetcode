from ast import List

class Solution:

    # idk why but i think about suffix trees and aho corsiak 

    # naive approach
    # i believe it's O(mn). move one character every time  
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # max length of lcp is the min of the strings lengths
        l = min([len(s) for s in strs])

        # iterate horizontally and then vertically
        for i in range(l):
            c = strs[0][i]
            for j in range(len(strs)):

                # if stopped matching, return current lcp
                if c != strs[j][i]:
                    return strs[0][:i]
                
        return strs[0][:l]

    ## another O(mn). function application lmao 
    #def longestCommonPrefix(self, strs: List[str]) -> str:
        ## the idea is that LCP(S[0], .., S[n]) = LCP(S[n], LCP(S[n-1], ... ((((...(LCP(s[0], s[1])..))
        #prefix = strs[0]
        #for i in range(1, len(strs)):
            ## calculate LCP(prefix, s[i])
            #l = min(len(prefix), len(strs[i]))

            #for j in range(l):
                ## update prefix
                #if prefix[j] != strs[i][j]:
                    #prefix = prefix[:j]
        #return prefix

    # i believe there's also a binary approach to this.. 
