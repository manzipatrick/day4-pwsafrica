#!/usr/bin/env python
# coding: utf-8

# In[4]:


max([1,2,3])


# In[5]:


def findmin(list):
    minvalue=list[0]
    for i in list:
        if i<minvalue:
            minvalue=i
    return minvalue
res=findmin([1,2,3,4,5])
print(res)


# In[ ]:


def findmin(list):
    minvalue=list[0]
    for i in list:
        if i<minvalue:
            minvalue=i
    return minvalue
res=findmin([1,2,3,4,5])
print(res)


# In[20]:


def average(list):
    sum1 = sum(list)
    n=len(list)
    avg=sum1/n
    return avg
result=average([1,2,3,4,5])
print(result)


# In[25]:


def sum(list):
    summation=0
    for i in list:
        summation=summation + i
    return summation 
answer=sum([1,2,3,4,5])

def average(list):
    sum1 = answer
    n=len(list)
    avg=sum1/n
    return avg
result=average([1,2,3,4,5])
print(result)


# In[9]:


februarydata = [[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
maxweek=[]
for i in range(len(februarydata)):
    m=max(februarydata[i])
    maxweek.append(m)
maxall=max(maxweek)
print(maxall)


# In[16]:


#not complete
februarydata = [[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
avgweek=[]
for i in range(len(februarydata)):
    
    #aw=average(februarydata[i])
    #avgweek=avgweek.append(aw)


# In[17]:


#februarydata = [[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
#count=0
#for i in range(len(februarydata)):
#    if februarydata[i]>3:

def numofcounts(februarydata)
    


# In[31]:


februarydata = [[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
for i in februarydata:
    def average(februarydata[i]):
        sum1=sum(februarydata[i])
        n=len(februarydata[i])
        avg=sum1/n
        return avg
    averagef=average(februarydata[i])
    print(averagef)


# In[46]:


def average(list):
    sum1 = sum(list)
    n=len(list)
    avg=sum1/n
    return avg
februarydata = [[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
newlist=[]
for i in range(len(februarydata)):
    mavg=average(februarydata[i])
    newlist.append(mavg)
print(newlist)
m=average(newlist)
print(m)

    


# In[ ]:


#number3
#how much water he uses in a month


# In[82]:


#simple counts
def makecount(list):
    count=0
    for i in list:
        if i==0:
            count+=1
    return count
list=[1,0,3,4,0,2,3,0,2]
result=makecount(list)*50
print(result)


# In[81]:


#counting where 
def makecount(list):
    count=0
    for i in list:
        for j in i:
            if j ==0:
                count+=1
    return count*150

februarydata = [[5,2,5,0,3,4,4],[1,0,3,1,3,1,4],[5,2,1,1,3,3,3],[0,0,0,1,3,4,4]]
allcounts= makecount(februarydata)
   
print(allcounts)


# In[89]:


def mycounter(list) :
    count=0
    for i in list:
        for n in i:
            if n>3:
                count+=1
    x=count
    return x
februarydata = [[5,2,5,0,3,4,4],[1,0,3,1,3,1,4],[5,2,1,1,3,3,3],[0,0,0,1,3,4,4]]
answer=mycounter(februarydata)
print(str(answer) + " times")


# In[110]:


def average(list):
    sum1 = sum(list)
    n=len(list)
    avg=sum1/n
    return avg
marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],
[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]

newlist=[]
for i in range(len(marks)):
    mavg=average(marks[i])
    newlist.append(mavg)
print(newlist)
count = 0
for i in newlist:
    if i>70:
        for
        count+=1
print(str(count) + " meet the requirement" )


# In[ ]:


#i  think i also need to check tyhe individual course marks
#or it is to check only the avg?
#lemme try i will show u later wrong answer it was supposed to be 3 because  but failed on module so he wioll not be included


# In[117]:


def average(list):
    sum1 = sum(list)
    n=len(list)
    avg=sum1/n
    return avg
marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],
[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]

for i in marks:
    for j in i:
        if j>=50:
            
            newlist=[]
            for i in range(len(marks)):
                mavg=average(marks[i])
                newlist.append(mavg)
print(newlist)
count = 0
for i in newlist:
    if i>70:
        count+=1
print(str(count) + " meet the requirement" )


# In[113]:


def average(list):
    sum1 = sum(list)
    n=len(list)
    avg=sum1/n
    return avg


# In[136]:


marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],
[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]
count=0
for i in marks:
    passed = True
    for j in i:
        if j<50:
            passed=False
    if passed==True:
        #marks[0][0] we will loop through
        myaverage= average(i)
        #can i maybe increment count
        if myaverage>70:
            count+=1
            
print(count)
            
#how do we push


# In[129]:


#u may help then i want to check if avg is >70 to increment count

i want to make a new list then i will perform count on that new list
repeat #again plz


# In[ ]:




