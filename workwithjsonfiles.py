import json 

file_name = 'mypassword.json'
try:
    with open (file_name) as file:
        password = json.load(file)
except FileNotFoundError:
    password = input('Enter your password: ')
    with open (file_name , 'w') as file:
        json.dump(password , file)
        print(f'your password is {password}')
    
else:
    print('your password was' , password)

        

file_name = 'mydata.txt'
with open(file_name) as file:
    lines = file.readlines()
    print(lines)

file_name = 'mydata.txt'
try: 
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
        print("this file is not exist")
else:
     arg = content.split()
     tedad_arg = len(arg)
     print(f'this file {file_name} has {tedad_arg} arg')