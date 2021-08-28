#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#b.enter details amjad,28,male
name=str(input("enter your name:"))
age=float(input("enter your age:"))
gender=str(input("enter your gender:"))
if name=="":
    print("Name:",name)
    print("yes that's my name")
    if age=='0':
        print("Age:",age)
    if age <=18:
         print("My age is {} major")
    else:
         print("My age is {} minor")
    if gender=="male":
        print("gender:",gender)
        print("i am a male.",'\n')


# In[ ]:


#b.enter details amjad,28,male
name=str(input("enter your name:"))
age = float(input("enter your age:"))
gender=str(input("enter your gender:"))
if name:
    print("name:",name)
    print("yes its my name '{}' ".format(name.capitalize()))
if age:
    if age >= 18:
        print("your an major '{}'".format(age))
    else:
        if age <=18:
            print("you are an minor '{}' ".format(age))
if gender:
         print("okay you are {}".format(gender))


# In[ ]:


#ELIF, STRINGS
name=str(input("enter your name:"))
if name=="emilly":
    print("emilly")
elif name=="mike":
    printe("mike")
elif name=="bob":
    print("bob")
else:
    print("you are not in the list!")
print("thank you and good bye!",'\n')


# In[ ]:


#conditionals : string MANIPULATIONS

single_quote=str(input('single quotes'.upper()))
double_quote=str(input("double quotes".title()))
single_double=str(input('this is "single_double" string'.capitalize()))
double_single=str(input("this is 'double_single' string".capitalize()))
print("single_quote".title())
print("double_quote".upper())
print("single_double".capitalize())
print("double_single".capitalize())


# In[ ]:


#CONDITIONAL PROJECT (checking the day)

num=int(input("enter the number:"))
if(num==1):
    print("today is sunday.".captalize())
elif(num==2):
    print("today is monday.".capitalize())
elif(num==3):
    print("today is tuesday.".capitalize())
elif(num==4):
    print("today is wenesday.".capitalize())
elif(num==5):
    print("today is thursday.".capitalize())
elif(num==6):
    print("today is friday.".capitalize())
elif(num==7):
    print("today is saturday.".capitalize())
else:
    print("enter the number '1-7' to display the day.")
print("have a nice day and good bye.".capitalize())


# In[ ]:


num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch = int(input("Enter your choice:"))
if(ch==1):
    sum = num1+num2
    print("Sum:",sum)
elif(ch==2):
    diff = num1 - num2
    print("Diff:",diff)
elif(ch==3):
    mul = num1 * num2
    print("Mul:",mul)
elif(ch==4):
    div = num1 % num2
    print("Div:",div)
else:
    print("Select from the below options")


# In[ ]:


#ELSE STATMENT

name="saraha"
if name=="john":
    print("john")
else:
    print("name was not john",'\n')


# In[ ]:


#b.checking odd or even number
number=float(input("enter the number:"))
if number%2==0:
    if number==0:
        print("enter the integers value")
    else:
        print("number:",number)
        print("even")
else:
    print("number:",number)
    print("odd")
print("thank you!",'\n')


# In[ ]:


#BUILT-IN FUNCTIONS(MIN,MAX,SUM,LEN)

'''THERE IS NO DIFFRENCE BY
PLACING TUPLE OR LIST IN NUMBERS  '''

string="helloworld"
numbers=(3.14,-5,10*4,17)
print("min:",min(numbers))
print("max:",max(numbers))
print("sum:",sum(numbers))
print("len:",len(numbers))
print("min:",min(string))
print("max:",max(string))
print("len:",len(string))


# In[ ]:


#BUILT IN STRINGS
s='string_example'
if s=="string_example":
    print("this is used to print all 'capital' letters.".capitalize())
    if s=="string_example":
         print("this is used to print all 'starting capital' value.".title())
         if s=="string_example":
                print("this is used to print all 'starting upper' value.".upper())
                if s=="string_example":
                    print("this is used to print all 'starting lower' value.".lower())
            
print("s:",s.center(50,'0'))
print("checks alpha numeric value:",s.isalnum())
print("checks alphabetic charecter:",s.isalpha())
print("checks digit character:",s.isdigit())
print("checks all lower characters:",s.islower())
print("checks all numeric characters:",s.isnumeric())
print("checks white space characters:",s.isspace())
print("checks title charecters:",s.istitle())
print("checks all upper characters:",s.isupper())


# In[ ]:


n = int(input("Enter n:"))
for i in range(1,n+1):
    print(i)


# In[ ]:


#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists


# In[ ]:


#dictionaries
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values


# In[ ]:


a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")
if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")
c= b/a
if ( c in list ):
    print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")


# In[ ]:


a = 20
b = 20
print ('Line 1','a =',a,':',id(a), 'b =',b,':',id(b))
if ( a is b ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")
if ( id(a) == id(b) ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")
b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is not b ):
    print ("Line 5 - a and b do not have same identity")
else:
    print ("Line 5 - a and b have same identity")


# In[ ]:


a = 20
b = 10
c = 15
d = 5
print ("a:%d b:%d c:%d d:%d" % (a,b,c,d ))
e = (a + b) * c / d #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ", e)
e = ((a + b) * c) / d # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ", e)
e = (a + b) * (c / d) # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ", e)
e = a + (b * c) / d # 20 + (150/5)
print ("Value of a + (b * c) / d is ", e)


# In[ ]:


#Iterabels
amount=int(input("Enter amount: "))
if amount<1000:
    discount=amount*0.05
    print ("Discount:",discount)
else:
    discount=amount*0.10
    print ("Discount",discount)
print ("Net payable:",amount-discount)


# In[ ]:


#Iterabels
amount = float(input("enter your amount:"))
if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
print ("Net payable:",amount-discount)


# In[ ]:


#nested if:
num=int(input("enter number:"))
if num%2==0:
    if num%3==0:
        print ("Divisible by 3 and 2")
else:
    print ("divisible by 2 not divisible by 3")
if num%3==0:
    print ("divisible by 3 not divisible by 2")
else:
    print ("not Divisible by 2 not divisible by 3")


# In[ ]:


#Loops
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")


# In[ ]:


#infinate loop
var = 1
while var == 1 : # This constructs an infinite loop
    num = int(input("Enter a number :"))
    print ("You entered: ", num)
print ("Good bye!")


# In[ ]:


count = 0
while count < 5:
    print (count, " is less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")


# In[ ]:


# traversal of a string sequence
for letter in 'Python':
    print('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
     print ('Current fruit :', fruit)
print ("Good bye!")


# In[ ]:


fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print ('Current fruit :', fruits[index])
print ("Good bye!")


# In[ ]:


numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print('the list contains an even number')
        break
else:
    print ('the list doesnot contain even number')


# In[ ]:


for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
    print()
#end=' ' which appends a space instead of defaulthe newline.


# In[ ]:


for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
    print ('Current variable value :', var)
    var = var -1
    if var == 5:
        break
print ("Good bye!")


# In[ ]:


no=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num==no:
        print('number found in list')
        break
else:
    print('number not found in list')


# In[ ]:


for letter in 'Python':
    if letter == 'h':
        continue
    print ('Current Letter :', letter)





var = 10 
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ('Current variable value :', var)
print ("Good bye!")


# In[ ]:


import random
list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ", list)
random.shuffle(list)
print ("Reshuffled list : ", list)


# In[ ]:


var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')


# In[ ]:


str="this is string example....wow!!!"
sub='i'
print ("str.count('i') : ", str.count(sub))
sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))


# In[ ]:


Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))


# In[ ]:


#The isalnum() method checks whether the string consists of 
#alphanumeric characters.

str = "this2016" # No space in this string
print (str.isalnum())
str = "this is string example....wow!!!"
print (str.isalnum())


# In[ ]:


#The isalpha() method checks whether the string consists 
#of alphabetic characters only.
str = "this"; # No space & digit in this string
print (str.isalpha())
str = "this is string example....wow!!!"
print (str.isalpha())


# In[ ]:


str = "This Is String Example...Wow!!!"
print (str.istitle())
str = "This is string example....wow!!!"
print (str.istitle())


# In[ ]:


s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))


# In[ ]:


str = " this is string example....wow!!!"
print (str.lstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))


# In[ ]:


str = "www.tutorialspoint.com"
print ("Min character: " + min(str))
str = "TUTORIALSPOINT"
print ("Min character: " + min(str))


# In[ ]:


str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))


# In[ ]:


str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))


# In[ ]:


str = "this is string example....wow!!!"
print (str.split( ))
print (str.split('i',1))
print (str.split('w'))


# In[ ]:


list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print ("updated list : ", list1)


# In[ ]:


str = "this2016"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())


# In[ ]:


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


# In[ ]:


#converting tuple to list
aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)
str="Hello World"
list2=list(str)
print ("List elements : ", list2)


# In[ ]:


#append() method appends a passed obj into the existing list.
list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print ("updated list : ", list1)


# In[ ]:


#count() method returns count of how many times obj occurs in list.
aList = [123, 'xyz', 'zara', 'abc', 123]
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))


# In[ ]:


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.remove('Biology')
print ("list now : ", list1)
list1.remove('maths')
print ("list now : ", list1)


# In[ ]:


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print ("list now : ", list1)


# In[ ]:


ist1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)


# In[ ]:


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


# In[ ]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


# In[ ]:


dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("updated dict : ", dict)


# In[ ]:


# Function definition is here
def changeme( mylist ):
    mylist = [1,2,3,4]
    print ("Values inside the function:", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


# In[ ]:


# Function definition is here
def printinfo( name, age ):
    print ("Name: ", name)
    print ("Age ", age)
    return
# Now you can call printinfo function
printinfo( age=50, name="miki" )


# In[ ]:


def sum( arg1, arg2 ):
    total = arg1 + arg2
    print ("Inside the function : ", total)
    return total
# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )


# In[ ]:


i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
print(i)


# In[ ]:


a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9]
a.append(b)


# # converting mixture of list into single list
# 

# In[ ]:


data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)


# In[ ]:


data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element 
          in each_list]
print(output)


# In[ ]:


print (sum(
1 for x in range(1000)
if x % 2 == 0 and
'9' in str(x)
))


# In[ ]:


#changing a list of integers into list
items = ["1","2","3","4"]
[int(item) for item in items]


# In[ ]:


#List Comprehension with nested loop
[x + y for x in [1, 2, 3] for y in [3, 4, 5]]


# In[ ]:


#Nested List Comprehension
[[x + y for x in [1, 2, 3]] for y in [3, 4, 5]]


# In[ ]:


#The Nested example is equivalent to
l = []
for y in [3, 4, 5]:
    temp = []
    for x in [1, 2, 3]:
        temp.append(x + y)
    l.append(temp)


# In[ ]:


#Sorted Version
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), 'wombat', 'mongoose', 'malloo', 'camel']
sorted_list = sorted(list_things, key = lambda x: x[0])
print(sorted_list)
print()


# # Filter without function

# In[ ]:



list(filter(None, [1, 0, 2, [], '', 'a']))


# In[ ]:


# Usage without function (None):
#list(filterfalse(None, [1, 0, 2, [], '', 'a']))
# Out: [0, [], '']


# In[ ]:


#Function and Call
def func(myList):
    for item in myList:
        print(item)
func([1,2,3,5,7])
aList = ['a','b','c','d']
func(aList)


# # Return statement inside loop in a function

# In[ ]:


#In this example, function will return as soon as value var has 1
def func(params):
    for value in params:
        print ('Got value {}'.format(value))
        if value == 1:
# Returns from function as soon as value is 1
            print (">>>> Got 1") 
            return
        print ("Still looping")
    return "Couldn't find 1"
func([5, 3, 1, 2, 8, 9])


# In[ ]:


from itertools import groupby
from operator import itemgetter
import json


# # Itertools Module
# 
# In other words: It will return a generator of tuples of all the possible k-wise combinations of the input list.

# In[ ]:


import itertools
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2))
print (b)


# In[ ]:


#for three combinations
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 3))
print (b)


# In[ ]:


a = [1,2,1]
list(itertools.permutations(a))


# In[ ]:


#This simple function generates infinite series of numbers. For example...
for number in itertools.count():
    if number > 20:
        break
    print(number)


# In[ ]:


c


# In[ ]:




