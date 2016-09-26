
# coding: utf-8

# In[ ]:




# In[269]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=[0,10,10,50,50,90,90,100]
a=10
b=50
c=90

plt.xlabel('Valores de X')
plt.title('Funcion Triangulo')

plt.grid()

def f(x,a,b,c):
    if ((x<a) | (x>=c)):
        ans=0
    if ((a<=x) & (x<b)):
         ans=(x-a)/(b-a);
    if ((b<=x) & (x<=c)):
        ans=1-(x-b)/(c-b);
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)
plt.plot(x,f_vec(x,a,b,c))



# In[ ]:




# In[ ]:



