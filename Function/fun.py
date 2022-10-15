# FUNCTION : It is a special block of code which is defined to perform a specific task.
# 1) Function Returning value :-

#Example-1 :-
'''
from math import *
t=(10,20,30)
x=sum(t)
print("x = ",x)

y=100+sqrt(81)
print("y = ",y)
#end of __main__


#Example-2 :-

def square(n):
    sq=n**2
    return(sq)
#end of def function

#__main__
x=square(5)
print("x = ",x)

y=x*2
print("y = ",y)
#end of __main__


# Example-3 : design two function volumn() and surfaceArea() of a box, which will calculate and print the result when L & B & H of a box() are passed as argument.

def volume(L,B,H):
    v=L*B*H
    return(v)
#end of volume function

def surfaceArea(L,B,H):
    s=2*(L*B + B*H + H*L)
    return(s)
#end of surfaceArea function

#__main__
V=volume(5,6,7)
print("Volumn Of Box = ",V)
S=surfaceArea(5,6,7)
print("SurfaceArea Of Box = ",S)
#end of __main__


# Example-4 :- design two function area() and circumference() of a circle, which will calculate and return the result when L & B of a rectangle are passed as argument.


def area(r):
    A=3.14*r*r
    return(A)
#end of area() function

def circumference(r):
    C=2*3.14+r
    return(C)
#end of perimeter() function


#__main__
A=area(5)
print("Area Of Rectangle = ",A)
C=circumference(5)
print("Circumference Of Rectangle = ",C)
#end of __main__



# 2) Function NOT Returning value :-

#Example-1 :-

from turtle import *
#__main__
t=Turtle()
t.shape("turtle")
t.speed(2)
t.color("blue")
t.fillcolor("yellow")
t.begin_fill()

for i in range(1,5):
    t.forward(10)
    t.right(10)
#end of loop
t.end_fill()
done()
#end of __main__


Example-2 :-

def square(n):
    sq=n**2
    print("Square root of %d is %d " %(n,sq))
#end of square function

#__main__
square(9)
#end of __main__


# Example-3 :- design two function volume() and surfacearea() of a box & calculate() and print the result.

def volume(L,B,H):
    v=L*B*H
    print("Volume = ",v)
#end of volume function

def surfaceArea(L,B,H):
    s=2*(L*B + B*H + H*L)
    print("Surface Area = ",s)
#end of surfaceArea function

#__main__
L,B,H=5,6,7
volume(L,B,H)
surfaceArea(L,B,H)
#end of __main__


# Example-4 :- design two function area() and perimeter() of a rectangle which will print the result when L & Bof a rectangle are passed as argument.


def area(l,b):
    A=l*b
    print("Area Of Rectangle : ",A)
#end of area() function

def perimeter(l,b):
    P=2*(l+b)
    print("Perimeter = ",P)
#end of perimeter() function


#__main__
area(5,6)
perimeter(2,3)
#end of __main__


# Example-5 :- design two function area() and circumference() of a circle, which will calculate and print the result when L & B of a rectangle are passed as argument.


def area(r):
    A=3.14*r*r
    print("Area Of Rectangle : ",A)
#end of area() function

def circumference(r):
    C=2*3.14+r
    print("circumferenceter = ",C)
#end of perimeter() function


#__main__
area(5)
circumference(5)
#end of __main__



# User-Defined Function :-

def stars(n):
    for i in range(1,n+1):
        print("*",end=" ")
    #end of loop
    print()
#end of stars

#__main__
print("Compilers")
stars(10)
print("Rajapeth")
stars(20)
print("Amravati")
stars(30)
#end of __main__




# Function with default(ie. optioal) argument

def addition(a,b,c=0,d=0):
    return(a+b+c+d)
#end of addition function

#__main__
x=addition(10,20,30,40)
print("sum = ",x)

y=addition(50,60,70)
print("sum 2 = ",y)

z=addition(80,90)
print("sum 3 = ",z)
#end of __main__


#Calling function by using keyword argument

def displayName(first_name,last_name):
    print("\nFirst Name = ",first_name)
    print("Last Name = ",last_name)
#end of displayName function


#__main__

#both are positional argument
displayName("VRUSHALI" ,"SIRSATH")

#both are keyword argument
displayName(last_name="sirsath",first_name="vrushali")

#first is positional and second is keyword argument
displayName("Vrushali",last_name="Sirsath")

#end of __main__



#Double Asterisk in function call

def displayname(first_name,last_name):
    print("\nFirst Name = ",first_name)
    print("Last Name = ",last_name)
#end of displayName function

#__main__
d={"last_name":"Sirsath" , "first_name":"Vrushali"}
displayname(**d)
#end of __main__




#Function with arbitrary argument/(any number of argument) :-

# Example-Design a function addition which will return sum of some number which will passed as argument.
def add(*arg):
    print("\n DataType Of args = ",type(arg))
    print("arg = ",arg)
    s=0
    for i in arg:
        s=s+i
    #end of loop
    return s
#end of add function

#__main__
x=add(10,20,30)
print("x = ",x)

y=add(1.1,2.2)
print("y = ",y)

z=add(10,33,45,89,52)
print("z = ",z)
#end of __main__



#function with positional and arbitrary argument.
# Example 1) :-
def display(a,*p):
    print("a = ",a)
    print("p = ",p)
#end of display

#__main__
display(10,20,30,40)
#end of __main__

# Example 2) :-

def display(a,*p,b):
    print("a = ",a)
    print("b = ",b)
    print("p = ",p)
#end of display

#__main__
display(10,20,30,b=40)
#end of __main__


# Example 2) :-

def display(a,*p,b=0):
    print("\na = ",a)
    print("b = ",b)
    print("p = ",p)
#end of display

#__main__
display(10,20,30,b=40)
display(10,20,30)
#end of __main__



#Recursive Function :- Function call itself is called Recursive Function.

# Example :- Define a Recursive function fact() which will return factorial of the number which is passed as argument.

def fact(n):
    if n==1:
        return(1)
    else:
        return(n*fact(n-1))
#end of fact function

#__main__
x=fact(5)
print("Factorial = ",x)
#end of __main__


# Defining a function inside a function / closure.

# Example :- Design a function mean() which will return average of 3 numbers.

def mean(a,b,c):
    def add(p,q,r):
        return(p+q+r)
    #end of add function

    m=add(a,b,c)/3.0
    return m
#end of mean fun

#__main__
x=mean(5,6,8)
print("Mean = ",x)
#end of __main__


# Returning Multiple value from a function

def sum_mean(a,b,c):
    s=a+b+c
    m=s/3
    t=(s,m)
    return t
#end of sum_mean function

#__main__
x=sum_mean(5,6,8)
print("x = ",x)
print("Sum = ",x[0])
print("Mean = ",x[1])
#end of __main__

'''


# Lamda Function / Anonymous Function :- function without name is called lamda function.

# Example :- design a lamda function with name cube which name cube which only return cube of given number.

#__main__
cube=lambda n:n**3

x=cube(2)
print("x = ",x)
#end of __main__






