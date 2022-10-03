
class Solution:
    
    """ preface: I know of 3 or 4 solutions from algorithms class..

     1) naive O(n^3) - look at all substrings, determine if palindrome and find max length 
     2) dynamic programming O(n^2) time and O(n) space [diagonals]
     3) odd and even palindromes O(n^2) time
     4) suffix trees + LCA preprocessing. O(n) space and time
        -   this one in particular is interesting. we can insert S#R(S) to the suffix tree.
            we could then find the LCA of suffix i and suffix 2n+2-i, or 2n+2-i-1 
            for odd and even palindromes respectively. compare the length of the LCA path
            to n the length of S
            and viola, palindrome verifier. 
         
            each LCA query is O(1) and we have O(n) comparisons. 
            -- i just.. couldn't find a way to implement it without having to implement suffix trees..
    """

    # compare letter by letter and move away from the proposed center
    def pali_len(self, s: str, c1: int, c2: int) -> int:
        # should i use in range here..?
        while (0 <= c1 and c2 < len(s)) and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return c2 - c1 - 1 
        #return s[c1 + 1: c2] 

    # odd and even palindromes approach
    def longestPalindrome(self, s: str) -> str:

        # thank you shai golan, what would I have done without you. 
        # pali = ""
        start = end = 0         
        for i in range(len(s)):

            # calculate lengths for odd and even palindromes
            length = max(self.pali_len(s, i, i), self.pali_len(s, i, i+1))

            # shameless code theft I admit I had trouble phrasing this.. 
            if (length > end - start): 
                start = i - ((length-1)/2)
                end = i + (length/2)  

            # is it.. bad to work with strings here? 
            # odd = self.pali_len(s, i, i)
            # even = self.pali_len(s, i, i+1)
            # longest = odd if len(odd) > len(even) else even
            # pali = pali if len(pali) > len(longest) else longest               

        return s[start: end+1]
        # return pali        
