import matplotlib.pyplot as plt
gas = ['paper', 'Yard trimming', 'Food scraps', 'plastics', 'Others', 'Metals', 'Rubber', 'Wood', 'Glasses' ]
value = [28.5, 13.4, 13.9, 12.4, 3.4, 9.0, 8.4, 6.4, 4.6]
plt.axis("equal") # if graph pixels are not showing correctly  then use this function it will correct that problem
plt.pie(value, labels=gas, explode=[0.03, 0, 0, 0, 0.5, 0, 0, 0, 0], autopct='%0.2f%%', startangle=0)
plt.title('Total MSW Generation')
plt.show()