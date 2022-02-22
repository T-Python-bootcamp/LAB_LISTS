# Q1: Write a Python program to sum all the items in a list.
my_lists =[2,3,5,765,63,143,323,33,0]
print("list :",my_lists)

sum=0
for num in my_lists:
    sum+=num

print("sum number from a list is :" ,sum)

## Q2: Write a Python program to get the largest number from a list.

print("largest number from a list is : " ,max(my_lists))

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

my_lists = [num for num in range(1200, 2000, 125) if num % 2 != 0]
print("odd numbers range from 1200 to 2000 with steps of 125 is :",my_lists )

######
# Q1: Create a tuple with duplicate elements and find the index of the the duplicate item.

duplicate=(1,2,3,1,1,4,3,5)
print("tuple :" ,duplicate)
print(" duplicate elements :",duplicate.count(1))

# Q2: Write a Python program to remove duplicates from a tuple
result  = []
for elem in duplicate:
    if elem not in result :
        result.append(elem)
print("tuple without repetition :",tuple(result ))

####
