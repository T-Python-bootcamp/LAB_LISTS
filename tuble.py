# Q1: Create a tuple with duplicate elements and find the index of the the duplicate item.


test_list = [3, 4, 4, 5, 3, 4,  3, 4, 4, 5, 6, 7]
print("The original list : " + str(test_list))
res = list(set([ele for ele in test_list
            if test_list.count(ele) > 1]))
print("All the duplicates from list are : " + str(res))

# Q2: Write a Python program to remove duplicates from a tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
print("The original tuple is : " + str(test_tup))
res = tuple(set(test_tup))
print("The tuple after removing duplicates : " + str(res))