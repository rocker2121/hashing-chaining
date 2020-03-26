#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# implement hashinf plus chaining class on folding method


# In[52]:


class haschain:
    def __init__(self):
        self.lst=[None]*11
        
    def put (self,number):
        x=number
        sum1=0
        while int(number/100)!=number:
            sum1+=number%100
            number=int(number/100)
        sum1=sum1+number
        sltval=sum1%11
        if self.lst[sltval]==None:
            self.lst[sltval]=[x]
        else:
            
            self.lst[sltval].append(x)
        
    def getslot (self, number):
        x=number
        sum1=0
        while int(number/100)!=number:
            sum1+=number%100
            number=int(number/100)
        sum1=sum1+number
        sltval=sum1%11
        if x in self.lst[sltval]:
            return (sltval)
        else:
            return "try again you loose"
    def printchain(self):
        print (self.lst)
        
    
        
        
        

       
        


# In[53]:


c=haschain()


# In[54]:


c.put(9876)


# In[55]:


c.put(8888)


# In[56]:


for i in range (1000,9999,1):
  
    c.put(i)


# In[57]:


c.printchain()


# In[61]:


c.getslot(2310)


# In[5]:


twosum(9876)


# In[ ]:




