# LISTS

# 1
list = [4, 3, 55, 87, 35, 24]
print(sum(list))

# 2
print(max(list))

# 3
listOdd = [x for x in range(1200, 2000, 125) if x % 2 == 1]
print(listOdd)
# TUPLES
print("____________________________________")

# 1
tup = (35, 1, 65, 7, 35, 5, 35, 43)

result = [i for i in range(len(tup)) if tup[i]==35]
print(result)

# 2
print(set(tup))