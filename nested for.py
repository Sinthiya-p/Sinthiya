print("left traingle")
for i in range(5):
    for j in range(1,5-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()
print("right traingle")
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("square")
for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print()
print("print 8")
for i in range(7):
    for j in range(5):
        if (i in [0, 3, 6]) and (j > 0 and j < 4):
            print("*",end="")
        elif (j in [0, 4])and(i not in [0, 3, 6]):
            print("*",end="")
        else:
            print(" ",end="")
    print()    
print("hollow square")
n=8
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("hollow right traingle")
n=8
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("inverse right traingle")
x=5
for i in range(x,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("inverse left traingle")
y=5
for i in range(y,0,-1):
    for space in range(y-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
print("right traingle")
a=5
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("left traingle")
b=5
for i in range(b,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("hollow right traingle")
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
print("repeated alphabets right traingle")
for i in range(65,71):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()
print("continuous alapha right traingle")
x=5
ch=65
for i in range(1,x+1):
    for j in range(i):
        print(chr(ch),end="")
        ch+=1
    print()
print("repeated alphabets right traingle")
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()
print("sequential alphabets right traingle")
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()    
