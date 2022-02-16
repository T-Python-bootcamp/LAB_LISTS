lst = [3, 4, 5]

x = 0
for n in lst:
    x += n
    print(x)
  
#  ---------------------- 


max = lst[0]
for i in lst:
    if i > max:
        max = i 
        print(max)   
        

#  ---------------------- 


odds = []
odds = [item for item in range(1200, 2000, 125) if item%2 ]
print(odds)

#  ---------------------- 


tup = ("A", "B", "C", "A")
for i in tup:
    if tup.count(i) > 1:
        print(tup.index(i))

#  ---------------------- 

def dubs():
    tup = ("A", "B", "C", "A")
    lst = list(tup)
    for i in tup:
        if tup.count(i) > 1:
            print(i)
            lst.remove(i)
            print(lst)
            tup = tuple(lst)
            print(tup)
            
dubs()
