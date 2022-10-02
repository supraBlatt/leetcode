class Solution:
    
    # ultra naive is O(n^3) time to substr and O(m) space for alphabet dict
    
    # a bit less naive but still naive 
    # i believe it's o(n^2) thanks to the 'in'. 
    #def lengthOfLongestSubstring(self, s: str) -> int:
        #seen = ""
        #length = 0
        #for ch in s:
            ## if the character has been seen skip over first appearance
            ## any string containing both would be illegal anyway.

            ## i believe this 'in' is o(n^2) amortized? 
            ## also the split is another o(n) amortized as it 'keeps walking forward'?
            #if ch in seen:
                ## split after first appearence 
                #length = max(len(seen), length)
                #seen = seen.split(ch, 1)[1]
            ## add the new appearance to the end
            ## is this also a problem with python's string immutability?
            #seen += ch

        #return max(len(seen), length)

    # same general approach but with a set instead
    # i believe that this one is o(n) time thanks to sets hashes?
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0 
        left = 0 

        for i in range(len(s)): 
            # add characters to set until one shows up again
            # then move left index until we 'remove' it.
            if s[i] in seen:
                length = max(length, len(seen))
                # is there a better way to write this dumb loop?
                # anyway 'n' movements forward overall
                while(s[i] != s[left]): 
                    seen.remove(s[left])
                    left += 1
                left += 1

            # add new element to set.. 
            seen.add(s[i])

        return max(length, len(seen))
