print("Adding Two Lists")
l=["good",123,89]
l1=[56,"friend",7]
l2=l+l1
print(l2)

print("Repeating list elements")
l3=l*3
print(l3)

print("Check if an element exists in a list")
li=[50,78,95,25,90]
num=int(input("Enter a number to check: "))
if num in li:
    print(f"{num} exists in the list")
else:
    print(f"{num} not found in the list")

print("Slicing a list")
l5=[1,2,3,4,5,6,7,8,9]
print(l5[:3])
print(l5[-3:])

print("Largest of Two Numbers in a List")
li.sort()
print("Two Largest numbers are: ",li[-1],"and",li[-2])

print("Finding Duplicate elements in a list")
l6=[1,2,3,2,1,4,7,5]
duplicates=[]
for i in l6:
    if l6.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate Elements: ",duplicates)

print("Remove duplicate elements from a list")
unique=[]
for i in l6:
    if i not in unique:
        unique.append(i)
print("List after removing duplicates:", unique)

print("List of Square Numbers from 1 to 10")
squares=[]
for i in range(1,11):
    squares.append(i**2)
print("Squares from 1 to 10: ",squares)
print("Separate even and odd numbers into two lists")
even=[]
odd=[]
for i in l6:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers: ",even)
print("Odd Numbers: ",odd)
print("Finding Common Elements between two lists")
lis1=[1,2,3,4,5]
lis2=[4,5,6,7]
common=[]
for i in lis1:
    if i in lis2:
        common.append(i)
print("Common elements: ",common)
print("Finding Elements present in one list but not in another")
diff=[]
for i in lis1:
    if i not in lis2:
        diff.append(i)
print("Elements in list1 but not in list2:",diff)
print("Removing all occurrences of a specific element from a list")
liss=[1,2,3,2,4,2,5]
x=2



while x in liss:
    liss.remove(x)
print("List after removing all",x,":",liss)
print("Converting a list into a tuple")
print("List: ",l2)
print("Tuple: ",tuple(l2))
print("Finding the Average of list elements")
avg=sum(li)/len(li)
print("Average: ",avg)
print("Counting positive,negative, and zero numbers in a list")
li3=[10,-5,0,3,-2,-1,0,8,9]
p=n=z=0
for i in li3:
    if i>0:
        p+=1
    elif i<0:
        n+=1
    else:
        z+=1
print("Positive: ",p)
print("Negative: ",n)
print("Zero: ",z)
print("Finding product of all elements in a list")
li4=[2,3,4,5]
prod=1
for i in li4:
    prod*=i
print("Product of elements: ",prod)
print("Create a Tuple")
t=()
l=list(t)
num=int(input("Enter number of elements: "))
for i in range(num):
    e=int(input("Enter an element: "))
    l.append(e)
t = tuple(l)
print(t)
print()
print("Finding the size of the tuple")
print(l)
print(len(l))
print()
print("Sorting tuples")
sorted_tuple=sorted(t)
print("Sorted Tuple: ",sorted_tuple)
print()
print("Create a tuple with different data types")
tup=()
li=list(t)
num=int(input("Enter number of elements: "))
for i in range(num):
    el=input("Enter an element: ")
    li.append(el)
tup = tuple(li)
print(tup)
print()
print("Unpack a tuple into several variables")
tup1=1,2,3
a,b,c=tup1
print("a: ",a)
print("b: ",b)
print("c: ",c)
print()
print("Converting a tuple to a string")
print(tup)
print(str(tup))
print()
print("Get the 4th element and 4th element from last of a tuple")
t1=(10,20,30,40,50,60,70,80)
print("4th element: ",t1[3])
print("4th element from last: ",t1[-4])
print()
print("Finding Repeated items in a tuple")
duplicates=[]
for i in t1:
    if t1.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Repeated items: ",duplicates)
print()
print("To Check whether an element exists or not")
t2=(34,56,23,25,81)
x=int(input("Enter element to check: "))
if x in t2:
    print(x,"exists in the tuple")
else:
    print(x,"doesn't exist in the tuple")
print()
print("Convert a list to a tuple")
lis=[1,2,3,4]
print(lis)
print(tuple(lis))
print()
print("Remove an item from a tuple")
tup2=(1,2,3,4,5)
li5=list(tup2)
li5.remove(3)
tup2=tuple(li5)
print("Tuple after Removing 4th element: ",tup2)
print()
print("Slicing a tuple")
print(tup2)
print("First Two Elements: ",tup2[:2])
print("Last Two Elements: ",tup2[-2:])
print()
print("Finding the index of an item in a tuple")
tup3=(5,10,15,20,25)
print("Index of 15 is: ",tup3.index(15))
print()
print("Finding the Length of Tuple")
print(tup3)
print(len(tup3))
print()
print("Reversing a Tuple")
print(tup2)
print("Reversed Tuple: ",tup[::-1])
print()
print("Converting a given string list to a tuple")
list2=['Almond','Cake','Berries','Dragon Fruit']
print(tuple(list2))

