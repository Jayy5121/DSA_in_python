def spriral(matrix):
    row=len(matrix)
    col=len(matrix[0])
    left=0
    right=col-1
    top=0
    bot=row-1
    ans=[]
    while top<=bot and left<=right:
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top+=1
        for i in range(top,bot+1):
            ans.append(matrix[i][right])
        right-=1
        if top<=bot:
            for i in range(right,left-1,-1):
                ans.append(matrix[bot][i])
            bot-=1
        if left<=right:
            for i in range(bot,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
    return ans
print(spriral([[1,2,3],[4,5,6],[7,8,9]]))
