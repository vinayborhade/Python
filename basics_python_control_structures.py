"""
#Created on Fri Oct 19 19:46:28 2018

#@author: Vinay Borhade
"""
    
age = 10

if age > 13:
    print('inside if block')
    print('you are a teenager')

elif age > 18:
    print('inside elif block')
    print('you are a adult')
    
elif age > 60:
    print('inside elif block')
    print('you are a senior citizen')
    
else:
    print('inside else block')
    print('grow up kid!')

    
age = 36
gender = "Female"

if age >= 18 and age <= 35:
    print('you are eligible')
else:
    print('try in next life!')
    
    
if age >= 18:
    if gender == "Female":
        print("Entry FREE!!")
        
if age >= 18 and gender == "Female":
        print("Entry FREE!!")
        
# ***** Control Structures *****

# if-else
age = 55
time = 20


age_valid = True

# check if age is integer and non zero
if type(age) != int:
    age_valid = False
    print("age invalid")
elif age == 0:
    age_valid = False
    print("age invalid")

    
pub_open = True  

# chdeck if time is more than 11 am and less than 11 pm
if time <= 11 or time >= 23:
    pub_open = False
    print("Pub is closed")
else:
    print("Welcome! Pub is open now")
    
# chdeck if pub is open and age is valid input
if pub_open and age_valid:
    # check if age is less than 19
    if age <= 18:
        print('age under limit')   
        print('you cannot enter')
    elif age > 50:
        print('age over limit')
    elif age > 18 and age <=50:
         print('allowed')
    else:
        print('In correct input')
else:
    print("Sorry..")
        
# get price from user and convert it into a float:
price = 9
s = None
if price < 10:
    s = "That’s cheap, buy a lot!"
elif price < 30:
    s = "Okay, buy a few"
elif price < 40:
    s = "Okay, buy a few"
else:
    s = "Too much, buy somethng else"
print(s)


# get price from user and convert it into a float:
model = "S"

if model == 'SU':
   print("Welcome to ML world..")
   print('runUnSupervisedModel')
else:
   print("Choice Invalid")
   print("Give correct Choice")


# Class average program with counter-controlled repetition.

total = 0          # sum of grades
gradeCounter = 1   # number of grades entered
grades = ["98", 70, 77, 81, 100, 96, 69, 75, 83, 83]
error = False

# processing phase
while gradeCounter <= len(grades) and not error:               # loop 10 times
    grade = grades[gradeCounter-1] # get one grade
    
    #grade = int( grade )
    try:
        if grade <= 100:
            print(gradeCounter)
        else:
            error = True
            print('Grade cannot be greater than 100')
        
        total = total + grade
        
        
    except TypeError:
        print('Grade should be an integer')            
        error = True
        
    finally:
        gradeCounter = gradeCounter + 1
        
# termination phase
if not error:
    average = total / 10          # integer division
    print("Class average is", round(average))

####################
# Counter-controlled repetition with the
# for structure and range function.
grades = [98, 70, 77, 81, 101, 96, 69, 75, 83, 83]
for index in range( len(grades)-1 ):
    
    if(grades[index] > 100):
        print('Marks cannot be greater than 100')
        continue
    else:
        print(grades[index])
        
    
for index in range( len(grades)-1, 1, -1 ):
    if(grades[index] > 100):
        print('Marks cannot be greater than 100')
        continue
    else:
        print(grades[index])

print(list(range( len(grades)-1, 1, -1 )))

total = 0
grades = [98, 76, 77, 81, 100, 96, 69, 75, 83, 83]
for marks in grades:
    total += marks

average = total / 10          # integer division
print("Class average is", round(average))

####################
# interest.py
# Calculating compound interest.

principal = 1000.0   # starting principal
rate = .05           # interest rate

print("Year %21s" % "Amount on deposit")

for year in range( 1, 11 ):
    amount = principal * ( 1.0 + rate ) ** year
    print("%4d%21.2f" % ( year, amount ))
    
####################


check_uptp_num = 100

prime_num = []

for check_num in range(2, check_uptp_num+1):
    
    is_prime = True
    
    for divisor in range(2, check_num):
        #print("Dividing by - " + str(divisor))
        if check_num % divisor == 0:
            is_prime = False
            break
            
    if is_prime:
        prime_num.append(check_num)
    
    
print(prime_num)
####################

# break and continue
for x in range( 1, 11 ):
    if x == 5: 
        continue # skip next statement when x == 5, but continue the looping
    
    if x == 8:
        break # break loop and stop iteration when x == 10
    
    print(x)

####################

l = [1,2,3,4,5,34,56,35,7]
l[0]
l[1]

for ind in [0,1,2,3,4,5,6,7,8]:
    l[ind]
    
for ind in range(0,9):
    l[ind]
    
for val in l:
    print(val)


print(list(range(101)))

print([num for num in range(101) if num % 2 == 0 ])
    
    
print([num for num in range(101) if num % 2 != 0 ])

marks = [90,89,56,67,29,49]
fail = []
for mark in marks:
    if mark < 35:
        fail.append(mark)

fail = [mark for mark in marks if mark < 35]


######################
resume = "Have experience of 4 years in Data Science"

r = resume.split()

exlude_words = ['of', 'in']

new_r = [word for word in r if word not in exlude_words]

print(list(new_r))

match = ['Business', 'Analysts']
new_r = [word for word in r if word in match]
print(list(new_r))


students = ['Vinay', 'Deepika', 'Gaurav', 'Manish', 'Komal', 'Sanket']
absent = ['Sanket', 'Komal']

final_l = []

for s in students:
    if s not in absent:
        final_l.append(s)


final_l = (s for s in students if s not in absent)
    
    
###

my_dict = {
       
       'B1' : {
               'Topic': 'Python',
               'Std_Cnt' : 3,
               'Start_Date' : '29-June-2020',
               'End_Date' : None,
               'Days' : 'Mon-Fri',
               'Time' : '18-20 IST',
               'Status' : 'Ongoing',
               'students' : ['Vinay', 'Deepika', 'Gaurav', 'Manish', 'Komal', 'Sanket']
               },
        'B2' : {
               'Topic': 'R',
               'Std_Cnt' : 4,
               'Start_Date' : '1-June-2020',
               'End_Date' : '30-June-2020',
               'Days' : 'Sat-Sun',
               'Time' : '13-15 IST',
               'Status' : 'Completed',
               'students' : ['Deepika', 'Gaurav', 'Manish', 'Komal', ]
               },
        'B3' : {
               'Topic': 'Data Science',
               'Std_Cnt' : 3,
               'Start_Date' : '29-June-2020',
               'End_Date' : None,
               'Days' : 'Sat-Sun',
               'Time' : '18-20 IST',
               'Status' : 'Ongoing',
               'students' : ['Deepika', 'Gaurav', 'Manish',]
               },
       }
    
students = ['Vinay', 'Deepika', 'Gaurav', 'Manish', 'Komal', 'Sanket']    
for v in students:
    if v ==  'Gaurav':
        
students = []
        
for batch_id, batch_details in my_dict.items():
    if batch_details['Status'] == 'Ongoing':
        print(batch_id)
        print(batch_details['Days'])
        print(batch_details['Time'])
        
        students.append(batch_details['students'])
        
common_stud = []
for stud in students[0]:
    if stud in students[1]:
        common_stud.append(stud)
        
s1 = set(students[0])

s2 = set(students[1])

s1.intersection(s2)       

set(students[0]).intersection(set(students[1]))             




cart = {
        
        'id' : "Hypercity",
        
        "dairy" :  {
                    "milk" : {
                               "normal" : 40,
                               "fat" : 45,
                               "creamy" : 50
                               },
                    "yoghurt": {
                                "sour" : 40,
                                "sweet": 45
                                }
                    },
        "whole_grain" : {
                         "Wheat" : 40,
                         "Bajra" : 30,
                         "Ragi" : 56
                        },
        "egg":{
                    "one" : "60/doz",
                    "two" : "70/doz",
                    "three" : "80/doz"
            },
        "misc":{
                "soft_drink":  {
                                "cola":2,
                                "fanta":1
                                },
                "juice": {"mango": "500 ml",
                          "pineapple" : "1l"
                          }
                },
       }

for k , v in cart.items():
    if type(v) == dict:
        if v.get("one") != None:
            if type(v.get("one")) == int and v.get("one") > 50:
                print(v.get("one"))
                print(k)
            else:
                print("value to compare is not a integer type")
        

