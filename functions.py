def greet_user(first_name , last_name):
    print(f'Hi {first_name} {last_name} how are you?')
    print('Welcome,I am glad that you are reading my first test codes :)')

# optional kwargs
def func1(*args):
    for arg in args:
        print(arg)

    
def miangin(aval , *baghi):
    return (aval + sum(baghi)) /(1 + len(baghi))


def func2(**kwargs):
    for k, v in kwargs.items():
        print ('%s == %s' %(k , v))


def func3(arg1 , arg2 , arg3):
    print ('arg1' , arg1)
    print ('arg2' , arg2)
    print ('arg3' , arg3)


# When we have a number of files and want to count its arguments. 
def count_numb_arg(file_name):
    try: 
        with open(file_name) as file:
            content = file.read()
    except FileNotFoundError:
            print("this file is not exist")
            # pass
    else:
         arg = content.split()
         arg_numb = len(arg)
         print(f'this file {file_name} has {arg_numb} arg')
         
file_name = ['mydata.txt','mydatax','mydata2.txt','mydata3.txt','mydata4']
for file in file_name:
    count_numb_arg(file)


# Convert written characters to emojies
def emoji_converter(message):
    words = message.split(' ')
    emojies = {
    ":(" : "🙃",
    ":)" : "😀" ,
    }
    output = ""
    for word in words:
        output += emojies.get(word , word) + ' '
    return output


message = input('>>>')
print(emoji_converter(message))



# Counting down a number
def count_numb(a):
    if a <= 0:
     print('payan')
    else:
     print(a)
     count_numb(a-1)
     
# Counting an expression to an arbitrary number
def count_str(str , a):
    if a <= 0:
        return
    print(str)
    count_str(str, a-1)

