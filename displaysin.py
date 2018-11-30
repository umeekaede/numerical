import matplotlib.pyplot as plt
import math

x_list=[]
y_list=[]

f=open('sin.dat', 'rt')

for line in f:
    data= line[:-1].split(' ')
    print(data)
    x_list.append(float(data[0]))
    y_list.append(float(data[1]))

#plt.plot(x_list, y_list)
#plt.plot(x_list, y_list,color='RED',linewidth=4.0)
plt.plot(x_list, y_list, color='BLUE',linewidth=3.0)
#plt.plot(x_list, y_list, 'o', linestyle='None')

#plt.xlabel('HV')
#plt.ylabel('Efficiency')
plt.xlabel('x')
plt.ylabel('y')


plt.grid(True)


plt.show()
