print("string to the end of another string")
a="break"
b="fast"
c=a+b
print(c)
print("string contains the specified sequence of char values")
x=input("Enter a string: ")
y=input("Enter a character to check: ")
if(y in x):
    print("True")
else:
    print("not found")
print("all the characters in a string to lowercase")
z="SANTHIYA"
o=z.lower()
print(o)
print("leading or trailing whitespace from a given string")
s="     kannan    "
p=s.strip()
print(p)
print("reverse a string")
q="Ramar"
u=q[::-1]
print(u)
print("replace all spaces with underscores")
d="hello girl"
e=d.replace(" ","_")
print(e)
print("middle three characters")
s="python123"
mid=len(s)//2
middle_three=s[mid-1:mid+2]
print(middle_three)
print("first and last letter to capital")
g="papa"
p=g.upper()
print(p)
print("string character length")
k="thiya"
length=len(k)
print("length of a k:",length)
print("count number of words in a string")
name="sathiyakannan"
letter="a"
count=name.count(letter)
print("the letter",letter,"apper",count,"times in string")
print("replace in specified charecter with another string")
s="The quick brown fox jumps over the lazy dog"
p=s.replace("dog","fog")
print(p)
print("count vowels in a string")
w="Arunachalakani"
vowels="aeiouAEIOU"
count=0
for char in w:
    if char in vowels:
        count+=1
print("numbers of vowels:",count)        
print("string contains only whitespace")
l="i am going to maadurai"
if l.strip()==" ":
    print("only whitespace")
print("remove all digits from a string")
m="date14month7year2002"
v=''.join([ch for ch in m if not ch.isdigit()])
print(v)
print("length of your name using")
n="paramasivan"
length=len(n)
print("length of a n:",length)
print("string uppercase using")
s="sinthiya"
r=s.upper()
print(r)        
print("string lowercase using")
a="AMMU"
b=a.lower()
print(b)
print("appers in a string using")
x="i am going to madurai"
count=x.count("a")
print(count)
print("string start with the word 'Hello'using")
a="Hello Sinthiya"
if a.startswith("Hello"):
    print("The string with 'Hello'")
else:
    print("The string does not start with 'hello'")
print("string ends with'.com' using")
b="sinthiyaparamaasivan@gmail.com"
if b.endswith(".com"):
    print("The ends with '.com'")
else:
    print("The string does not end with '.com'")
print("position of word 'python' in a sentence using")
s="i am studying python"
position=s.find("python")
print(position)
print("replace the word 'java' with 'python' in a sentence using")
s="I am learning java programming"
new=s.replace("java","python")
print(new)
print("remove extra space")
t="  Hello, Sinthiya   "
c=t.strip()
print(c)
print("capitalize the first letter of a sentence")
x="sinthiya going to market"
y=x.capitalize()
print(y)
print("split a sentence")
r="i am drink a water"
w=r.split()
print(w)
print("join a list of word")
x=['i', 'am', 'drink', 'a', 'water']
y=' '.join(x)
print(y)
print("string has only alphabetic")
sen1="sinthiya"
sen2="sinthiya23"
print(sen1.isalpha())
print(sen2.isalpha())
print("string contains only numeric")
t1="12345"
t2="12345sin"
print(t1.isdigit())
print(t2.isdigit())
print("string has both letter and number")
a="python123"
b="python "
c="1234!"
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print("string are in lowercase")
x="Hi Thiya"
if x.islower():
    print("all characters are lowercase")
else:
    print("not all characters are lowercase")
print("string are in uppercase")
y="hi thiya"
if y.isupper():
    print("all characters are uppercase")
else:
    print("not all characters are uppercase")
print("swpe lowercase to upppercase")
s="hello mom"
t=s.swapcase()
print(t)
print("first letter to uppercase")
d="hello world, this is python"
t=d.title()
print(t)
print("string contains only spaces")
r=" "
is_only_space=r.isspace()
print(is_only_space)
print("number of vowels in a given string")
text="sathiya kannan"
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1
print("number of vowels:",count)
print("email and check if it ends with '@gmail.com'")
email=input("enter your email")
if email.endswith("@gmail.com"):
    print("the email is a gmail address")
else:
    print("the email is not a gmail address")
print("reverse a given string without using slicing")
i=input("enter a string:")
reversedstring="".join(reversed(i))
print("reversed string:",reversedstring)      
      
