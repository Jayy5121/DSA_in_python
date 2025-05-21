class Solution(object):
    def maxArea(self, height):
        i=0 #left side of array
        j=len(height)-1 #right side of array
        max_area=0

        while i<j:
            current_area=(j-i)*min(height[i],height[j])
            max_area=max(max_area,current_area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area