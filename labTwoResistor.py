import matplotlib.pyplot as plt
import numpy as numpy
#Data, but with fake numbers
v = numpy.array([5.021, 4.497, 4.009, 3.474, 2.929, 2.578, 1.959, 1.548, 1.069, 0.5388])
I = numpy.array([.5126, .4608, .4107, .3554, .2989, .2625, .1990, .1571, .1084, .05452])

# m,b = numpy.polyfit(I,v,1)
#b = numpy.polyfit(I,v,1)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current

m, b = numpy.polyfit(I,v,1) #If linear looks like it's the line that fits best
plt.plot(I, m*I + b)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current
plt.ylabel('Voltage (V)')
plt.xlabel('Current (A)')
plt.title('Voltage vs Current (Resistor)')
plt.show()
print('The slope is: ',m, 'so the equation of this line is V = ',m,'*I + ',b)
