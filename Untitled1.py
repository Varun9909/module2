#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1) Covert given hours and minutes in seconds
a=int(input("Enter the hours"))
b=int(input("Enter the minutes"))
c=a*60
d=c*60
e=b*60
f=e+d
print("The total seconds are",f)


# In[12]:


#Q2) Write code to find the average of ‘n’
numbers entered by the user to function avg ( )
def avg(lst1):
    a=0
    length=len(lst1)
    for i in range (0,length):
        a+=lst1[i]
    b=a/length
    print("Average of inputed numbers is",b)
        


# In[14]:


avg([5,10,15])


# In[25]:


# Q3)Pattern print
a=int(input("Enter the rows: "))
k=1
for i in range(1,a+1):
    
    for j in range(1,i+1):
        if k==1:
            print(1,end='')
            k-=1
        else:
            print(0,end='')
            k+=1
    print()
        


# In[1]:


# Q.4) Write a code to accept a number & print in words.
def words(a1):
    while a1>0:
        a2=a1%10
        a1=a1//10
        if a2==0:
            print("zero")
        elif a2==1:
            print("One")
        elif a2==2:
            print("Two")
        elif a2==3:
            print("Three")
        elif a2==4:
            print("Four")
        elif a2==5:
            print("Five")
        elif a2==6:
            print("Six")
        elif a2==7:
            print("Seven")
        elif a2==8:
            print("Eight")
        elif a2==9:
            print("Nine")
    


# In[4]:


words(123456789)


# In[11]:


#Q5) Create class 
class Maths:
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    def div(self,a,b):
        self.a=a
        self.b=b
        return self.a/self.b
    def sub(self,a,b):
        self.a=a
        self.b=b
        return self.a-self.b
    def mul(self,a,b):
        self.a=a
        self.b=b
        return self.a*self.b


# In[12]:


m1=Maths()


# In[13]:


m1.add(5,10)


# In[15]:


m1.div(5,2)


# In[16]:


m1.sub(10,5)


# In[17]:


m1.mul(10,5)


# In[1]:


# Q6) Q.7) Convert Paise in Rupees & Paises
 a=""
c=input("enter the rupees: ")
a=c
b=a.split(".")
b
print("Rupees= ",b[0],"\nPaise= ",b[1])


# In[ ]:




