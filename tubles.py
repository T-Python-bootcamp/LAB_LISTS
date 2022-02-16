#Q1: Create a tuple with duplicate elements and find the index of the the duplicate item.
#A1
def lastIndex(tubl):
    print(tubl.index(1))
lastIndex((1,2,5,4,1))
#Q2: Write a Python program to remove duplicates from a tuple
#A2
def removeDubl(tubl):
    newSet=set(tubl)
    tubl=newSet
    print(tubl)
removeDubl((1,3,5,5))