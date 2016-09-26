
# coding: utf-8

# In[2]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=[0,30,30,70,70,100]
a=30
b=70


plt.xlabel('Valores de X')
plt.title('Funcion Hombro Derecho')

plt.grid()

def f(x,a,b):

    if (x<a):
        ans=0
    if (x>=a)&(x<b):
         ans=(x-a)/(b-a)
    if (x>=b):
        ans=1
    return ans


f_vec = np.vectorize(f)
func=f_vec(x,a,b)
print func
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,f_vec(x,a,b))


# In[ ]:




# In[ ]:




# In[ ]:



