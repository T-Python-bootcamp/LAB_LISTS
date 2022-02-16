import math
#A1:
def sumNumber(nums):
    total=0
    for num in nums:
        total+=num
    print(total)
sumNumber([1,3,6,2,7])
#A2:
def largNumber(nums):
    large=nums[0]
    for num in nums:
        if num>large:
            large=num
    print(large)
largNumber([1,3,6,2,7])
#A3
def oddNumber():
    newList=[num for num in range(1200,2000,125) if  math.remainder(num, 2)!=0.0]
    print(newList)
oddNumber()