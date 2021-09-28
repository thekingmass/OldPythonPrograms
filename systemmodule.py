import os
#os.system('notepad')# this will open a notepad file
#os.system('calc')# this will open calculator
'''
we can execute all dos command in this module
ex    os.system(mkdir program)
      this command well make a folder with the name 'program'
os.system('')
'''


'''
lets make folders using python
'''
#os.system('mkdir d:\\testing\\')
for i in range(1, 11):
    path = 'e:\\testing\\'
    folder_name = 'pratik' + str(i)
    total_path = path + folder_name
    create_folder = 'mkdir ' + total_path
    print(create_folder)
    #os.system(create_folder)