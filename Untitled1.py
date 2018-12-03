
# coding: utf-8

# In[1]:

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


# In[3]:

a=input("请输入")
1+1


# In[4]:

a


# In[5]:

a=input('请输入')


# In[6]:

a


# In[7]:

a=input('请输入')
a


# In[24]:

ord('1')


# In[36]:

print('hi,%s, I have %d dollars'%('zhangsan',20))


# In[41]:

word=['a','b,c','d']


# In[43]:

word[-1]


# In[48]:

for z in word:
    print(z)


# In[17]:


import random
def ra(a):
    if a>3:
        a=random.random()
    else:
        a= 0
    return a 




# In[18]:

ra(4)


# In[126]:

#计算x 的n 次方
def pow(x,n):
    i=1
    x1=x
    while i<n :
        x=x*x1
        i=i+1
    return x


# In[127]:

pow(3,4)


# In[148]:

def c(m):
    sum = 0
    for n in m:
        sum = sum + n * n
    return sum


# In[149]:

c(1)


# In[15]:

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)


# In[16]:

fact(10)


# In[177]:

def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)


# In[178]:

fact_iter(5,1)


# In[189]:

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.show()


# In[63]:

import matplotlib.pyplot as plt
from numpy.random import randn

plt.plot(randn(1000).cumsum(),'o--',label="o--")
plt.plot(randn(1000).cumsum(),'o-',label='o-')
plt.plot(randn(1000).cumsum(),'k-',label='k-')
plt.plot(randn(1000).cumsum(),'k.',label='k.')

plt.legend()
plt.show()


# In[7]:

import numpy as np
a=[3,1,24,0,5]
b=np.array(a)


# In[13]:

print (b.dtype)


# In[67]:

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')

plt.show()


# In[72]:

if not(6%4)


# In[ ]:



