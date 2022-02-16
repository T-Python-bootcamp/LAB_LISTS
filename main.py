
# ------
# LISTS:
lst = [3,10,5,22,55,2,11]

#   Q1:
result1 = 0
for item in lst: result1+=item
print(f"\nLists Q1: {result1}")

#   Q2:
result2=0
for item in lst: 
    if item>result2: result2=item
print(f"Lists Q2: {result2}")

#   Q3:
result3 = [item for item in range(1200,2000,125) if not item%2==0]
print(f"Lists Q3: {result3}\n")

#-------
#Tuples:
tup = (1,2,3,2,2,0,5)

#   Q1:
for item in range(len(tup)):
    if tup.count(tup[item])>1: print(f"Tuples Q1: {item}")

#   Q2:
tup = list(tup)
for item in tup:
    if tup.count(item)>1: tup.remove(item)
print(f"Tuples Q2: {tup}\n")

