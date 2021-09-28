import matplotlib.pyplot as plt
day = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
confirmed = [100, 250, 256, 50, 39, 354, 149]
recovered = [25,150,500, 6, 70, 98, 458]
#plt.plot(x, y, color='cornflowerblue', linewidth=2, linestyle='solid')
plt.plot(day, confirmed, "+r--", markersize='10', label='confirmed')
plt.plot(day, recovered, "+g--", markersize='10', label='recovered')
'''
 1.   supported values for line style :supported values are '-', '--', '-.', ':', '', ' ', '', '',
    '', 'dashdot', 'dotted'
'''
plt.xlabel('day')
plt.ylabel('cases')
plt.title('weekly corona cases')
plt.legend(shadow='true')
plt.savefig("first graph.png")
plt.grid()

plt.show()

