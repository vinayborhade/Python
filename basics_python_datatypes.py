# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:44:03 2018
@author: Vinay Borhade
"""
# ***** Primitive Data Structures *****

# Integers
i = 10

i = i + 2

print(i + 2)
print(i - 2)
print(i * 2)
print(i / 2)    
print(i % 2)
print(i ** 2)


# float
f = 1.618

print(f)

print(f + 2)

# boolean
b = True

b = "Hello"

print(b)
print(not b)

a = 3
b = 4

# comaritive operators
print(a == b)
print(a != b)

print(a < b)
print(a > b)

# string
s1 = 'Hello'
s2 = "World"
s3 = "2018"

# string concat
print(s1 + s2 + s3)
print(s1 + ' ' +  s2 + ' ' + s3)
len(s1 + ' ' +  s2 + ' ' + s3)

# functions on string
print(s1.isdigit()) 
print(s3.isdigit())
print(s1.upper())

# Splitting a phrase on BLANK Spaces
s4 = "Few words are not repeated, few words are"
s5 = s4.split()
print(s5)
type(s5)

# ***** Non-Primitive Data Structures *****

# lists

l1 = [1,2,3,4,5]
print(l1)

list2 = ["My", "Name", "is", "Tony", "Stark"]
print(list2)

print(l1 + list2)

l1.append(list2)
print(l1)

fruits = ['apple', 'cherry', 'banana', ]
print(fruits)
fruits.append("orange")
print(fruits)

fruits.append("mango")
print(fruits)

print(fruits[0])
print(fruits[3])
print(fruits[-1])

###slicing
print(fruits[:])
print(fruits[1:])
print(fruits[1:3])

print(min(l1))
print(max(l1))

# list mutable, subscripting

list2[3] = "Ned"
print(list2)

###sorting
print(sorted(fruits))
print(fruits.sort())

print(fruits)

r = range(1, 6)
print(list(r))

r1 = list(r)


alp = ['a', 'b', 'c', 'd', 'e']
print(alp)

z = zip(r1, alp)

z1 = list(z)

#  Object Reference in Python
a = [1, 2, 3]
b = a.copy()

a.append(4)

c = b

b.append(5)

print(b)
print(list(z))


# Tuple
t1 = (1, 2, 3, 4)
t2 = (2, 4, 6, 8)

print(t1 + t2)
print(t1[1]) # slicing same as lists

# tuple immutable
t2[2] = 50

# Dictonaries

        
models = {
"S": 'Supervised', 
"US": 'UnSupervised',
3 : {
     "a" : "ABC",
     "b" : "PQR"
     },
4: [1,2,3],
5: (3,4,5)
}
print(models)

print(models.get(5))

print(models["5"])

models[3] = 'SemiSupervised'
print(models)

models[3] = 'Semi-Supervis  ed'
print(models)

models[4] = 'Yet to come'
print(models)

del models[4] 
print(models)

len(models)

d = {}
d[1] = 'Element 2'
print(d)

d1 = dict()
print(d1)


# Advanced Dict concepts
from collections import defaultdict
 
somedict1 = dict()
print(somedict1[3]) # KeyError

somedict2 = defaultdict(int)
print(somedict2[3]) # print int(), thus 0
print(somedict2)

d_int = defaultdict(int, a=10, b=12, c=13) 
print(d_int)

kwargs = {'a':10,'b':12,'c':13}
d_int2 = defaultdict(int, **kwargs)
print(d_int2)

s4 = "Few words are not repeated, few words are"
s5 = s4.split() 
print(s5)

repeated_word_count = defaultdict(int)
print(repeated_word_count)
for word in s5:
    repeated_word_count[word] += 1

print(repeated_word_count)

print("************Iterate the dictionary************")
for k, v in repeated_word_count.items():
    print(k, v)
    
for k in repeated_word_count.keys():
    print(k)
    
for v in repeated_word_count.values():
    print(v)
     
# Sets
str1 = "Few words are not repeated, few words are"
str2 = "Golden words are not repeated"

print(str1.split())
print(str2.split())

set1 = set(str1.split())
print(set1)

set2 = set(str2.split())
print(set2)

common = set1.intersection(set2)
print(common)

unique = set1.union(set2)
print(unique)

# itertools

from itertools import chain, combinations

ch = chain(r, alp)
print(list(ch))

comb1 = combinations(r, 4)
print(comb1)
print(list(comb1))

l = list(comb1)
type(l)

l[0]

comb2 = combinations(alp,2)
print(list(comb2))



