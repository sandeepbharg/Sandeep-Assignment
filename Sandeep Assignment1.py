#!/usr/bin/env python
# coding: utf-8

#   TASK1.
#   
#   Q1.print hello world
#     
#     Ans:

# In[ ]:


print ("hello world")


# Q2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line
# 
# Ans-

# In[3]:


A= []
for i in range(2000,3200):
    if (i%7==0) and (i%5==0):
        A.append(str(i))
print (','.join(A))


# Q3.Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.
# Ans-

# In[4]:


Name="Sandeep Bhargav"
print(Name[::-1])


# Q4.Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r
# 3

# In[5]:


pi=3.14
r=6
V=4.0/3.0*pi* r**3
print(V)


# TASK2.
# 
# Q1.Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.
# 
# Ans-
# 

# In[6]:


Value=input("Enter comma seperated number: ")
list= Value.split(",")
print('List: ',list)


# Q2.Create the below pattern using nested for loop in Python.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# 
# 
# Ans-

# In[7]:


n=6;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# Q3.Write a Python program to reverse a word after accepting the input from the user.
# 
#     Ans-

# In[8]:


Word=input("InputWord: ")
for char in range(len(Word) -1,-1,-1):
    print(Word[char], end="")
print("\n")


# Q4.Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# 
# 
# Sample Output:
# WE, THE PEOPLE OF INDIA,
# 	having solemnly resolved to constitute India into a SOVEREIGN,!
# 		SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# 		and to secure to all its citizens:
# 

# In[9]:


I= "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(I.format('\n\t','!\n\t\t','\n\t\t',':'))


# In[ ]:




