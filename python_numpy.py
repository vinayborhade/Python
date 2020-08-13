# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:01:46 2019

@author: Vinay Borhade
"""
import numpy as np 
l = [1,2,3]
a = np.array(l) 
print(a)

type(a)
type(l)

print(a.shape)
print(a.ndim)

# more than one dimensions 
l = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
a = np.array(l) 
print(a)

print(a.shape)
print(a.ndim)

# minimum dimensions 
a = np.array([1, 2, 3, 4, 5], ndmin = 2) 
print(a)

print(a.shape)

# this resizes the ndarray 
a = np.array([[1,2,3],[4,5,6]]) 
print(a.shape)
print(a)
a.shape = (3,2) 
print(a)
a.shape = (6,) 
print(a)
################################################
# an array of evenly spaced numbers 
a = np.arange(24) 
print(a)

a.ndim

b = a.reshape(2,3,4)
print(b) 

b = a.reshape(6,2,2)
print(b) 

b = a.reshape(6,4)
print(b) 

a = np.arange(10, 21) 
print(a)

a = np.arange(10, 20, 3) 
print(a)

x = np.linspace(10,20,11, retstep=True)
print(x)

x = np.linspace(0, 1000, 15, retstep=True)
print(x)

x = np.linspace(10,20,7, retstep=True)
print(x)
################################################
x = np.empty([3,2], dtype = int) 
print(x)

x = np.zeros([3,2], dtype = int) 
print(x)

x = np.zeros(5)
print(x)

x = np.zeros((5,), dtype = np.int) 
print(x)

x = np.ones(5)
print(x)

x = np.ones((5,), dtype = int) 
print(x)

x = np.ones((3,2), dtype = int) 
print(x)

################################################
a = np.arange(10,20) 
print(a)

print(a[5])

b= a[3:]
print(b)

s = slice(2,7)
print(a[s])

print(a[2:7])

print(a[slice(2,7)])

s = slice(2,7,2)
print(a[s])

b = a[2:7]
print(b)

b = a[2:7:2]
print(b)

a = np.array([[1,2,3],
              [3,4,5],
              [4,5,6]]) 


print(a[1:])

print(a[...,1]) #ellipses

print(a[1,...])

print(a[...,1:])

print(a[...])

################################################

a = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [12,13, 14, 15]])
b = np.array([[10, 20, 30, 40]])

a.shape
b.shape

a * b
a + b
a / b
a - b
a % b
a // b

################################################

l = [[1,2,3,4], [2,3,4,5]]

for x in l:
    print(x)

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

# using 2 for loops
for x in a:
    for ele in x:
        print(ele)

# using np.nditer and 1 for loop
print('Modified array is:')
for x in np.nditer(a):
   print(x)
   
b = a.T

print(b)
for x in np.nditer(b):
   print(x)


for x in np.nditer(a):
   print(x)

for x in np.nditer(a, order='K'):
   print(x)
   
for x in np.nditer(a, order='C'):
   print(x)
   
for x in np.nditer(a, order='F'):
   print(x)
   
   
################################################   
for x in np.nditer(a): # gives error as array x is readonly
   x[...] = 2*x

for x in np.nditer(a, op_flags=['readwrite']):
   x[...] = 2*x

print(a)
################################################

print(a)

for x in np.nditer(a, flags = ['external_loop'], order='F'):
    print(x)
    
for x in np.nditer(a, flags = ['external_loop'], order='C'):
    print(x)
    
for x in np.nditer(a, order='F'):
    print(x)
    
for x in np.nditer(a, flags = ['external_loop'], order='K'):
    print(x)

for x in np.nditer(a, op_flags=['readwrite'], flags = ['external_loop'], order='F'):
    x[...] = 2*x

print(a)

################################################
a = np.arange(0,60,5)
a = a.reshape(2,2,3)

print(a)

for x in np.nditer(a):
   print(x)
   
for x in np.nditer(a, order='C'):
   print(x)
   
for x in np.nditer(a, order='F'):
   print(x)

for x in np.nditer(a, flags = ['external_loop'], order='F'):
    print(x)
    
for x in np.nditer(a, flags = ['external_loop'], order='C'):
    print(x)

for x in np.nditer(a, op_flags=['readwrite'], flags = ['external_loop'], order='F'):
    x[...] = 2*x

print(a)

a = np.array([  5,  10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110])
a = a.reshape(2,2,3)
################################################
#statistics

print(a.flat[...])

np.amin(a)
np.amax(a)

np.amin(a, axis=0)
np.amax(a, axis=0)

np.amin(a, axis=1)
np.amax(a, axis=1)

np.amin(a, axis=2)
np.amax(a, axis=2)

#calculates range (max - min)
np.ptp(a)
np.ptp(a, axis=0)
np.ptp(a, axis=1)
np.ptp(a, axis=2)

np.percentile(a, 50)
np.percentile(a, 50, axis=1)

np.median(a)
np.mean(a)
np.std(a)
np.var(a)
np.sum(a)

np.sort(a, axis=1)

np.argmax(a)
np.argmin(a)

np.argmax(a, 0)
np.argmin(a, 0)

np.argmax(a, 1)
np.argmin(a, 1)

np.argmax(a, 2)
np.argmin(a, 2)
################################################
np.nonzero(a)

np.where(a>50)

condition = a > 25
np.extract(condition, a)
################################################
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.dot(a, b)
################################################