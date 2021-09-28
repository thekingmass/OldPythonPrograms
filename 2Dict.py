names=['pratik','praveen','hemant','anil','jaiky']
numbers=[8707347698,8853003095,9695702715,8934982310,6306577096]
phone= dict (zip(names,numbers))
print(phone)

#we can  also delete and add the data in our dictionary
phone['dilip']='9793308611'
phone['pintu']='8896884202'
print(phone)
del phone['jaiky']
print(phone)
print(phone['anil'])
