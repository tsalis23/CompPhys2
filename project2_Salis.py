#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:27:38 2020

@author: bensalis
"""
import matplotlib.pyplot as plt
import numpy as np

import scipy.integrate as integrate

'''
gonna need inital values for our system before proceeding.
However, they needed to be normalized since they were given
in SI units.  
'''
v1_0 = 0
v2_0 = 0

'''
#Uncomment for first case, where 0.5 * m1 = m2
x1_0 = 3/5
x2_0 = 9/5
'''
'''
#Uncomment for second case, where m1 = m2
x1_0 = 1/2
x2_0 = 3/2
'''

#Uncomment for 3rd case, where .9 * m1 = m2
x1_0 = 19/37
x2_0 = 57/37

v1 = [v1_0]
v2 = [v2_0]

x1 = [x1_0] 
x2 = [x2_0]

t = [0]
dt = .1
lastStep = 100

'''
while the midpoint method requires an acceleration term
we already know that gbar is a normalized acceleration 
quantity with a value of 1. So we'll treat it as such
'''
idx = 0
while idx < lastStep:
    t += [t[idx] + dt]
    approx_v1 = v1[idx] - dt
    approx_x1 = x1[idx] + (dt*(approx_v1 + v1[idx])/2)
    approx_v2 = v2[idx] - dt
    approx_x2 = x2[idx] + (dt*(approx_v2 + v2[idx])/2)
    
    if approx_x1 > approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(x2[idx]))
        x1+=[x2[idx]]
        x2+=[x2[idx]]
        print(idx)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[idx] * -1) - dt
        bounce_x1 = x1[idx-1] + dt*(v1[idx -1] - v1[idx])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]
    
    idx += 1
  

'''
#Uncomment for 1st case
v1 += [-0.805]
v2 += [0.809]


i = 16
'''
'''
#Uncomment for 2nd case

v1 += [-0.53]
v2 += [1.48]
i = 15

'''

#Uncomment for 3rd case

v1 += [-1.432]
v2 += [.436]
i = 16

while i < lastStep:
    t+= [t[i] + dt]   
    approx_v1 = v1[i] - dt
    approx_x1 = x1[i] + (dt*(approx_v1 + v1[i])/2)
    approx_v2 = v2[i] - dt
    approx_x2 = x2[i] + (dt*(approx_v2 + v2[i])/2)
    
    if approx_x1 > approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(x2[i]))
        x1+=[x2[i]]
        x2+=[x2[i]]
        print(i)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[i] * -1) - dt
        bounce_x1 = x1[i-1] + dt*(v1[i -1] - v1[i])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]

    i += 1
    
''' 

#Uncomment for 1st case
v1 += [-0.624]
v2 += [0.767]
j = 31

'''
'''
#Uncomment for 2nd case
v1 += [-1.537]
v2 += [0.686]
j = 46
'''


#Uncomment for 3rd case
v1 += [-0.022]
v2 += [1.438]
j = 21

while j< lastStep:
    
    t+= [t[j] + dt]
    approx_v1 = v1[j] - dt
    approx_x1 = x1[j] + (dt*(approx_v1 + v1[j])/2)
    approx_v2 = v2[j] - dt
    approx_x2 = x2[j] + (dt*(approx_v2 + v2[j])/2)
    
    if approx_x1 > approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(approx_x1))
        x1+=[approx_x1]
        x2+=[approx_x1]
        print(j)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[j] * -1) - dt
        bounce_x1 = x1[j-1] + dt*(v1[j -1] - v1[j])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]
 
    j += 1


'''
#Uncomment for 1st case
v1 += [-0.426]
v2 += [0.868]
k = 47
'''
'''

#Uncomment for 2nd case
v1 += [0.381]
v2 += [1.035]
k = 52
'''

#Uncomment for 3rd case
v1 += [-1.484]
v2 += [0.741]

k = 52

while k< lastStep:
    t+= [t[k] + dt]
    approx_v1 = v1[k] - dt
    approx_x1 = x1[k] + (dt*(approx_v1 + v1[k])/2)
    approx_v2 = v2[k] - dt
    approx_x2 = x2[k] + (dt*(approx_v2 + v2[k])/2)
    
    if approx_x1 > approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(approx_x2))
        x1+=[approx_x2]
        x2+=[approx_x2]
        print(k)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[k] * -1) - dt
        bounce_x1 = x1[k-1] + dt*(v1[k -1] - v1[k])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]

    k += 1

'''
#Uncomment for 1st case
v1 += [-0.5]
v2 += [0.919]

r = 65
'''
'''
#Uncomment for 2nd case
v1 += [-1.151]
v2 += [0.605]

r = 74

'''


#Uncomment for 3rd case
v1 += [0.329]
v2 += [1.402]
r = 56

while r< lastStep:
    t+= [t[r] + dt]
    approx_v1 = v1[r] - dt
    approx_x1 = x1[r] + (dt*(approx_v1 + v1[r])/2)
    approx_v2 = v2[r] - dt
    approx_x2 = x2[r] + (dt*(approx_v2 + v2[r])/2)
    
    if approx_x1 >= approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(approx_x1))
        x1+=[approx_x1]
        x2+=[approx_x1]
        print(r)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[r] * -1) - dt
        bounce_x1 = x1[r-1] + dt*(v1[r -1] - v1[r])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]
       
    r += 1


'''

#Uncomment for 1st case
v1 += [-0.538]
v2 += [0.494]

b = 83

'''
'''
#Uncomment for 2nd case
v1 += [-0.331]
v2 += [0.887]

b = 83


'''

#Uncomment for 3rd case
v1 += [-1.449]
v2 += [0.579]
b = 85


while b < lastStep:

    approx_v1 = v1[b] - dt
    approx_x1 = x1[b] + (dt*(approx_v1 + v1[b])/2)
    approx_v2 = v2[b] - dt
    approx_x2 = x2[b] + (dt*(approx_v2 + v2[b])/2)
    
    if approx_x1 > approx_x2:
        print("Ball One Collision Velocity: "+str(approx_v1))
        print("Ball Two Collision Velocity: "+str(approx_v2))
        print("Collision Height: " + str(x1[b]))
        print(b)
        break

    elif approx_x1 >= 0:
        v1 += [approx_v1]
        x1 += [approx_x1]
        
        
    elif approx_x1 < 0:
        bounce_v1 = (v1[b] * -1) - dt
        bounce_x1 = x1[b-1] + dt*(v1[b -1] - v1[b])/2 
        v1 += [bounce_v1]
        x1 += [bounce_x1]
    
    
    if approx_x2 >= 0:
        v2 += [approx_v2]
        x2 += [approx_x2]
    t+= [t[b] + dt]        
    b += 1

plt.plot(t,x1,'mo',label = "Position of Ball 1")
plt.plot(t,x2,'o',label = "Position of Ball 2")
plt.xlabel(" Normalized Time, t")
plt.ylabel("Normalized Postion, $X$")
plt.title("Position of Balls 1 and 2 as a function of Time, 3rd Case")
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.grid(b=None, which='major', axis='both')
plt.legend()
plt.show()
plt.close()



plt.plot(x2,v2,"o-")
plt.xlabel("Normalized Position")
plt.ylabel("Normalized Velocity")
plt.title("Poincare Section of Ball 2, 3rd Case")
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.grid(b=None, which='major', axis='both')
plt.legend()
plt.show()
plt.close()



x1avg = np.average(x1)
x2avg = np.average(x2)


print(x1avg)
print(x2avg)

print(len(x2))
tau = .1
tauList=[0]

val = 1
x1tau=[x1[1]]
x2tau=[x2[2]]


blank1 = [x1_0]
blank2 = [x2_0]
while val < 80:
    x1tau += [x1[val+1]]
    x2tau += [x2[val+1]]
    tauList += [t[val]] 
    blank1 += [x1[val]]
    blank2+= [x2[val]]
    val += 1


cA = np.subtract(x1tau, x1avg)
cB = np.subtract(blank1,x1avg)
Ct = integrate.simps(np.multiply(cA,cB),tauList) 

print(Ct)


