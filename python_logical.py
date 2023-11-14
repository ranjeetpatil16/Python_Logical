
a=10
b=20
print("a is",a,"and b is",b)
print(a,"is a and",b,"is b")
print("a is",a,b,"is b")

a=10
b=20
print("addition",a+b)
print("division",a/b)
print("float division",a//b)#round down
print("modulus",a%b)#gives remainder
print("power",a**2)

37%130

number=int(input("Enter a number:"))
if number>0:
  print(number,"is positive")
else:
  print(number,"is negative")

number=int(input("Enter a number:"))
if number>0:
  print(number,"is positive")
elif number==0:
  print(number,"is zero")
else:
  print(number,"is negative")
print("coded by Ranjeet Patil")# out of conditional statement

"""Loops

While loop

Counter
"""

i=1 #start
while i<=5: #condition
  print(i)
  i=i+1 #i+=1
print("Out of loop")

"""CountDown"""

i=10
while i>=1:
  print(i)
  i=i-1 #i-=1
print("Out of loop")

i=10
while i>=1:
  print(i)
  i=i-0.5 #float step is allowed is the most important difference between for loop and while loop in python
print("Coded by Ranjeet")

"""For loop

"""

for i in range(1,11,1): #(start,end,range) end should be n-1
  print(i)
print("coded by Ranjeet")

for i in range(10,0,-1): #step size is -1
  print(i)
print("coded by Ranjeet")

a=10
b=20
print(a,b)
a,b=b,a
print(a,b)#swapping the values in python

"""Area of circle"""

radius=float(input("Enter radius of circle:"))
area=3.14*radius**2
print("The area of circle is:",area)

"""Membership operator
in - Returns true if the element is present else false
not in - Returns true if the element is not present else false
"""

a=10
list=[1,2,3,4,5]
if a in list:
  print("True")
else:
  print("False")

a=1
list=[1,2,3,4,5]
if a in list:
  print("True")
else:
  print("False")

a=10
list=[1,2,3,4,5]
if a not in list:
  print("True")
else:
  print("False")

#program for addition,substraction,multiplication and division
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("The sum of two numbers is",num1+num2)
print("The substraction of two numbers is",num1-num2)
print("The multiplication of two numbers is",num1*num2)
print("The division of two numbers is",num1/num2)

unit=int(input("Enter electricity consumption units: "))
charge=5
total=unit*charge
print("Bill for",unit,"units is",total)
print("10% discount is applicable over your bill")
bill=total-(total*0.1)
print("Bill to be pay",bill);

Eng=int(input("Enter English marks: "))
Hindi=int(input("Enter Hindi marks: "))
Sci=int(input("Enter Science marks: "))
His=int(input("Enter History marks: "))
Geo=int(input("Enter Geography marks: "))
total=Eng+Hindi+Sci+Geo+His
print("Total marks got out of 500 is",total)
per=(total*100)/500
print("Congratulation! You got",per,"Percentage")

a=int(input("Enter a number:"));
b=int(input("Enter a number:"))
print("The value of a berfore is",a,"and the value of b before is",b)
a,b=b,a
print("The value of a after is",a,"and the value of b after is",b)

sale=int(input("Enter total sales amount:"))
profit=sale*0.05
print("The profit on sale of",sale,"Rs is Rs",profit)

"""Odd or even"""

number=int(input("Enter a number:"))
if number%2==0:
  print("The number is even")
else:
  print("The number is odd")

"""voting eligibility"""

age=int(input("Enter your age:"))
if age>=18:
  print("You can vote")
else:
  print("You can not vote")

"""Gratest of two numbers"""

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if n1>n2:
  print(n1,"is greater than",n2)
else:
  print(n2,"is greater than",n1)

"""Greatest of three numbers"""

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1>n2 and n1>n3:
  print(n1,"is greatest")
elif n2>n1 and n2>n3:
  print(n2,"is greatest")
else:
  print(n3,"is greatest")

i=1
while i<=10:
  print(i)
  i+=1
print("Numbers from one to ten")

#printing n natural numbers
num=int(input("Enter a number"))
i=1
while i<=num:
  print(i)
  i+=1
print("Printing of N natural numbers")

#printing N natural numbers in reverse order
num=int(input("Enter number"))
i=num
while i<=num:
  print(i)
  i-=1
  if i==0:
    break
print("Reverse order")

n=int(input("Enter a number:"))
while n>=1:
  print(n)
  n-=1
print("coded in reverse order")

n=int(input("Enter a number:"))
sum=0
i=1
while i<=n:
  sum+=i
  i+=1
  print(sum)
print("sum of n natural numbers")

n=int(input("Enter a number:"))
sum=0
i=1
while i<=n:
  sum=sum+(i*i)
  print(sum)
  i+=1
print("The sum of square of n natural numbers")

n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
  sum+=(i*i*i)
  print(sum)
  i+=1
print("Sum of cube of n natural numbers")

n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
  if i%2==0:
    sum=sum+i
  i=i+1
print("The sum of even natural numbers is",sum)

n=int(input("Enter number who's numbers digit to be calculated: "))
sum=0
while n>0:
  sum=sum+n%10 #gives remainder for addition
  n=n//10 #Seperated 10th decimal place
print("Sum of digit of given number is",sum)

num=int(input("Enter a number:"))
sum=0
while num>0:
  sum=sum+(num%10)*(num%10)
  num=num//10
print("The sum of square of digit of numbers is",sum)

num=int(input("Enter a number:"))
sum=0
while num>0:
  sum=sum+(num%10)*(num%10)*(num%10)
  num=num//10
print("The sum of square of digit of numbers is",sum)

"""Armstrong Number"""

num1=int(input("Enter a number: "))
sum=0
num2=num1
power=len(str(num2))
while num1>0:
  sum=sum+(num1%10)**power
  num1= num1//10
if num2==sum:
    print(num2,"is armstrong number")
else:
    print(num2,"is not armstrong number")

"""Product of each digit in number"""

n=int(input("Enter a digit: "))
pro=1
num=n
while n>0:
  pro=pro*(n%10)
  n=n//10
print(pro)

"""Prime Number"""

n=int(input("Enter a number: "))
count=0
for i in range(2,n):
  if n%i==0:
      count+=1
if count==0:
    print("The number prime")
else:
    print("The number is not prime")

n=int(input("Enter a number: "))
pro=1
num=n
while n>0:
  pro=pro*(n%10)
  n=n//10
print(pro)

"""Palindrome Number"""

n=int(input("Enter a number:"))
rev=0
x=n
while n>0:
  rev=(rev*10)+n%10
  n=n//10
if x==rev:
  print(x,"is palindrome")
else:
  print(x,"is not palindrome")

"""Factorial Of Number"""

n=int(input("Enter a number: "))
fact=1
copy=n
while n>0:
  fact=fact*n
  n=n-1
print("factorial of ",copy," is",fact)

"""Fibonacci Series"""

n=int(input("Enter a number: "))
a=0
b=1
c=0
while c<=n:
  print(c)
  a=b
  b=c
  c=a+b

"""Prime numbers within a range"""

lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))
for num in range(lower,upper+1):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
    else:
      print(num,end=" ")

"""Nth prime number"""

n = int(input("Enter the value of n: "))

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
number = 2

while True:
    if is_prime(number):
        count += 1
        if count == n:
            print(f"The {n}-th prime number is: {number}")
            break
    number += 1

"""List Assignment"""

list=[24,30,45,34,23]
print("The maximum temperature is:",max(list))

list1=[['soap',10],['colgate',20],['brush',20],['towel',50]]
sum=0
for i in list1:
  sum=sum+i[1]
print(sum)

sp=[100,112,134,123,111]
a=sp[0]
b=sp[-1]
per=((b-a)*100)/a
print(per,"%")

age=[['ranjeet',23],['shubham',26],['rohit',22],['tito',23]]
list=[]
for i in age:
  list.append(i[1])
print(max(list))

list=["hello world","work hard play hard"]
for item in list:
  print(item,"No of Words: ",len(item.split()))

email=["ranjeet.com@gmail","tito@gmail.com","shubh@gmail.org"]
list=[]
for item in email:
  if item[-4:]==".com":
    list.append(item)
print(list)

a = [2, 2, 4, 5, 6, 7, 4, 2, 5, 8, 2]

element_counts = {element: a.count(element) for element in set(a)}

sorted_elements = sorted(a, key=lambda element: element_counts[element])

print(sorted_elements)

list="Ranjeet Patil"
list1=list.split()
list1[::-1]

