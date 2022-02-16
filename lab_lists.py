# List

# Q1: Write a Python program to sum all the items in a list.

lst = [1,2,3,4]
sum = 0
for num in lst:
    sum += num

# Q2: Write a Python program to get the largest number from a list.
largest = sorted(lst)[-1]

# Create an odd numbers list from the elements of a range from 
# 1200 to 2000 with steps of 125, using list comprehension.

lst2 = [num for num in range(1200, 2000, 125) if num % 2 != 0]

# Tuple 

# Q1: Create a tuple with duplicate elements and find the index of the the duplicate item.

# Note: This for return the index of all duplications
tpl = (1,2,3,1,2,4,5,2)
lst = list(tpl)
duplicates = []
for i in range(len(lst)):
    if lst.count(lst[i]) > 1 :
        item = lst[i]
        lst[i] = " "
        duplicates.append(lst.index(item))



# Q2: Write a Python program to remove duplicates from a tuple

# Direct solution
st = set(tpl)
tpl = tuple(st)

# Another Solution
'''
lst = list(tpl)
tmp = []
for i in duplicates:
    lst[i] = ""

for i in lst:
    if i != "":
        tmp.append(i)

tpl = tuple(tmp)

'''
