#!/usr/bin/env python
# coding: utf-8

# In[1]:


#conditions
a,b = 0,1
if a>b:
    print('a() is less than b ()' .format(a,b))
else:
    print('a () is not less than b()'.format(a,b))


# In[2]:


#if we use the tupels in dict to show the place of the value
a,b = 4,1
if a<b:
    print('a({}) is less than b ({})' .format(a,b))
else:
    print('a ({}) is not less than b({})'.format(a,b))


# In[3]:


#by using display use double codes inside the tuple
print("amjad" if a < b else "bar")


# In[4]:


#ther are two fundemental loops of python
#while
a,b= 0,1
while b<50:
    print(b)
    a,b = b,a+b
print("As long as the conditon is true it keep on gentrating")


# In[5]:


def isprime(n):
    if n==1:
        print("1 is special")
        return False
    for x in range(2,n):
        if n % x ==0:
            print("{} equals {} % {} ".format(n,x,n//x))
            return False
    else:
        print(n,"is a prime number")
        return True
for n in range(1,20):
    isprime(n)


# In[6]:


def isprime(n):
    if n==1:
        return False
    for x in range(2,n):
        if n % x ==0:
            return False
    else:
        return True
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)
    


# In[7]:


a =21
s = "tiubei urgbeiuge {} ibiue".format(a)
print(s)


# In[8]:


choices = dict(
          one = 'first',
          two =  'second',
          three = 'three'
           )
v = 'seven'
print(choices[v])


# In[9]:


print(choices.get(v,'other'))


# In[10]:


#conditional statment for short hand
a,b = 0,1
v = 'this is true' if a<b else 'this is not true'
print(v)


# In[11]:


#using enumarate
s = 'this is a string'
for i ,c in enumerate(s): #i=index,c=charecter
    if c=='s':print('index {} is an s'.format(i))


# In[12]:


s = 'this is amjad'
for i in s:
    print(i,end="")


# In[13]:


#continue
r = 'this is amjad'
for i in r:
    if i =='s':continue
    print(i,end="")


# In[14]:


#break
r = 'this is amjad'
for i in r:
    if i =='s':break
    print(i,end="")


# In[15]:


#by using while statment
s = 'this is string'
i = 0
while(i < len(s)):
    print(s[i],end='')
    i +=1
else:
    print('else')


# In[16]:


#to open the text file if does not open place a text
try:
    fh = open('read the file')
    for line in fh: print(line.strip())
except IOError as e:
    print("could not open the file.come back tomorrow.")

    


# In[17]:


# basic function
def testfun():
    print("this is a test function")
testfun()


# In[18]:


for i in range(0,25,3):
    print(i,end='')


# In[19]:


def inclusive_range(start,stop,step):
    i = start
    while i <= stop:
        yield i
        i += step
def inclusive_range() 


# In[20]:


#creating a simple database
import sqlite3
def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exsits test')
    db.execute('create table test(t1 text,i1 int)')
    db.execute('insert into test (t1,i1) values(?,?)',('one',1))
    db.execute('insert into test (t1,i1) values(?,?)',('two',2))
    db.execute('insert into test (t1,i1) values(?,?)',('three',3))
    db.execute('insert into test (t1,i1) values(?,?)',('four',4))
    db.commit()
    cursor = db.execute('select * from test order by t1')
    for row in cursor: print(row)



 

    


# In[21]:


s= input("print the number:")
print("s:",s,'\n')


# In[22]:


s=int(input("enter number1:"))
s1=int(input("enter number2:"))
mul=s*s1
print("mul:",mul,'\n')


# In[23]:


a=int(input("enter the integer 1:"))
b=int(input("enter the integer 2:"))
add=a+b
print(a,"+",b,"=",add)
print("add:",add,'\n')


# In[24]:


a=float(input("enter the integer 1:"))
b=float(input("enter the integer 2:"))
Sub=a-b
print(a,"-",b,"=",Sub)
print("Sub:",Sub,'\n')


# In[25]:


a=int(input("enter the integer 1:"))
b=int(input("enter the integer 2:"))
add=a+b
print(a,"+",b,"=",add)
print("add:",add,'\n')


# In[26]:


a=float(input("enter the integer 1:"))
b=float(input("enter the integer 2:"))
mul=a*b
print(a,"*",b,"=",mul)
print("mul:",mul,'\n')


# In[27]:


a=float(input("enter the division:"))
b=float(input("enter the division:"))
div=a//b
print(a,"//",b,"=",div)
print("div:",div,'\n')


# In[28]:


#reminder,division
n1=float(input("enter the numerator:"))
n2=float(input("enter the denominator:"))
reminder=n1%n2
print(n1,"%",n2,"=",reminder)
print("reminder:",reminder,'\n')


# In[29]:


#3.STRING,square
a=str(input("enter the string1:"))
b=str(input("enter the string2:"))
square=a+b
print(a,"+",b,"=",square)
print("square:",square,'\n')


# In[30]:


#4.BOLLEAN

s=int(input("enter the bollean:"))
s1=int(input("enter the bollean1:"))
result=s>s1
print(s,">",s1,"=",result)
print("result:",result,'\n')


# In[31]:


s=str(input("enter the bollean:"))
s1=str(input("enter the bollean1:"))
result=s>=s1
print(s,">",s1,"=",result)
print("result:",result)


# In[32]:


#BUILT IN STRINGS AND FORMATING
#FORMAING  : .FORMATE(STR)
# EXAMPLE SINGLE LINE FORMATING(%d,%b,%s,%f).
n=10
a="amjad"
print("this prints the 'given number' {:d}".format(n))
print("this prints the binary'' {:b}".format(n))
print("this prints the 'string' {:s}".format(a))
print("this prints 'real number' small {:f}".format(n))
print("this prints 'real number' small '{}' '{}'".format(n,a))


# In[33]:


#EXAMPLE FORMATING :F
float=1.234567
integer=11
string="computer"
print("{:}".format(float))
print("{0} {1} {2}".format(float,integer,string),'\n')


#ANOTHER EXAMPLE
print("This is {name} i have {ows} of {objects}"
      .format(name="amjad khan",
                    ows=5,
                    objects="mangoes"),'\n')


# In[34]:


#PROJECT: (printing first_name,middle_first,last_name)
first_name = str(input("enter your first name:".capitalize()))
middle_name = str(input("enter your middle name:".capitalize()))
last_name = str(input("enter your last name:".capitalize()))
first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()
name_formate = "{first}{middle:1s}{last}"
print(name_formate.format(first=first_name,
                          middle=middle_name,
                          last=last_name))


# In[35]:


first_name = str(input("enter your first name:".capitalize()))
middle_name = str(input("enter your middle name:".capitalize()))
last_name = str(input("enter your last name:".capitalize()))
print('{} {} {}'.format(first_name,middle_name,last_name))


# In[36]:


#DICTIONARIES
#to print the statment enter tuple in list
dict = {'name:':'amjad','age:':7,'class':'first'}
print(dict.keys())
dict.values()


# In[37]:


#print(dict('name:'))
print("dict['name:']:",dict['name:'])
print("dict['age:']:",dict['age:'])
print("dict['class']:",dict['class'],'\n')


# In[38]:


del dict['name:']
print(dict)


# In[39]:


#CLEAR ALL THE ENTRIES
dict.clear()
print(dict)


# In[40]:


#1.LENGTH
print(len(dict))
dict
len(dict)


# In[41]:


#STRING
print(str(dict))


# In[42]:


#to print the statment enter tuple in list
dict = {'name:':'amjad','age:':7,'class':'first'}
#STRING
print(str(dict))


# In[43]:


print(len(dict))
dict
len(dict)


# In[44]:


print(type(dict))


# In[45]:


#COPY
dict1=dict.copy()
print(dict1)


# In[46]:


#DICTIONARIES VARIABLE.FROMKEYS((SEQ,VALUE))
#converting tuples into DICTIONARIES

seq=('name','age','sex')
dict=dict.fromkeys(seq)
print(str(dict))
dict=dict.fromkeys(seq,10)
print(str(dict))


# In[47]:


#SET DEFAULT

dict={'name':'amjad','age':28}
print(dict.setdefault('age',))


# In[48]:


#CONDITIONAL or DECISION MAKING

#1.IF statment
'''syntax:  if expression:
               statment(s)
                      ''' 
var1=100
if var1:
    print("1-got a true expression.")
    print("var1:",var1,'\n')


# In[49]:


age=34
if age==35:
    print("age is equal to 35!")
    print("age:",age,'\n')
else:
    print("above statment is not correct")


# In[50]:


#3.IF contains more if within a statment
age=28
name="amjad"
if name=="amjad":
    print("yes my name is amjad!")
    if age==28:
        print("my name is amjad! and i am 28 years old",'\n')


# In[51]:


#a.type name:amjad,age:28
name=str(input("enter your name:"))        
if name:
    print("Name:",name.capitalize())
    print("My name is:",name)
else:
    print("enter only string values")
    


# In[52]:


#a.type name:amjad,age:28
name=str(input("enter your name:"))        
age=int(input("enter your age:"))
if name=="amjad":
   print("name:",name)
   print("my name is amjad!")
   if age==28:
       print("age:",age)
       print("yes your age is 28!",'\n')


# In[ ]:




