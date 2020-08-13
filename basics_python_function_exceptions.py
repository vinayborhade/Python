# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:18:06 2018

@author: Vinay Borhade
"""

def function_name(arg1, arg2):
    #logic
    return()


def add(n1=1, n2=2):
    out = n1 + n2
    return(out)
    
o = add(1, 2)
add(n2=2, n1=4)

add(n2=2)
    
#**********************************************************

#MAndatory VS Default

#mandatory param (positional)
def mandatory(arg1, arg2):
    print(arg1, arg2)

mandatory() # gives error

mandatory(1) # gives error

mandatory(1, 2)

mandatory(arg2=4, arg1=2)

#default params

def default(arg1=1, arg2=2):
    print(arg1, arg2)
    
default()
default(2)
default(2,4)
default(4,2)
default(arg1=2,arg2=4)
default(arg2=4, arg1=2)

def mixed(arg1, arg2=1):
    print(arg1, arg2)

 ######################################################   
# default parameter
def add(n1, n2):
    result = n1 + n2
    return(result)

def sub(n1,n2):
    result = n1 - n2
    return(result)

def mul(n1,n2):
    result = n1 * n2
    return(result)

def div(n1,n2):
    result = n1 / n2
    return(result)
    
def calc(n1, n2, choice="ADD"):
    result = None
    if choice == 'ADD':
        result = add(n1,n2)
    elif choice == 'SUB':
        result = sub(n1,n2)
    elif choice == 'MUL':
        result = mul(n1,n2)
    elif choice == 'DIV':
        result = div(n1,n2)
    else:
        print("Invalid choice")
        
    return (result)
    
c = calc(1, 2)
if c:
    print("Output - ", c)    
    
######################################################
def check_train_availability(no_of_tickets, date):
    
    available = False
    
    print('Checking Train Availability')
    
    # available variable will be overriden with True if tickets are available
    
    return available
    
def check_flight_availability(no_of_tickets, date):
    
    available = False
    
    print('Checking Flight Availability')
    
    # available variable will be overriden with True if tickets are available
    
    return available

def augmented_reservation(no_of_tickets, date, start="Mum", end="Del", mode="train"):
    
    print(start)
    print(end)
    print(date)
    
    if mode == 'train':
        is_available = check_train_availability(no_of_tickets, date)
    
    elif mode == 'flight':
        is_available = check_flight_availability(no_of_tickets, date)
        
    else:
        print("Inalid mode")
        
    if is_available:
        print("Yes tickets are available")
    else:
        print("Tickets not available, try different date")

        
augmented_reservation(2, "31 July", mode="flight", end="Bangalore")

    
##############################################################################    

def func(mandatory, default=0, *extra_args, **kwargs):
    pass

#packing

def add(a, *b):
    print(b)
    for i in b:
        a = a + i

    return(a)

s1 = 9000

t = [100, 200, 40, 30]
    
r = add(s1, *t)
print(r)

def calc(arg, mode=1, *n1):
    print(n1)
    out = 0
    if(mode == 1):
        for v in n1:
            out += v
    elif(mode == 2):
        out = 1
        for v in n1:
            out *= v
    else:
        out = None
        
    return(out)


def calc1(arg, mode=1, *n1):
    print(arg)
    print(mode)
    print(n1)
    
calc1(2,1,3,4,5)
    
        
calc(10,2)

#**********************************************************

def variable_no_args(arg1=0, *extra_args):
    print(arg1)
    print(extra_args)

variable_no_args(1)


t = (1,2,3)
variable_no_args(2, 3, 4, t)

ls = [1,2,3,4]
variable_no_args(1, ls, t)

l = [1,2,3,4]
variable_no_args(l)
variable_no_args(t, l)
variable_no_args(t, *l)
variable_no_args(t,1,2,3,4)

print(*(1,2,3))

def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    print(x)
    print(l)
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))

l = [23,34,56,75,78,49,6]
l2 = [23,34,56,75,78,49,6]
l3 = [23,34,56,75,78,49,6]
    
arithmetic_mean(10, *l2)


arithmetic_mean(10, *l, *l2, *l3)
arithmetic_mean(1,2,*l)

l1 = [23,34,56,75,78,49,6]
arithmetic_mean(l1) # gives error as first param is considered as string

arithmetic_mean(*l1) # list broken as extra args

def keyword_args(d=0, **kwargs):
    print(d)
    print(kwargs)
    
keyword_args(1, de="German",en="English",fr="French")

d = {'de': 'German', 'en': 'English', 'fr': 'French'}
keyword_args(5, **d)

keyword_args("Two"="2")

d1 = dict(de = 'German')
d1['en'] = 'English'
d1['eng'] = 'English1'

keyword_args(d, **d1)

def combined(pos_arg,  pos_arg2=None, pos_arg3=None, *extra_arg, **keyword_arg):
    print(pos_arg)
    print(pos_arg2)
    print(pos_arg3)
    print(extra_arg)
    print(keyword_arg)
    

a = 1

t = (2,3,4,5)

print(**t)

d1 = {'5': 'five', '6': 'six'}

d2 = {'7': 'seven'}

combined(a, 1, 2, *t, **d1) # extra_arg1, keyword_arg1 passed as extra args

combined(pos_arg1, *extra_arg1, keyword_arg1) #same as above

combined(pos_arg1, extra_arg1, **keyword_arg1) 

combined(pos_arg1,**keyword_arg1, *extra_arg1 ) 

combined(pos_arg1, *extra_arg1, **keyword_arg1) 

combined(1, **keyword_arg1, **keyword_arg2)# observe subtle diff between this an dabove statement


def adder(*x):
    print(x)
    sum = 0
    for val in x:
        sum += val
    print(sum)
    
l = [2,3,4,5,6,7,8]
adder(1,2,3,4,5,*l)

def details(**data):
    for k, v in data.items():
        print("{} = {}".format(k ,v))

        
d1 = {"Name":"Vinay", "LastName":"Borhade" }

d2 = {"age" : 35, "gender" : "M"}

details(**d1, **d2)
        
details(Name="Vinay", LastName="Borhade")

details(Name="Vinay", LastName="Borhade", age=35, gender="M")

def recurse(k):
    if(k > 0):
        result = k + recurse(k-1)
        print(result)
    else:
        result = 0
    return(result)
    
recurse(3)

def fibo(n):
    if(n <= 1):
        return(n)
    else:
        return(fibo(n-1) + fibo(n-2))

terms = 20
for i in range(terms):
    fibo(i)
    
def check_prime(n, divisor=None):
    if divisor is None:
        divisor = n - 1
        
    while(divisor >= 2):
        if(n % divisor) == 0:
            return(False) #break
        else:
            return(check_prime(n, divisor-1))
    else:
        return(True)

for i in range(1, 101):
    if(check_prime(i)):
        print("{} is prime".format(i))
        
#**********************************************************
#LAMDA / INLINE FUNCTIONS
add = lambda x, y: print (x+y) 
mydoubler1 = lambda a : print(a * 2)
mytripler1 = lambda a : print(a * 3)

def add1(x, y) :
    print(x+y)
    return

add(1,2)

add1(1,2)

def multiplier(n):
    
  return lambda a : a * n

mydoubler = multiplier(2)
print(mydoubler(11))

mytripler = multiplier(3)
print(mytripler(11))

#**********************************************************

from functools import partial

def power(p, x):
    print(p, x)
    return x ** p
    
print(power(2, 10))
    
# create a new function that squares
square = partial(power, 2)
# create a new function that squares
cube = partial(power, 3)

print(square(4))
print(cube(5))
#**********************************************************

x1 = 5
x2 = "0"

if x2 == 0:
    print('you cannot divide by zero')
elif type(x2) != int:
    print('you cannot divide by zero')
elif type(x1) != int:
    print('numerator cannot by zero')

l = [12,14,13,56,34,67,89,"vinay", "14", ""]   
div = 0


try:
    for i in l:
        print(i / div)
    print('Hi')
except ZeroDivisionError:
    print('you cannot divide by zero')
except TypeError:
    print('input should be a number')
finally:
    None
    #close connection
    #log entry

#Exceptions

class MyError(Exception):
    #Base class for exceptions in this module.
    pass


def divide(x, y):
    try:
        
        if (x ==0 and y == 0):
            raise MyError
               
        result = x / y
        print("result is", result)
        
    except MyError:
       print("Are you nuts!")
    except ZeroDivisionError:
        print("**Invalid Denom** - division by zero!")
    except TypeError:
        result = int(x) / int(y)
        print("result is", result)
    except Exception:
        print("Unknown error")
        
    finally:
        
        print("executing finally clause")

def add(x, y):

    result = x + y
    print("result is", result)

def main():
    x=2
    y=0
    
    divide(x, y)
    add(x, y)
    
    print('Multiplication Result - ', x*y)         
        
main()    
    
divide(2, 1)

divide(2, 0)

divide("4", "2")

divide(0, 0)


def simple_interest(P, N, R):
    try:
        if(P==0 or N==0 or R==0):
            raise Exception
        else:
            return(P*N*R)
    except Exception:
        print('input cannot be zero')        
    
a = [[1000000, 5, .1], [1000000, 0, .1], [1000000, 5, .09]]

for sce in a:
    si = simple_interest(sce[0], sce[1], sce[2])
    print("{}*{}*{} = {}".format(sce[0], sce[1], sce[2], si))
#**********************************************************


#**********************************************************

#PASS BY REFERENCE VS PASS_BY_VALUE

#Function definition is here
def changeMe( mylist1 ):
    "This changes a passes list into this function"
    mylist1.append( [1,2,3,4])
    print("Values inside the function:", mylist1)
    return

#Now you can call changeme function
mylist = [10,20,30]
changeMe( mylist ) #PASS BY REFERENCE
print("Values outside the function:", mylist)

mylist = [10,20,30]
changeMe( mylist[:] ) #PASS_BY_VALUE
print("Values outside the function:", mylist)

mylist = [10,20,30]


# Function to traverse through a N-Level Dictiionary
# Uses Generator Function

def traverse(value, key=None):
    if isinstance(value, dict):
        print("Iterating dict for item - ", key)
        for k, v in value.items():
            yield from traverse(v, k)
    else:
        yield key, value
        
for k, v in traverse(cart):
    print(k,  v)