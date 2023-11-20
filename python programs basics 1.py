#Write a program to print all even numbers that fall between two numbers (both numbers exclusive)
#entered from the user using while loop.

n1 = int(input(print("What is the first limit of the even number list?")))
n2 = int(input(print("What is the last limit of the even number list?")))

i = n1

while i <= n2:
    if i % 2 == 0:
        print(i, end = " ")

    i += 1
print()
print("==============================================")

#Write a program to print the first 10 integers and their squares using while loop.

i = 0
while i <= 10:
    iSq = i ** 2
    print(i, "and it's square is", iSq)
    i += 1

print("==============================================")

#Write a program to find the factorial of a number input by the user.


n1 = int(input("Enter the number whose factorial shall be calculated: "))
prd = 1
actN1 = n1
while n1 != 0:
    prd *= n1
    n1 -= 1

print(f"The factorial of {actN1} is {prd}")
print("==============================================")

#Write a program to generate the Fibonacci series for n terms, n being an integer read from the user

n = int(input(print("What is the required number of terms for the Fibanocci Series?")))
n1 = 0
n2 = 1
nSum = 0
if n < 0:
    print("Please enter a positive integer.")
    
elif n == 0:
    print("The number of terms cannot be 0.")
elif n == 1:
    print(n1)
elif n > 1:
    print(n1)
    print(n2)
    n -= 2
    while n != 0:
        nSum = n2 + n1
        n1 = n2
        n2 = nSum
        print(nSum)
        n -= 1
print("==============================================")
#Write a program to check whether a number is prime or not.

n = int(input(print("What number should be confirmed whether prime or not? ")))
isPrime = False
for i in range(2, n//2):
    if n % i == 0:
         isPrime = False
         break
    isPrime = True

    
if isPrime == True:
    print(f"{n} is prime!")
elif isPrime == False:
    print(f"{n} is not prime!")

#Write a program to reverse the number accepted from the user.
n = int(input("Input the number to be reversed: ")) #123 = 100 + 20 + 3, 123//10 = 3, 123//100 - 123//10 = 20, 
i = 0
digits = []
while n > 1: #to give the number of digits #ex 988
    i += 1
    digits.append(int(n%10)) #8, 8.8, 9.88
    n = n / 10 #98.8, 9.88, 0.988

#print("digits: ", digits)

for j in range(0, i):
    print(digits[j], end = "")
print()
print("==============================================")

#Write a program to add first n terms of the following series:
#1/1!+1/2!+…….+1/n!

n = int(input(print("What is the last term you'd like to see of the upcoming series?")))
i = 1
j = 0
add = 0
fact = 1
while i <= n:
    j = i
    while j <= i:
        fact *= j
        j += 1
    inverFact = 1/fact
    add += inverFact
    i += 1
print(add)
print("==============================================")

#Write a program to convert Decimal to Binary number.
n = int(input(print("What is the number you'd like to convert to binary? ")))
digitsBin = []
i = 0
j =  0
while n != 0:
    digitsBin.append(n%2)
    n = int(n/2)
    j += 1

for i in range(j, 0, -1):
    print(digitsBin[i-1], end = "")
print("==============================================")
#Write a program to check whether a number is palindrome or not.
actN = int(input("Input a number: ")) #123 = 100 + 20 + 3, 123//10 = 3, 123//100 - 123//10 = 20, 
i = 0
digits = []
n = actN
reversedNum = 0
while n > 1: #to give the number of digits #ex 988
    i += 1
    digits.append(int(n%10)) #8, 8.8, 9.88
    n = n / 10 #98.8, 9.88, 0.988

#print("digits: ", digits)

for j in range(i, 0, -1):
    reversedNum += digits[j-1]*(10**(i-j))
if reversedNum == actN:
    print("ITS A PALINDROME!")
elif reversedNum != actN:
    print("its NOT a palindrome :(")

print("reversed:", reversedNum)
#Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and
#500. (exclusive both numbers)

for i in range(101, 500):
    if i % 13 == 0 and i % 3 != 0:
        print(f"{i} satisfies the requirements. It is a multiple of 13, and not divisible by 3")

#Write a program to find the sum of following series:
#1+2+6+24+120…… until n terms
n = int(input(print("What is the last term you'd like to see of the upcoming series?")))
i = 1
j = 0
add = 0
fact = 1
while i <= n:
    j = i
    while j <= i:
        fact *= j
        j += 1
    add += fact
    i += 1
print(add)
print("==============================================")
#Write a program to find the sum of following series:
#1+ 4- 9 + 16 – 25 + 36 - ……. Until n terms
n = int(input(print("What is the last term you'd like to see of the upcoming series?")))
i = 1
j = 0
add = 0
if n > 0:
    while i <= n:
        if i == 1:
            sqr = 1
            add += 1
            j = 0
            i += 1
        elif i != 1:
            if j % 2 == 0:
                sqr = (i ** 2) * +1
            elif j % 2 != 0:
                sqr = (i ** 2) * -1
            add += sqr
            j += 1
            i += 1
    print(add)

x = int(input(print("Input x: ")))
n = int(input(print("Input the number of terms: ")))
i = 0
cube = 0
division = 0
add = 0
while i < n:
    cube = ((2*i)+1)**3
    #print(cube)
    division = cube/x
    #print(division)
    add += division
    #print(add)
    i += 1

print(f"The sum of the series upto {n} terms, each term divided by {x} is: {add}")


#PATTERNS
'''
1.
* 
* *
* * *
* * * *
* * * * *
'''
rows = 5
for i in range(1, rows+1):
    print("* "*i)


'''
2.
P
Py
Pyt
Pyth
Pytho
Python
'''

string = "Python"
j = 0
for i in range(1, 7):
    for j in range(i):
        print(string[j], end="")
    print()

'''
3.
1 2 3 4 5 
2 3 4 5
3 4 5
4 5
5
'''

i, j, rows = 0, 0, 5
for i in range(1, rows+1):
    for j in range(1, 7-i):
        print(j+i-1, end = " ")
    print()

'''
4.
5 4 3 2 1 
4 3 2 1
3 2 1
2 1
1
'''

i, j, rows = 0, 0, 5
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

'''
5.
1
33
555
7777
99999
'''

i, rows, j = 0, 5, 1
for i in range(1, rows+1):
    print(str(j)*i)
    j += 2

'''
6.
A 
A B
A B C
A B C D
A B C D E
'''

i, j, asciVal, rows = 0, 0, 65, 5
for i in range(1, rows+1):
    for j in range(i):
        print(chr(asciVal+j), end = " ")
    print()

'''
7.
    A 
   A B
  A B C
 A B C D
A B C D E
'''

i, j, asciVal, rows = 0, 0, 65, 5
wSpace = 4
for i in range(1, rows+1):
    print(" "*wSpace, end = "")
    for j in range(i):
        print(chr(asciVal+j), end = " ")
    wSpace -= 1
    print()
    

'''
8.
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
'''

rows = 5
asciVal = 65
i = 0

for i in range(1, rows+1):
    print(chr(64+i)*5)

'''
9.
    * 
   * *
  * * *
 * * * *
* * * * *
'''

wSpace, i, j, rows = 4, 0, 0, 5
for i in range(1, rows+1):
    print(" "*wSpace, end = "")
    wSpace -= 1
    print("* "*i)


'''
9.
         *

       * A *

     * A * A *

   * A * A * A *

 * A * A * A * A *
'''

i = 0
rows = 5
j = 0
z = 0
star = "*"
starA = "* A "
wSpace = 9
for i in range(1, rows+1):
    print(" "*abs(wSpace), end = "")
    print(starA*(i-1), end = "")
    print(star)
    print()
    wSpace -= 2

#1.	Write a program to input three numbers and display the largest of the three.

n = 3
l = []
for i in range(n):
    l.append(int(input(f"Enter number {i}: ")))
print("the largest number is:", max(l))

#2.	Write a program that calculates marks’ sum (5 subjects) and displays percentage & its corresponding grade.
n = 5
marks = []
for i in range(1,n+1):
    marks.append(float(input(f"Marks in subject {i}: ")))

tMarks = sum(marks)
prcnt = (tMarks/500) * 100

print(f"The total marks is, {tMarks}/500. Percentage is {prcnt}.")

grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'E': 50}

for mark in marks:
    for grade in grades.keys():
        if mark > grades[grade] and mark <= grades[grade] + 10:
            print(f"Grade obtained for subject with mark, {mark} is {grade}")

#3.	Write a program to display whether the entered number is positive, negative or zero

a = int(input("Enter number: "))

if a > 0:
    print("negative.")
elif a < 0:
    print("positive.")
else:
    print("zero.")

#4.	Write a Menu driven program to calculate area of circle, rectangle or triangle.
import math as m
shape = input("What shape..?")

if shape.lower().strip() == "circle":
    r = float(input("Radius: "))
    print("area: ", (m.pow(r, 2) * m.pi))
elif shape.lower().strip() == "rectangle":
    l, b = float(input("l: ")), float(input("b: "))
    print("area:", l*b)
elif shape.lower().strip() == "triangle":
    b, h = float(input("b: ")), float(input("h: "))
    print("area:", (0.5*b*h))

#8.	Write a program to generate the following pattern using nested loops

rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print("$", end="")
    print()

#9.	Write a program to find the sum of digits of a number, input by the user

n = str(input("number: "))
s = 0
for digit in n:
    s += int(digit)
print("sum:", s)

#10.	Write a program to produce the given sequence: 	1,-4,7,-10……n

import math as m

n = int(input("end limit: "))

count = 0
i = 1
while count <= abs(n//3):
    print(i, end=" ")

    if count % 2 == 0:
        i = -i
        i -= 3
    else:
        i =abs(i)
        i += 3
    count += 1

#13.	Write a program to read a list of n integers and find their median
import statistics as s


n = int(input("int n: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter number {i}: ")))

print(f"media is: {s.median(l)}")

#14.	Write a program to count the number of times a character occurs in a string.

c = input("character to be searched for: ")

s = input("string: ")
sum  = 0
for a in s:
    if a == c:
        sum += 1

print(f"the number of times '{c}' has occured in '{s}' is {sum}")

#15.	Write a program to replace all vowels in the string with ‘*’

vowels = ['a', 'e', 'i', 'o', 'u']

s = input("string: ")

for c in s: #loop over all characters
    for vowel in vowels: #loop over all vowels
        if c.lower() == vowel: #if c is a vowel
            s = s.replace(c, "*")
            
print(s)

#16.	Write a program to Count and display the number of vowels, consonants, uppercase, lowercase characters in string, entered from the user

vowels = ['a', 'e', 'i', 'o', 'u']

s = input("string: ")

vowelCount = 0
consCount = 0
upCount = 0
lowCount = 0
isVowel = False
for c in s:
    isVowel = False
    print(c)

    if not c.isspace():
        if c.isupper():
            upCount += 1
        else:
            lowCount += 1
        for vowel in vowels:
            if c.lower() == vowel:
                vowelCount += 1
                isVowel = True
                break
        if not isVowel:
            consCount += 1

print("vowelCount", vowelCount)
print("consCount", consCount)
print("lowCount", lowCount)
print("upCount", upCount)

#17.	Write a program to Input a string and convert the case of characters in it.

s = input("string: ")
print(s.swapcase())

#18.	Write a program to find the largest/smallest number in a list/tuple

n = int(input("How many members in the tuple: "))
num = tuple()
for i in range(1, n+1):
    num = num + ((int(input(f"What is number {i}: "))),)

print("smallest number is:", min(num))
print("largest number is:", max(num))

#19.	Write a program to input a list of numbers and swap elements at the even location with the elements at the odd location.

n = int(input("How many members in the list?"))
l = []
for i in range(1,n+1):
    l.append(int(input(f"Enter member {i}: ")))
print("current list:", l)

for i in range(len(l)):
    if i % 2 == 1: #i is odd
        l[i], l[i - 1] = l[i - 1], l[i]
print("new swapped list:", l)

#21.	Write a program to read a list of n integers (positive as well as negative). Create two new lists, one having all positive numbers and the other having all negative numbers from the given list. Print all three lists

n = int(input("How many members in the list?"))
l = []
for i in range(1,n+1):
    l.append(int(input(f"Enter member {i}: ")))
print("current list:", l)
pos = []
neg = []
for element in l:
    if element > 0:
        pos.append(element)
    elif element < 0:
        neg.append(element)

print(l, pos, neg)

#22.	Write a program that asks for the (i) position (ii) value of the element to be deleted from the list and deletes it.

n = int(input("How many members in the list?"))
l = []
for i in range(1,n+1):
    l.append((input(f"Enter member {i}: ")))
print("current list:", l)

pos = int(input("Position of element to be deleted: "))

l.pop(pos)
print(l)
val = input("Value of element to be deleted: ")

l.remove(val)
print(l)

#23.	Write a program to enter names of employees and their salaries as input and store them in a dictionary

db = dict()

n = int(input("How many employees: "))

for i in range(n):
    name = input(f"Name of employee {i+1}: ")
    db[name] = float(input(f"Salary of employee {i+1}: "))
print(db)

#24.	Write a program to create a dictionary with the roll number, name and marks of n students in a class and display  the names of students who have marks above 75.

db = dict()

n = int(input("How many students: "))
tmpList = []
for i in range(n):
    rollNo = int(input(f"Roll number of student {i+1}: "))
    tmpList.append(str(input(f"Name of student {i+1}: ")))
    tmpList.append(float(input(f"Marks obtained by student {i+1}: ")))

    db[rollNo] = tmpList
    tmpList = []
print(db)

for key in db.keys():
    if db[key][1] > 75:
        print(db[key][0], " has marks above 75!")
