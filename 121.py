def maxProfit(nums):
    maxi=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            profit=nums[j]-nums[i]
            maxi=max(profit,maxi)
    if maxi<0:
        return 0
    return maxi
print(maxProfit([7,6,4,3,1]))

def maxProfit2(nums):
    min_price=float('inf')
    max_price=0
    for price in nums:
        min_price=min(min_price,price)
        max_price=max(max_price,price-min_price)
    return max_price
print(maxProfit2([7,1,5,3,6,4]))