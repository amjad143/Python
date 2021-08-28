#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 10
if( i < 5) & (i ==10):
    print("this is a valid statemnt ")
elif i < 8:
    print("this is a valid stament in elif")
else:
    print("this will give me a defalut statement ")
    


# In[2]:


i = 10 
s = "sudh"
if i==10:
    if type(s)==int:
        print("this is my name ")
    else : 
        print("this is a defalut condition ")
else :
    print("this is default dtatemnt for outer if block ")


# In[3]:


l = [3,4,4,5,6,"sudh","kumar","xyz"]
l


# In[4]:


l[::2]


# In[5]:


m = []
for i in l:
    if type(i)==int:
        m.append(i/10)


# In[6]:


m


# In[7]:


b=[]
for i in l:
    if type(i)==int:
        i= i+i
        print(i)


# In[8]:



x = [1,2,3,4,6,'ashu','hello','hii']

m = 0

for i in x:
    
    if type(i) == int:
        m = m+i

print(m)


# In[9]:


for i in "sudh":
    print(i)


# In[10]:


l = [4,5,6,6]
for i in l :
    if i == 9:
        break
    print(i)
else :
    print("this is the for else block ")


# In[11]:


s = "sudh kumar"
for i in s :
    if i == 'k':
        continue
    print(i)


# In[12]:


list(range(6))


# In[13]:


list(range(4,9,2.0))


# In[14]:


list(range(4,9,2))


# In[15]:


l = [5,6,7,4,5,6,"sudh ","kuamr"]


# In[16]:


len(l)


# In[17]:


for i in range(len(l)):
    print(l[i])


# In[18]:


input()


# In[19]:


a = int(input("take my name and age" ))
type(a)


# In[20]:


type(input())


# In[21]:


"sudh"  + str(9)


# In[22]:


l = [4,5,6,6]
l1 = [4,5,6,4,3]


# In[23]:


l +l1


# In[24]:


#this is a code to explain your str operation 
'sudhanshu"s'


# In[25]:


"""faasfsafasf 
fasfsa
fsadfas
fsadfas
fas
fsa
fa
sf
asf
as
fd"""


# In[26]:


s = "hello world"


# In[27]:


s = s.upper()


# In[28]:


s


# In[29]:


s.lower()


# In[30]:


s = "hello world sudhanshu kumar"


# In[35]:


s.split("o")


# In[36]:


"my name is {} .my age is {}".format("sudh",432)


# In[37]:


s  = "hello world"


# In[38]:


s.find('l')


# In[39]:



str1 = 'hello world'
l = []
l1 = []
for i in range(len(str1)):
    if str1[i]=='l':
        l.append(i)
        l1.append(str1[i])
print(l, l1, sep='\n')


# In[40]:


s = "sudh"
s


# In[41]:


s.center(40,'v')


# In[42]:


'hello\tworld'.expandtabs()


# In[43]:


y = "HEllow"


# In[44]:


y.istitle()


# In[45]:


y.isalpha()


# In[46]:


y.isnumeric()


# In[47]:


y.islower()


# In[48]:


y.isupper()


# In[49]:


y.isspace()


# In[50]:


"sudh" * 3


# In[51]:


[5,6,8]*3


# In[52]:


l = [1,2,3,4,5,6,7,7,8,"sudh"]


# In[53]:


l.append("kumar")


# In[54]:


l


# In[55]:


l.insert(2,"xyz")


# In[56]:


l


# In[57]:


l


# In[58]:


l.pop()


# In[59]:


l


# In[60]:


l.pop(3)


# In[61]:


l


# In[62]:


l =l[::-1]


# In[63]:


l


# In[64]:


l.reverse()


# In[65]:


l


# In[66]:


l


# In[67]:


l.sort()


# In[68]:


l = [4,3,4,4,5,6,67,7]


# In[69]:


l.sort()


# In[70]:


l


# In[71]:


sl   = ["sudh",'kumar']


# In[72]:


sl.sort()


# In[73]:


sl


# In[74]:


l = [4,5,6,7,8]
l[3] = "sudh"


# In[75]:


l


# In[76]:


l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [6,5,7,8]


# In[77]:


l = [l1,l2,l3]


# In[78]:


l


# In[79]:


[i[2] for i in l]


# In[80]:


n


# In[81]:


l = [4,5,6,6]


# In[82]:


l.append([5,6,7])


# In[83]:


l


# In[84]:


l1 = [4,5,6,7]


# In[85]:


l1.extend([5,6,7])


# In[86]:


l1


# In[87]:


l = [5,3,4,5,6,7,8,5,6,7,8,2,4,3,2,2,2]


# In[88]:


l = [5,6,7,2,8,5,6,4,6,5,6,7,8,2]
l = [i for i in l if i != 2]


# In[89]:


l


# In[90]:


m=[]
l=[5,6,4,2,1,2,1,7,8,9,2,2]
for i in l :
    if i != 2 :
        m.append(i)
print(m)


# In[91]:


l=[2,2,22,2,22,5,4,5,5,7]
while 2 in l:
    l.remove(2)


# In[92]:


l


# In[92]:




