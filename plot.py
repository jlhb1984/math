import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

pi=math.pi
an=[]
bn=[]
serie_f=[]
#T=float(input("Type T value: "))
T=255
w=(2*pi)/T

a0=1/T
n=1
tiempo=0.1
for i in range(0,5):
    #an[i]=
    an.append((-(1/(n*pi)))*(math.sin(2*pi*n)-math.sin(1.992*pi*n)))
    bn.append(((1/(n*pi)))*(math.cos(2*pi*n)-math.cos(1.992*pi*n)))
    n=n+1
print(an)
print(bn)

t=np.linspace(0,514,1000)
#y=(an[0]*math.sin(w*t*1)+bn[0]*math.cos(w+t*1))
y=(a0+an[0]*np.cos(w*t*1)+bn[0]*np.sin(w*t*1)+
      an[1]*np.cos(w*t*2)+bn[1]*np.sin(w*t*2)+
      an[2]*np.cos(w*t*3)+bn[2]*np.sin(w*t*3))
plt.plot(t,y)
plt.show()


