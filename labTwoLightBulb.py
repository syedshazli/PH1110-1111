import matplotlib.pyplot as plt
import numpy as numpy
#Data, but with fake numbers
v = numpy.array([5.156,4.348,4.031,3.359,3.002,2.546,1.969, 1.523, 1.039, 0.5296])
I = numpy.array([.1826, .1658, .1589, .1434, .1348, .1228, .1064, .09242, .07520,.05372])

# m,b = numpy.polyfit(I,v,1)
#b = numpy.polyfit(I,v,1)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current

m, b = numpy.polyfit(I,v,1) #If linear looks like it's the line that fits best
plt.plot(I, m*I + b)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current
plt.ylabel('Voltage (V)')
plt.xlabel('Current (A)')
plt.title('Voltage vs Current (Lightbulb)')
plt.show()
print('The slope is: ',m, 'so the equation of this line is V = ',m,'*I + ',b)
