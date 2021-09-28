import matplotlib.pyplot as plt
import numpy as np
company = ['TechSrijan', 'Google', 'tcs', 'Microsoft']
revenue = [500, 10000, 2000, 1500]
profit = [1000, 15000, 3000, 8000]

xpos= np.arange(len(company))
#print(xpos)
plt.bar(xpos-0.2, revenue, width=0.4, color='green', label='revenue')
plt.bar(xpos+0.2, profit, width=0.4, color='blue', label='Profit')
plt.xlabel('company name')
plt.ylabel('Revenue in Millions')
plt.xticks(xpos, company)
plt.title("Company Profit bar chart")
plt.legend(shadow='True')
plt.show()