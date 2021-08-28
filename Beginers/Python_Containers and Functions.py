#!/usr/bin/env python
# coding: utf-8

# # In this session, we are going to explore other container objects and functions
# 
# ## In this session, we are going to learn the following key topics:
# *   Tuple
# *   Set
# *   Dictionary
# *   Function
# *   Lambda
# *   Iterator
# *   Generator
# *   Map
# *   Reduce
# *   Filter

# # Tuples
# 
# In Python, tuples are similar to lists but they are immutable i.e. they cannot be changed. You would use the tuples to present data that shouldn't be changed, such as days of week or dates on  a calendar.
# 
# In this section, we will get a brief overview of the following key topics:
# 
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples
# 
# You'll have an intuition of how to use tuples based on what you've learned about lists. But, Tuples work very similar to lists but the  major difference is tuples are immutable.
# 
# ## Constructing Tuples
# 
# The construction of tuples use () with elements separated by commas where in the arguments will be passed within brackets. For example:

# In[1]:


# Can create a tuple with mixed types
t = (1,2,3)


# In[2]:


# Check len just like a list
type(t)


# In[3]:


# Can also mix object types
t = ('one',2)

# Show
l = ['sdf','sf']
l.sort()
l


# In[4]:


# Use indexing just like we did in lists
t[0]


# In[5]:


# Slicing just like a list
t[-1]


# ## Basic Tuple Methods
# 
# Tuples have built-in methods, but not as many as lists do. Let's see two samples of tuple built-in methods:

# In[6]:


# Use .index to enter a value and return the index
t.index(89)


# In[7]:


# Use .count to count the number of times a value appears
t.count('one')


# ## Immutability
# 
# As tuples are immutable, it can't be stressed enough and add more into it. To drive that point home:

# In[8]:


t[0]= 'change'


# Because tuple being immutable they can't grow. Once a tuple is made we can not add to it.

# In[9]:


t.append('nope')


# ## When to use Tuples
# 
# You may be wondering, "Why to bother using tuples when they have a few available methods?" 
# 
# Tuples are not used often as lists in programming but are used when immutability is necessary. While you are passing around an object and if you need to make sure that it does not get changed then tuple become your solution. It provides a convenient source of data integrity.
# 
# You should now be able to create and use tuples in your programming as well as have a complete understanding of their immutability.

# # Sets
# 
# Sets are an unordered collection of *unique* elements which can be constructed using the set() function. 
# 
# Let's go ahead and create a set to see how it works.

# In[10]:


x = set()


# In[11]:


# We add to sets with the add() method
x.add(3)


# In[12]:


#Show
x


# Note that the curly brackets do not indicate a dictionary! Using only keys, you can draw analogies as a set being a dictionary.
# 
# We know that a set has an only unique entry. Now, let us see what happens when we try to add something more that is already present in a set?

# In[13]:


# Add a different element
x.add(2)


# In[14]:


#Show
x


# In[15]:


# Try to add the same element
x.add(1)


# In[16]:


#Show
x


# Notice, how it won't place another 1 there as a set is only concerned with unique elements! However, We can cast a list with multiple repeat elements to a set to get the unique elements. For example:

# In[17]:


# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]


# In[18]:


# Cast as set to get unique values
set(l)


# # Dictionaries
# 
# We have learned about "Sequences" in the previous session. Now, let's switch the gears and learn about "mappings" in Python. These dictionaries are nothing but hash tables in other programming languages.
# 
# In this section, we will learn briefly about an introduction to dictionaries and what it consists of:
# 
#     1.) Constructing a Dictionary
#     2.) Accessing objects from a Dictionary
#     3.) Nesting Dictionaries
#     4.) Basic Dictionary Methods
# 
# Before we dive deep into this concept, let's understand what are Mappings? 
# 
# Mappings are a collection of objects that are stored by a "key". Unlike a sequence, mapping store objects by their relative position. This is an important distinction since mappings won't retain the order since they have objects defined by a key.
# 
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.
# 
# 
# ## Constructing a Dictionary
# Let's see how we can construct dictionaries to get a better understanding of how they work!

# In[19]:


# Make a dictionary with {} and : to signify a key and a value
my_dict = {True:'value1','key2':'value2','key1':'valuedfvdfg','key1':'abc'}
my_dict


# In[20]:


# Call values by their key
my_dict['key2']


# Note that dictionaries are very flexible in the data types they can hold. For example:

# In[21]:


my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[22]:


#Let's call items from the dictionary
my_dict['key2'][2]


# In[23]:


# Can call an index on that value
my_dict['key3'][0]


# In[24]:


#Can then even call methods on that value
my_dict['key3'][0].upper()


# We can effect the values of a key as well. For instance:

# In[25]:


my_dict['key1']


# In[26]:


# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123


# In[27]:


#Check
my_dict['key1']


# Note, Python has a built-in method of doing a self subtraction or addition (or multiplication or division). We could also use += or -= for the above statement. For example:

# In[28]:


# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
my_dict['key1']


# We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

# In[29]:


# Create a new dictionary
d = {}
type(d)


# In[30]:


# Create a new key through assignment
d['animal'] = 'xyz'
d


# In[31]:


# Can do this with any object
d['answer'] = 42


# In[32]:


#Show
d


# ## Nesting with Dictionaries
# 
# Let's understand how flexible Python is with nesting objects and calling methods on them. let's have a look at the dictionary nested inside a dictionary:

# In[33]:


# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# Thats the inception of dictionaries. Now, Let's see how we can grab that value:

# In[34]:


# Keep calling the keys
d['key1']['nestkey']


# ## A few Dictionary Methods
# 
# There are a few methods we can call on a dictionary. Let's get a quick introduction to a few methods:

# In[35]:


# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}


# In[36]:


# Method to return a list of all keys 
f=d.keys()
list(f)[0]


# In[37]:


# Method to grab all values
type(d.values())


# In[38]:


# Method to return tuples of all items  (we'll learn about tuples soon)
d.items()


# 

# ## Dictionary Comprehensions
# 
# Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension for quick creation. It is not as commonly used as List Comprehensions, but the syntax is:

# In[39]:


{x:x**2 for x in range(10)}


# One of the reasons is the difficulty in structuring the key names that are not based on the values.

# # Functions
# 
# ## Introduction to Functions
# 
# What is a function in Python and how to create a function? 
# 
# Functions will be one of our main building blocks when we construct larger and larger amount of code to solve problems.
# 
# **So what is a function?**
# 
# A function groups a set of statements together to run the statements more than once. It allows us to specify parameters that can serve as inputs to the functions.
# 
# Functions allow us to reuse the code instead of writing the code again and again. If you recall strings and lists, remember that len() function is used to find the length of a string. Since checking the length of a sequence is a common task, you would want to write a function that can do this repeatedly at command.
# 
# Function is one of the most basic levels of reusing code in Python, and it will also allow us to start thinking of program design.

# ## def Statements
# 
# Now, let us learn how to build a function and what is the syntax in Python.
# 
# The syntax for def statements will be in the following form:

# In[40]:


def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (doc-string) goes
    '''
    # Do stuff here
    #return desired result


# We begin with def then a space followed by the name of the function. Try to keep names relevant and simple as possible, for example, len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a [built-in function in Python](https://docs.python.org/2/library/functions.html) (such as len).
# 
# Next, comes the number of arguments separated by a comma within a pair of parenthesis which acts as input to the defined function,  reference them and the function definition with a colon.  
# 
# Here comes the important step to indent to begin the code inside the defined functions properly. Also remember, Python makes use of *whitespace* to organize code and lot of other programming languages do not do this.
# 
# Next, you'll see the doc-string where you write the basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these doc-strings by pressing Shift+Tab after a function name. It is not mandatory to include docstrings with simple functions, but it is a good practice to put them as this will help the programmers to easily understand the code you write.
# 
# After all this, you can begin writing the code you wish to execute.
# 
# The best way to learn functions is by going through examples. So let's try to analyze and understand examples that relate back to the various objects and data structures we learned.

# ### Example 1: A simple print 'hello' function

# In[41]:


def say_hello():
    print('hello')


# Call the function

# In[42]:


say_hello()


# ### Example 2: A simple greeting function
# Let's write a function that greets people with their name.

# In[43]:


def greeting(name):
    print('Hello %d' %name)


# In[44]:


x


# In[45]:


x = greeting(90)


# In[46]:


x


# ## Using return
# Let's see some examples that use a return statement. Return allows a function to "return" a result that can then be stored as a variable, or used in whatever manner a user wants.
# 
# ### Example 3: Addition function

# In[47]:


def add_num(num1,num2):
    return num1+num2


# In[48]:


add_num(4,5)


# In[49]:


# Can also save as variable due to return
result = add_num(4,5)
result


# In[50]:


print(result)


# What happens if we input two strings?

# In[51]:


print(add_num('one',1))


# In Python we don't declare variable types, this function could be used to add numbers or sequences together! Going forward, We'll learn about adding in checks to make sure a user puts in the correct arguments into a function.
# 
# Let's also start using *break*,*continue*, and *pass* statements in our code. We introduced these during the while lecture.

# Now, let's see a complete example of creating a function to check if a number is prime (a common interview exercise).
# 
# We know a number is said to be prime if that number is only divisible by 1 and itself. Let's write our first version of the function to check all the numbers from 1 to N and perform modulo checks.

# In[52]:


def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print('not prime')
            break
    else: # If never mod zero, then prime
        print('prime')


# In[53]:


is_prime(0)


# Note that how we break the code after the print statement! We can actually improve this by only checking to the square root of the target number, also we can disregard all even numbers after checking for 2. We'll also switch to returning a boolean value to get an example of using return statements:

# In[54]:


import math

def is_prime(num):
    '''
    A Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# In[55]:


is_prime(7)


# In[55]:





# In[55]:





# In[56]:


for i in []:
    if 2 % i == 0:
        print("false")
print("true")


# # Iterators and Generators

# In this section, you will be learning the differences between iterations and generation in Python and also how to construct our own generators with the "yield" statement. Generators allow us to generate as we go along instead of storing everything in the memory.
# 
# We have learned, how to create functions with "def" and the "return" statement. In Python, Generator function allow us to write a function that can send back a value and then later resume to pick up where it was left. It also allows us to generate a sequence of values over time. The main difference in syntax will be the use of a **yield** statement.
# 
# In most aspects, a generator function will appear very similar to a normal function. The main difference is when a generator function is called and compiled they become an object that supports an iteration protocol. That means when they are called they don't actually return a value and then exit, the generator functions will automatically suspend and resume their execution and state around the last point of value generation. 
# 
# The main advantage here is "state suspension" which means, instead of computing an entire series of values upfront and the generator functions can be suspended. To understand this concept better let's go ahead and learn how to create some generator functions.

# In[57]:


# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3


# In[58]:


for x in gencubes(10):
    print(x)


# In[59]:


gencubes(10)


# In[60]:


for i in "fsfdsfsf":
    print(i)


# Great! since we have a generator function we don't have to keep track of every single cube we created.
# 
# Generators are the best for calculating large sets of results (particularly in calculations that involve loops themselves) when we don't want to allocate memory for all of the results at the same time. 
# 
# Let's create another sample generator which calculates [fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) numbers:

# In[61]:


def genfibon(n):
    '''
    Generate a fibonacci sequence up to n
    '''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


# In[62]:


for num in genfibon(10):
    print(num)


# What if this was a normal function, what would it look like?

# In[63]:


def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output


# In[64]:


fibon(10)


# Note, if we call some huge value of "n", the second function will have to keep track of every single result. In our case, we only care about the previous result to generate the next one.
# 
# 
# ## next() and iter() built-in functions
# 
# A key to fully understand generators is the next() and the iter() function.
# 
# The next function allows us to access the next element in a sequence. Let's check how it works.

# In[65]:


def simple_gen():
    for x in range(3,7):
        yield x


# In[66]:


# Assign simple_gen 
g = simple_gen()
g


# In[67]:


print(next(g))


# In[68]:


print(next(g))


# In[69]:


print(next(g))


# In[70]:


print(next(g))


# After yielding all the values next() caused a StopIteration error. What this error informs us that all the values have been yielded. 
# 
# You might be wondering that why don’t we get this error while using a for loop? The "for loop" automatically catches this error and stops calling next. 
# 
# Let's go ahead and check out how to use iter(). You remember that strings are iterable:

# In[71]:


s = 'helloo'

#Iterate over string
for let in s:
    print(let)


# But that doesn't mean the string itself is an *iterator*! We can check this with the next() function:

# In[72]:


l = "helllo"


# This means that a string object supports iteration, but we can not directly iterate over it as we could with a generator function. The iter() function allows us to do just that!

# In[73]:


s = iter(l)


# In[74]:


next(s)


# In[75]:


next(s_iter)


# # map()
# 
# The map() is a function that takes in two arguments: 
# 1. A function 
# 2. A sequence iterable. 
# 
# In the form: map(function, sequence)
#     
# The first argument is the name of a function and the second a sequence (e.g. a list). map() applies the function to all the elements of the sequence. It returns a new list with the elements changed by the function.
# 
# When we went over list comprehension we created a small expression to convert Fahrenheit to Celsius. Let's do the same here but use map. 
# 
# We'll start with two functions:

# In[76]:


def fahrenheit(T):
    return ((float(9)/5)*T + 32)


def celsius(T):
    return (float(5)/9)*(T-32)
    
temp = [0, 22.5, 40,100]


def summ(x, y ):
    return x+y


# Now let's see map() in action:

# In[77]:


F_temps = list(map(fahrenheit, temp))

#Show
F_temps


# In[78]:


# Convert back
list(map(celsius, F_temps))


# In the example above, we haven't used a lambda expression. By using lambda, it is not necessary to define and name fahrenheit() and celsius() functions.

# In[79]:


list(map(lambda x : x+1, F_temps))


# Map is more commonly used with lambda expressions since the entire purpose of a map() is to save effort on creating manual for loops.

# map() can be applied to more than one iterable. The iterables must have the same length.
# 
# For instance, if we are working with two lists-map() will apply its lambda function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the nth index is reached.
# 
# For example, let's map a lambda expression to two lists:

# In[80]:


a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12,4,5]

list(map(lambda x,y:x+y,a,b))


def sum(x,y,z):
    return x+y+z


# In[81]:


# Now all three lists
list(map(sum, a,b,c))


# In the above example, the parameter 'x' gets its values from the list 'a', while 'y' gets its values from 'b' and 'z' from list 'c'. Go ahead and create your own example to make sure that you completely understand mapping more than one iterable.

# # reduce()
# 
# The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value. 
# 
# If seq = [s1, s2, s3, ... , sn], calling reduce(function, sequence) works like this:
# 
# * At first the first two elements of sequence will be applied to function, i.e. func(s1,s2) 
# * The list on which reduce() works looks like this: [ function(s1, s2), s3, ... , sn ]
# * In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
# * The list looks like: [ function(function(s1, s2),s3), ... , sn ]
# * It continues like this until just one element is left and return this element as the result of reduce()
# 
# Let's see an example:

# In[82]:


from functools import reduce
lst =['sdfs','sdfsfsdf','sdf']
reduce(lambda a,b: a+b,lst)


# Let's look at a diagram to get a better understanding of what is going on here:

# In[83]:


from IPython.display import Image
Image('http://www.python-course.eu/images/reduce_diagram.png')


# Note how we keep reducing the sequence until a single final value is obtained. Let's see another example:

# In[84]:


#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
lst =[47,11,42,13]
a,b


# In[85]:


#Find max
reduce(max_find,lst)


# # filter
# 
# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns "True". 
# 
# The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns "True" will the element of the iterable be included in the result.
# 
# Let's see some examples:

# In[86]:


#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True


# Now let's filter a list of numbers. Note that putting the function into filter without any parenthesis might feel strange, but keep in mind that functions are objects as well.

# In[87]:


lst =[1,2,3,4,5,6,7,8]

list(filter(even_check,lst))


# filter() is more commonly used with lambda functions, this because we usually use filter for a quick job where we don't want to write an entire function. Let's repeat the example above using a lambda expression:

# In[88]:


list(map(lambda x: x%2==0,lst))


# In[88]:




