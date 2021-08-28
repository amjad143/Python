#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = 'amjad'
print('how are you ',name)


# In[2]:


name = float(input('enter any number:'))
print(name)


# In[3]:


drink = "would you like a coffe?"
drink.replace("o","")
drink.replace("coffe","tea")


# In[4]:


drink.split()
drink.split("of")


# In[5]:


word = drink.split()
" yoyo " .join(word)


# In[6]:


drink.endswith("?")


# In[7]:


name='amjad'
name.startswith("a")


# In[8]:


names = ['a','b','c']
[' hello '+amj for amj in names]


# In[9]:


for i in range(0,100):
    print(i)


# In[10]:


number = list(range(0,100))
print(number)


# In[11]:


number = list(range(1,101))
[evn for evn in number if evn%3==0 ]


# In[12]:


drink= {'type':'beer','quantity':'q glass'}
print("would you like " +drink['quantity'] +" of " +drink['type']+"?")


# In[13]:


string = "do things respectively each other."
list= ['white','yellow','bliue','black']
dict = {'color':'white','shape':'circle','size':10}


for khan in list:
    print(khan)


# In[14]:


for key,value  in dict.items():
    print(key,value)


# In[15]:


for key,value  in dict.items():
    print("{0}-->{1}".format(key,value))


# In[16]:


a= 30
b= 20
if a>b:
    print("true")
else:
    print('false')


# In[17]:


def greet(name):
    print("hello {0} !".format(name))
name= ['john','amjad','khan']
for amj in name:
    greet(amj)


# In[18]:


def decide_cloth(temp):
    hot=30
    warm=20
    chill=10
    freezing=0
    cloth=''
    if temp>hot:
        cloth ='t-shirt'
    elif temp>warm:
        cloth ='jacket'
    else:
        cloth='coat'
    return cloth
cloth = decide_cloth(20)
print(cloth)


# In[ ]:




