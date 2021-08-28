#!/usr/bin/env python
# coding: utf-8

# # Modules and Packages

# Modules in Python are simply Python files with the .py extension, which implement a set of functions. Modules are imported from other modules using the import command. Before you go ahead and import modules, check out the full list of built-in modules in the Python Standard library.
# 
# When a module is loaded into a running script for the first time, it is initialized by executing the code in the module once. If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a "singleton" - they are initialized only once.
# 
# If we want to import module math,  we simply import the module:

# In[1]:


# import the library
import math


# In[2]:


# use it (ceiling rounding)
math.ceil(2.4)


# ## Exploring built-in modules
# 
# While exploring modules in Python, two important functions come in handy - the dir and help functions. dir functions show which functions are implemented in each module. Let us see the below example and understand better.

# In[3]:


print(dir(math))


# When we find the function in the module we want to use, we can read about it more using the help function, inside the Python interpreter:

# In[4]:


help(math.ceil)


# ## Writing modules
# Writing Python modules is very simple. To create a module of your own, simply create a new .py file with the module name, and then import it using the Python file name (without the .py extension) using the import command.
# 
# ## Writing packages
# Packages are name-spaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
# 
# The twist is, each package in Python is a directory which MUST contain a special file called **\__init\__.py**. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.
# 
# If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. We also must not forget to add the **\__init\__.py** file inside the foo directory.
# 
# To use the module bar, we can import it in two ways:

# In[5]:


# Just an example, this won't work
import foo.bar


# In[6]:


# OR could do it this way
from foo import bar


# In the first method, we must use the foo prefix whenever we access the module bar. In the second method, we don't, because we import the module to our module's name-space.
# 
# The **\__init\__.py** file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the **\__all\__** variable, like so:

# In[7]:


__init__.py:

__all__ = ["bar"]


# # Errors and Exception Handling
# 
# In this section, we will learn about Errors and Exception Handling in Python. You've might have definitely encountered errors by this point in the course. For example:

# In[8]:


print('Hello)


# Note how we get a SyntaxError, with the further description that it was an End of Line Error (EOL) while scanning the string literal. This is specific enough for us to see that we forgot a single quote at the end of the line. Understanding of these various error types will help you debug your code much faster. 
# 
# This type of error and description is known as an Exception. Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.
# 
# You can check out the full list of built-in exceptions [here](https://docs.python.org/2/library/exceptions.html). Now, let's learn how to handle errors and exceptions in our own code.

# ## try and except
# 
# The basic terminology and syntax used to handle errors in Python is the **try** and **except** statements. The code which can cause an exception to occur is put in the *try* block and the handling of the exception are the implemented in the *except* block of code. The syntax form is:
# 
#     try:
#        You do your operations here...
#        ...
#     except ExceptionI:
#        If there is ExceptionI, then execute this block.
#     except ExceptionII:
#        If there is ExceptionII, then execute this block.
#        ...
#     else:
#        If there is no exception then execute this block. 
# 
# Using just except, we can check for any exception: To understand better let's check out a sample code that opens and writes a file:

# In[9]:


try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Now, let's see what happens when we don't have write permission? (opening only with 'r'):

# In[10]:


f = open('testfile','r')
f.write('Test write this')
print("fsfsfsfsf")


# In[11]:


try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Notice, how we only printed a statement! The code still ran and we were able to continue doing actions and running code blocks. This is extremely useful when you have to account for possible input errors in your code. You can be prepared for the error and keep running code, instead of your code just breaking as we saw above.
# 
# We could have also just said except: if we weren't sure what exception would occur. For example:

# In[12]:


try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Now, we don't actually need to memorize the list of exception types! Now what if we keep wanting to run code after the exception occurred? This is where **finally** comes in.
# ##finally
# The finally: Block of code will always be run regardless if there was an exception in the try code block. The syntax is:
# 
#     try:
#        Code block here
#        ...
#        Due to any exception, this code may be skipped!
#     finally:
#        This code block would always be executed.
# 
# For example:

# In[13]:


try:
   f = open("testfile", "w")
   f.write("Test write statement")
finally:
   print("Always execute finally code blocks")


# We can use this in conjunction with except. Let's see a new example that will take into account a user putting in the wrong input:

# In[14]:


def askint():
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            
        finally:
            print("Finally, I executed!")
        print(val)       


# In[15]:


askint()


# In[18]:


askint()


# Check how we got an error when trying to print val (because it was properly assigned). Let's find the right solution by asking the user and checking to make sure the input type is an integer:

# In[19]:


def askint():
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            try:
                val = int(input("Try again-Please enter an integer: "))
            except:
                print("handle it ")
        finally:
            print("Finally, I executed!")


# In[20]:


askint()


# ### Hmmm...that only did one check. How can we continually keep checking? We can use a while loop!

# In[37]:


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            break
        else:
            print('Yep thats an integer!')
            break
        finally:
            print("Finally, I executed!")
            print(val) 


# In[38]:


askint()


# ## Database connectivity and operations using Python.
# 
# For Example, the following is the example of connecting with MySQL database "my_database1" and creating table grades1 and inserting values inside it.

# In[44]:


#!/usr/bin/python

import sqlite3
#connecting with the database.
db = sqlite3.connect("my_database3.db")
# Drop table if it already exist using execute() method.
db.execute("drop table if exists grades1")
# Create table as per requirement
db.execute("create table grades1(id int, name text, score int)")
#inserting values inside the created table
db.execute("insert into grades1(id, name, score) values(101, 'John',99 )")
db.execute("insert into grades1(id, name, score) values(102, 'Gary',90 )")
db.execute("insert into grades1(id, name, score) values(103, 'James', 80 )")
db.execute("insert into grades1(id, name, score) values(104, 'Cathy', 85 )")
db.execute("insert into grades1(id, name, score) values(105, 'Kris',95 )")


# In[45]:


db.commit()


# In[47]:


results = db.execute("select * from grades1 order by id")
for row in results:
    print(row)
print("-" * 60 )


# In[20]:


results = db.execute("select * from grades1 where name = 'Gary' ")
for row in results: print(row)
print("-" * 60 )


# In[21]:


results = db.execute("select * from grades1 where score >= 90 ")
for row in results:
    print(row)
print("-" * 60 )


# In[22]:


results = db.execute("select name, score from grades1 order by score desc ")
for row in results:
    print(row)
print("-" * 60 )


# In[23]:


results = db.execute("select name, score from grades1 order by score")
for row in results:
    print(row)
print("-" * 60 )


# In[24]:


results = db.execute("select name, score from grades1 order by score")
for row in results:
    print(row)


# In[ ]:




