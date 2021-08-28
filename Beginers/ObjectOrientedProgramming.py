#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating a class


# In[2]:


class Student:
    
    def __init__(self,first_name,last_name,age,class_,section):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.class_ = class_
        self.section = section


# In[3]:


student1 = Student("Ram","Kumar",17,10,"A")
student2 = Student("Shyam","Sharma",16,9,"C")


# In[4]:


print("Details of first student : Name = {0}, Age= {1} , class_section = {2}".
      format(student1.first_name+ " " +student1.last_name, student1.age, str(student1.class_)+student1.section))


# In[5]:


print("Details of second student : Name = {0}, Age= {1} , class_section = {2}".
      format(student2.first_name+ " " +student2.last_name, student2.age, str(student2.class_)+student2.section))


# In[5]:





# ### Let's see how we can write methods in a class

# In[6]:


import sqlite3

class DataBaseOperations:

    def __init__(self,databasename):
        
        self.databasename = databasename

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.databasename)
        except ConnectionError:
            raise ConnectionError
        return conn

    def createTable(self,tablename,dictionaryOfcolumnNamesAndcolumnDatatypes):
        try:
            conn = self.createDatabase()
            c = conn.cursor()
            for key in dictionaryOfcolumnNamesAndcolumnDatatypes.keys():
                datatype = dictionaryOfcolumnNamesAndcolumnDatatypes[key]
                try:
                    conn.execute(
                        'ALTER TABLE {tableName} ADD COLUMN "{column_name}" {dataType}'.format(tableName=tablename,
                                                                                               column_name=key,
                                                                                               dataType=datatype))
                except:
                    conn.execute('CREATE TABLE {tableName} ({column_name} {dataType})'.format(tableName=tablename,
                                                                                              column_name=key,
                                                                                              dataType=datatype))
            print("Table {0} created in database {1}".format(tablename,self.databasename))
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")

            print("Exception occured: " + str(e))

    def insertIntoTable(self,tablename, listOfvaluesToInsert):
        try:
            conn = self.createDatabase()
            conn.execute('INSERT INTO {tablename}  values ({values})'.format(tablename = tablename,values=(listOfvaluesToInsert)))
            conn.commit()
            print("Values Inserted Successfully!!!")
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))

        # self.closeDbconnection()
    
    def selectFromTable(self,tablename):

        try:
            conn = self.createDatabase()
            c = conn.cursor()
            c.execute("SELECT *  FROM {table}".format(table=tablename))
            print("values in table : " ,c.fetchall())
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            
        except Exception as e:
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))
    
    def closeDbConnection(self,connection):
       
        connection.close()


# In[7]:


#creating an object of class databaseOperations
db = DataBaseOperations("test1")


# In[8]:


#creating database
db.createDatabase()


# In[9]:


tableDetails = {"studentId" : "INTEGER", "studentRoll" : "INTEGER", "studentMarks" : "FLOAT"}


# In[10]:


db.createTable("table1",tableDetails)


# In[11]:


valuesToisnert= ('1,1,97')


# In[12]:


db.insertIntoTable("table1",valuesToisnert)


# In[13]:


db.selectFromTable("table1")


# In[13]:





# ### Let's understand some other concepts related to OOPS

# #### Inheritance

# In[14]:


class StudentMarks(DataBaseOperations): # inheriting the DatabaseOperation class
    
    def __init__ (self, ID, RollNumber, Marks):
        
        self.id= ID
        self.RollNum = RollNumber
        self.Marks = Marks
        self.databasename = "StudentDetails"
    


# In[15]:


student1 = StudentMarks(23,34,76)


# In[16]:


student1.createDatabase()


# In[17]:


tableDetails = {"studentId" : "INTEGER", "studentRoll" : "INTEGER", "studentMarks" : "FLOAT"}


# In[18]:


student1.createTable("studentMarks",tableDetails)


# In[19]:


valuestoInsert= ("{0},{1},{2}".format(student1.id,student1.RollNum,student1.Marks))


# In[20]:


student1.insertIntoTable("studentMarks",valuestoInsert)


# In[21]:


student1.selectFromTable("studentMarks")


# ### Polymorphism 

# In[22]:


class Instagram:
    
    def share_stories(self):
        print("share your stories on Instagram!!!")
    
class Facebook:
    
    def share_stories(self):
        print("share your stories on Facebook!!!")

def ShareStory(application):
    application.share_stories()    


# In[23]:


insta = Instagram()
fb = Facebook()


# In[24]:


ShareStory(insta)


# In[25]:


ShareStory(fb)


# ### Method OverRiding

# In[26]:


#another class inheriting the DataBaseOperation class with overRiding the insert function
class StudentDetails(DataBaseOperations): # inheriting the DatabaseOperation class
        
        def __init__ (self, FirstName,LastName, RollNumber, Class):
        
            self.FirstName= FirstName
            self.LastName = LastName
            self.RollNumber = RollNumber
            self.Class = Class
            self.databasename = "StudentDetails"
            
        #overriding the insert method of parent class to insert string values in table
        def insertIntoTable(self,tablename):
            try:
                
                firstName = '"' + self.FirstName + '"' #putting string value under quotes to insert into database
                LastName = '"' + self.LastName + '"'
                Class = '"' + self.Class + '"'
                
                listOfvaluesToInsert= ("{0},{1},{2},{3}".format(firstName,LastName,self.RollNumber,Class))
                conn = self.createDatabase()
                conn.execute('INSERT INTO {tablename}  values ({values})'.format(tablename = tablename,values=(listOfvaluesToInsert)))
                conn.commit()
                print("Values Inserted Successfully!!!")
                self.closeDbConnection(conn)
                print("Connection to database closed!!")
            except Exception as e:
                conn.rollback()
                self.closeDbConnection(conn)
                print("Connection to database closed!!")
                print("Error occured: " + str(e))
    


# In[27]:


student1 = StudentDetails("Raj","Kumar",34,"Ten")


# In[28]:


student1.createDatabase()


# In[29]:


tableDetails = {"studentFirstName" : "Varchar", "studentLastName" : "Varchar", "studentRollNumber" : "INTEGER","StudentClass": "Varchar"}


# In[30]:


student1.createTable("studentDetails",tableDetails)


# In[31]:


student1.insertIntoTable("studentDetails")


# In[32]:


student1.selectFromTable("studentDetails")


# 

# ### Encapuslation
# 

# In[33]:


class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg       
        
        
        
        


# In[34]:


emp1 = BonusDistribution(1232,'B')
emp2 = BonusDistribution(1342,'A')
emp3 = BonusDistribution(1031,'E')


# In[35]:


emp2.bonusCalculator()


# In[36]:


emp1.bonusCalculator()


# In[37]:


emp3.bonusCalculator()


# #### Let's try to change the private value of the class:

# In[38]:


emp1._bonusforRatingB = "90%"


# In[39]:


emp1.bonusCalculator()


# #### The private attribute is not changed.
# 
# To change the private attribute we need to define a function inside the class. Let's see how.

# In[40]:


class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg       
        
    def changeBonusForRatingForRest(self,value):
        
        self.__bonusforRatingForRest = value
        
        
        
        
        
        
        


# In[41]:


emp3 = BonusDistribution(1031,'E')


# In[42]:


emp3.bonusCalculator()


# In[43]:


emp3.changeBonusForRatingForRest("20%")


# In[44]:


emp3.bonusCalculator()


# #### We can see that the private attribute has now been changed and anyone can change that attribute now. This is bad way of writing a method which can change an private attribute. Let's make the function also private so it doesnot showup for everyone.

# In[45]:


class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg       
        
    def __changeBonusForRatingForRest(self,value):
        
        self.__bonusforRatingForRest = value


# In[46]:


emp3 = BonusDistribution(1031,'E')


# In[47]:


emp3.bonusCalculator()


# In[55]:


emp3.__changeBonusForRatingForRest("20%")


# #### You can see that that method cannot be accessed now. Also, the method doesnot show up in the class property:
# 
# <img src="private_method.png">
# 
# 
# If you know the name of the method, then you can still call the private member by using the class name as shown below:

# In[56]:


emp3._BonusDistribution__changeBonusForRatingForRest("20%")


# In[57]:


emp3.bonusCalculator()


# ### Operator Overloading

# In[58]:


class multiplyNum():
    
    def __init__(self,a):
        self.a =a


# In[59]:


a1 = multiplyNum(2)
a2 = multiplyNum(3)


# In[60]:


#let's try and multiply both the objects
print(a1*a2)


# We are getting an error because by default multiply supports only numerical values.
# 
# We can change the function of multiply and this is what we call overloading. 
# 
# Python calls "__mul__" function to multiply numbers, let's overload it.

# In[61]:


class multiplyNum():
    
    def __init__(self,a):
        self.a =a
    
    def __mul__(self,other):
        
         return self.a*other.a


# In[62]:


a1 = multiplyNum(2)
a2 = multiplyNum(3)


# In[63]:


a1*a2


# Great!! now we can multiply objects. We can also overide our __mul__ function and get it do return sum instead of multiplication.

# In[64]:


class multiplyNum():
    
    def __init__(self,a):
        self.a =a
    
    def __mul__(self,other):
        
         return self.a+other.a  #overloading multiply method and returning sum instead of multiplication


# In[65]:


a1 = multiplyNum(2)
a2 = multiplyNum(3)


# In[66]:


a1*a2


# ### let's overload string method 

# In[67]:


class printInformation():
    
    def __init__(self,operator):
        self.operator =operator
    
    def __str__(self):
        return "overloading the opearator :" + self.operator 


# In[68]:


print_ = printInformation('string')


# In[69]:


print(print_)


# In[69]:




