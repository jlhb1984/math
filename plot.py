import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import math

pi=math.pi
an1=[]
bn1=[]
an2=[]
bn2=[]

#T=float(input("Type T value: "))
T1=255
T2=105

w1=(2*pi)/T1
w2=(2*pi)/T2
a0=1/T1
n=1

for i in range(0,5):
    #an[i]=
    an1.append( (1/(n*pi)) * (math.sin(2*pi*n)-math.sin(1.9921*pi*n)) )
    bn1.append( (-1/(n*pi)) * (math.cos(2*pi*n)-math.cos(1.9921*pi*n)) )
    n=n+1
print(an1)
print(bn1)
n=1

for i in range(0,5):
    #an[i]=
    an2.append( (1/(n*pi)) * (math.sin(2*pi*n)-math.sin(1.9809*pi*n)) )
    bn2.append( (-1/(n*pi)) * (math.cos(2*pi*n)-math.cos(1.9809*pi*n)) )
    n=n+1
print(an2)
print(bn2)


t=np.linspace(0,4096,8192)
#y=(an[0]*math.sin(w*t*1)+bn[0]*math.cos(w+t*1))
y1=(1/255+an1[0]*np.cos(w1*t*1)+bn1[0]*np.sin(w1*t*1)+
      an1[1]*np.cos(w1*t*2)+bn1[1]*np.sin(w1*t*2)+
      an1[2]*np.cos(w1*t*3)+bn1[2]*np.sin(w1*t*3)+
      an1[3]*np.cos(w1*t*4)+bn1[3]*np.sin(w1*t*4)+
      an1[4]*np.cos(w1*t*5)+bn1[4]*np.sin(w1*t*5)
      )

y2=(1/105+an2[0]*np.cos(w2*t*1)+bn2[0]*np.sin(w2*t*1)+
      an2[1]*np.cos(w2*t*2)+bn2[1]*np.sin(w2*t*2)+
      an2[2]*np.cos(w2*t*3)+bn2[2]*np.sin(w2*t*3)+
      an2[3]*np.cos(w2*t*4)+bn2[3]*np.sin(w2*t*4)+
      an2[4]*np.cos(w2*t*5)+bn2[4]*np.sin(w2*t*5)
      )

plt.subplot(2,1,1)
plt.plot(t,y1)
plt.subplot(2,1,2)
plt.plot(t,y2)
plt.show()


