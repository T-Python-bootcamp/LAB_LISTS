### Q1: Write a Python program to sum all the items in a list.
answer = 0
lst = [1,2,3]
for item in lst:
    answer += item
print(answer)

#--------------------------------------------------#
### Q2: Write a Python program to get the largest number from a list.
answer = 0
lst = [1,2,3]
for item in lst:
    if item > answer:
        answer = item
print(answer)

#--------------------------------------------------#
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, 
# using list comprehension.
oddNum = []
oddNum = [item for item in range(1200, 2000, 125) if not item % 2 == 0]
print(oddNum)

#--------------------------------------------------#
