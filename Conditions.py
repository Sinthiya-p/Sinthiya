print("Write a Python program to check whether a number is positive, negative, or zero.")
number=int(input("enter your number"))
if(number>0):
    print("positive")
elif(number<0):
    print("negative")
elif(number==0):
    print("Zero")
print("Write a program to check whether a number is even or odd")
if(number%2==0):
    print("even")
elif(number%2==3):
    print("odd")
print("Write a program to check if a person is eligible to vote (age ≥ 18)")
age=20
if(age>=18):
    print("you are eligible to vote")
else:
    print("your not eligible to vote")
print("Write a program to check if a student passed or failed based on marks")
sub1 = 49
sub2 = 64
sub3 = 34
sub4 = 57
sub5 = 63
if(sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35 and sub5>=35):
    print("pass")
else:
    print("fail")
print("Write a program to find the largest of two numbers")
num1 = 23
num2 = 53
if num1 > num2:
    print(f"the largesr num is: {num1}")
elif num2 > num1:
    print(f"the largest num is:{num2}")
else:
    print("both numbers are equal")
print("Write a program to display grade (A, B, C, D, Fail) based on marks")
mark=int(input("enter your mark"))
if mark>90 and mark<=100:
    print("A greater")
elif mark>80 and mark<=90:
    print("B greater")
elif mark>60 and mark<=80:
    print("C greaater")
else:
    print("D greater")
