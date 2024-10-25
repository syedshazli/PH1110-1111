import matplotlib.pyplot as plt
import numpy as numpy
#Data, but with fake numbers
v = numpy.array([4.918, 4.503, 3.997, 3.576, 3.041, 1.730, 1.495, 1.122, .4511, .1198])
I = numpy.array([.01353, .01190, .009669, .007904, .005625, .0005569, .0005266, .0005871, .0005236, .0005841])

# m,b = numpy.polyfit(I,v,1)
#b = numpy.polyfit(I,v,1)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current

m, b = numpy.polyfit(I,v,1) #If linear looks like it's the line that fits best
plt.plot(I, m*I + b)

plt.plot(I,v, 'ro') #uses matplotlib to plot voltage vs current
plt.ylabel('Voltage (V)')
plt.xlabel('Current (A)')
plt.title('Voltage vs Current (LED)')
plt.show()
print('The slope is: ',m, 'so the equation of this line is V = ',m,'*I + ',b)
