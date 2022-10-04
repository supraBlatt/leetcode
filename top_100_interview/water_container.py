from ast import List

class Solution:

    # naive O(n^2). check all permutations of lines and their respective areas
    #def maxArea(self, height: List[int]) -> int:
        #max_area = 0

        #for i in range (len(height)):
            #for j in range(len(height)):
                ## the area is the distance between lines
                ## multiplied by the smallest of heights
                #area = (j-i) * min(height[j], height[i])

        #return area

    # a bit less naive O(n). the idea here is to eliminate candidates 
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        left = 0
        right = len(height) - 1

        # the approach would be moving the lowest of the two bars inwards as it is eliminated

        # the motivation behind it is that given bars i,j where i is at least as tall as j.
        # the area of i,j is j * |i-j|. the area of every k,j for k>=i is smaller than that. 
        # the height of each k,j is at most j, and the distance between points is smaller than |i-j|. 
        # - in essence, the bar j is eliminated as all inwards matches k,j are smaller than the current i,j.
        # no point in checking further so we advance j inwards. what a brilliant approach.
        while left != right: 
            max_area = max(max_area, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else: 
                right -=1 

            # could we make an improvement when they're equal? as both bars are eliminated. 
        return max_area 
                