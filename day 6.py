#!/usr/bin/env python
# coding: utf-8

# In[1]:


class bank_account():
    own=""
    bal=0
    def __init__(self,own,bal):
        self.own=own
        self.bal=bal
    def deposit(self):
        dep=int(input("ENTER THE AMOUNT TO BE DEPOSIT:"))
        self.bal=self.bal+dep
        return self.bal
    def withdraw(self):
        wd=int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
        if(wd>self.bal or  wd==self.bal):
            print("CANNOT WITHDRAW AMOUNT")
        else:
            print("withdraw the amount successfully")
            self.bal=self.bal-wd
            return self.bal 
own=input("ENTER THE NAME ")
bal=int(input("Enter the balance "))
customer=bank_account(own,bal)
print(customer.deposit())
print(customer.withdraw())


# In[3]:


import math
class cone():
    
    pi=3.14159
    
    def __init__(self,rad,ht):
        self.rad=rad
        self.ht=ht
    def volume(self):
          print("VOLUME", self.rad*self.rad*self.pi*(self.ht/3))
    def surface_area(self):
        print("Base" ,self.rad*self.rad*self.pi)
        print("SIDE", self.pi*self.rad*math.sqrt(self.rad*self.rad + self.ht* self.ht))
rad=int(input("Enter the radius"))
ht=int(input("Enter the height"))
maths= cone(rad,ht)
maths.volume()
maths.surface_area()


# In[ ]:




