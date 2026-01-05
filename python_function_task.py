"Find key"
def find_key(search_key, **kwargs):
    if search_key in kwargs:
        print("Key found:", search_key)
    else:
        print("Key not found")

find_key("name", name="thiya", age=23, Qualification="BBA")
"Find value"
def find_key(search_key,**kwargs):
    if search_key in kwargs:
        print("value found:",search_key)
    else:
        print("value not found")
find_key("age",name="thiya",age=23,Qualification="BBA")
"Sum of number"
def total(*n):
    print(sum(n))
total(1,2,3,4,5)
"Even number"
def even_num(*n):
    for num in n:
        if num % 2==0:
            print(num)
even_num(10,24,51,69,85)
"Perfect number"
def n(*args):
    num = args[0]
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
n(75)
"Remove"
def sample(**kwargs):
    if kwargs:
        kwargs.popitem()
        print(kwargs)
    else:
        print("Dictionary is empty")
sample(name="thiya",age=23,Qualifiation="BBA")
"Calculator number"
def sample(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    if b != 0:
        print("Division =", a / b)
    else:
        print("Division not possible")
sample(78,3)
"Palindrome"
s = input("Enter a string: ")
s = s.lower()
rev = s[::-1]
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
"vowel"
def count_chars(s):
    vowels = 0
    consonants = 0
    special = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        else:
            special += 1
    return vowels, consonants, special
v, c, sp = count_chars("Hello World!123")
print("Vowels:", v)
print("Consonants:", c)
print("Special characters:", sp)
