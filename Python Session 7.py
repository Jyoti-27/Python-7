#!/usr/bin/env python
# coding: utf-8

# - Conditional Statement and Loops

# In[4]:


credentials = {'Rohith':'rohith123', 
               'Virat':'virat123', 
               'Sharma':'sharma123',
               'Kohli':'kohli123', 
               'Dhoni':'dhoni123',
               'Yuvi':'yuvi123' }
print(credentials)


# In[5]:


credentials.items()


# In[7]:


username = input('Please Enter your username: ')
password = input('Please Enter you password: ')

if username not in credentials.keys():
        print('username is not in database')
        ask = input('Would you like to sign up: y/n: ')
        if ask.lower() == 'y':
            username = input('Enter your New username: ')
            password = input('Enter you New password: ')
            
            credentials.update({username:password})
            print("Added Successfully")
            print(credentials)
        else:
            print('Thank you !!!')

elif credentials[username] == password:
    print('Hello {} welcome, Lets start the game !!!'.format(username))
    # nested if condition (or nested statements)
else:
    print('Username or password is wrong')


# - Q.1 write a program to read 3 numbers and check which number is greater

# In[8]:


num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print("The first number is greater")
    if num1==num2 or num1==num3:
        print("The entered numbers are equal. Please enter the numbers again")
elif num2>num3 and num2>num1:
    print("The second number is greater")
    if num2==num1 or num2==num3:
        print("The entered numbers are equal. Please enter the numbers again")
elif num3>num1 and num3>num2:
    print("The third number is greater")
    if num3==num1 or num3==num2:
        print("The entered numbers are equal. Please enter the numbers again")
else:
    print("All the numbers are equal")


# - Q.2 write a program, that user will enter the two numbers and your program need to tell which number is greater   and if both       are equal print both are equal.

# In[9]:


n1=int(input("Enter the first number: ")); 
n2=int(input("Enter the second number: "))
if n1>n2:
    print("The first number is greater")
elif n2>n1:
    print("The second number is greater")
else:
    print("The numbers are equal")


# In[10]:


list1 = [2,4,5,7,9]
for i in list1:
    print(i)


# In[11]:


list1 = [2,4,5,7,9]
for i in list1:
    print(i+2)


# In[12]:


list2 = ["Jyoti", "Navisha", "Chaitali"]
for i in list2:
    print(i)


# - Q Print DataFolkz at 10 times.

# In[14]:


for i in range(10):
    print(i)
    print('Datafolkz')


# In[15]:


list3 = ["Data", "Folkz", "Python", "DataScience", "AI"]
for ele in list3:
    print(ele)


# - iterate over the list using index
# - for index in range(len(list)):
# - print(list[index])

# In[17]:


list3 = ["Data", "Folkz", "Python", "DataScience", "AI"]
for i in range(len(list3)):


# In[18]:


range(10)


# In[19]:


list(range(10))


# In[20]:


list1 = list(range(400,500,10))
list1


# In[21]:


list1 = list(range(500,400,-10))
list1


# In[22]:


list2 = list(range(400,500,-10))
list2


# In[23]:


lst = ["Data", "Folkz", "Python", "DataScience", "MachineLearning"]
print(len(lst))
for index in range(len(lst)):
    print(lst[index])


# In[24]:


lst = ["Data", "Folkz", "Python", "DataScience", "MachineLearning"]
for i in range(len(lst)):
    print(i,'-',lst[i])


# In[25]:


# Find the Product of all numbers present in a list
lst = [10, 20, 30, 40, 50]
product = 1
#iterating over the list
for ele in lst:
    product *= ele # multiply product * ele(terate each index value of list "lst")
    print("Final Product is:{}".format(product))
    


# In[26]:


# Find the Product of all numbers present in a list
lst = [10, 20, 30, 40, 50]
product = 1
#iterating over the list
for ele in lst:
    print("Current indexing value in ", ele, '\n')
    print("Current product value at this ele is:" , product)
    product *= ele # multiply product * ele(terate each index value of list "lst")
    print("Current product after multiplying with each ele:", product, '\n')
    print("-"*50)
    print("Final Product is:{}".format(product))
    


# In[27]:


# To print sum of elements in list
list1=[2,3,4,5,6]
sum = 0
for i in list1:
    sum +=i # iterate each index value of list1
    print(sum) 
print('final sum is :',sum)    


# In[28]:


numbers = [1, 2, 3,4,8,9,12]
# iterating over the list
for item in numbers:
    print(item)
else:
        print("no item left in the list")


# In[29]:


for item in numbers:
    print(item)
    if item % 2 == 0:
        break
else:
            print("no item left in the list")


# In[30]:


numbers = [1, 2, 5, 7, 11, 12, 15]
# iterating over the list
for item in numbers:
    print(item)
else:
       print("no item left in the list")


# In[31]:


for item in numbers:
    print(item)
    if item % 2 == 0:
        break
else:
            print("no item left in the list")


# In[32]:


# Python Programme to display prime numbers within an interval. 
index1 = int(input("Enter Index1 number: "))
index2 = int(input("Enter Index1 number: "))
print("Primr numbers between {0} and {1} are :".format(index1,index2))
for num in range(index1,index2+1):  # default step size is 1
    if num > 1:
        isDivisible = False
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True
        if not isDivisible:
             print(num)


# In[33]:


firstname = input("My first name is: ")
lastname = input("My last name is: " )
print("My first name is {} and the last name is {}  : ".format(firstname,lastname))


# In[36]:


index1 = int(input("Enter Index1 number: "))
index2 = int(input("Enter Index2 number: "))

print("Prime numbers between {0} and {1} are :".format(index1, index2))

for num in range(index1, index2 + 1):
   # all prime numbers are greater than 1
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[37]:


list1 = [1,2,3,4,5]
for index, val in enumerate(list1):
    print(index, val)


# In[ ]:





# In[ ]:




