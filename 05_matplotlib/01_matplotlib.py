import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

#Function method
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

#Create Multi-plots
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()

#Object-oriented Method
# create figure object (empty canvas)
fig = plt.figure()

# define the location of the axes
# [ left, bottom, width, height ]

axes = fig.add_axes([ 0.1, 0.1, 0.8, 0.8 ])

axes.plot(x,y)
axes.set_xlabel( 'X Label' )
axes.set_ylabel( 'Y Label' )
axes.set_title( 'Set Title' )
plt.show()

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')
plt.show()

