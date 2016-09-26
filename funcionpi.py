
# coding: utf-8

# In[66]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=[0,15,15,50,150,180,180,200]
a=10
b=50
c=150
d=180

plt.xlabel('Valores de X')
plt.title('Funcion pi')

plt.grid()

def f(x,a,b,c,d):
    if ((x<a) | (x>=c)):
        ans=0
    if (x>=a)&(x<b):
         ans=(x-a)/(b-a)
    if (x>=b)&(x<d):
        ans=1
    if (x>=d)&(x<c):
        ans=1-(x-d)/(c-d)
    return ans


f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)
print func
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,f_vec(x,a,b,c,d))


# In[ ]:



