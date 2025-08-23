class Solution(object):
    def flipAndInvertImage(self, image):
        new_image=[]
        for row in image:
            flipped=row[::-1]
            inverted=[]
            for val in flipped:
                inverted.append(val^1)
            new_image.append(inverted)
        return new_image
s1=Solution()
print(s1.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))