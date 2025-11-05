print("divisible 6 buy not by 9")
for i in range(1,101):
   if i%6==0 and i%9!=0:
    print(i)
print("sum of odd numbers")
sum=0
for i in range(1,51,2):
    sum+=i
print(sum)
print("sum of even number")
sum=0
for i in range(1,51,1):
    sum+=i
print(sum)
print("divisible by both 4 and 6")
count=0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count+=1
print(count)
print("mutiplication table")
num=int(input("enter your number"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
print("factorial of a given number n")
count=1
n=int(input("enter your number"))
for i in range(1,n,+1):
      n*=i
print(n)
print("prime numbers between 1 and 50")
for num in range(2,51):
    count=0
    for i in range(2,num):
        count+=(num%i==0)
    if count==0:
         print(num)
print("arithmetic sum of digits")
num=int(input("enter your number"))
sum=0
num_digit=len(str(num))
for i in range(num_digit):
   digit=n%10
   sum+=digit
   n=n//10
   print(i)
print("sum:",sum)
print("perfect cubes in 500")
count=0
for i in range(1,501):
   cube=round(i**(1/3))
   if cube **3==i:
      count+=1
      print(i)
print("conut 1,500:",count)      
print("reverse number in arithmetic")
num=int(input("enter your number"))
n=num
reverse_num=0
for i in range(count):
   digit=n%10
   reverse_num=reverse_num*10+digit
   n//=10
print("reverse num:",reverse_num)
print("1 to 100 but skip numbers ending digit 5")
for i in range(1,101):
   if i%10==5:
      print(i)
        

        
