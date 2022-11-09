# Convert pounds to kilos and vice versa
weight = int(input("weight: "))
unit = input('(L)bs or (K)g:')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")

else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
    
# form input for username and password
name = input("what's your name: ")
if len(name) < 3:
    print("Error: Name must be at least 3 characters")
    name = input("what's your name: ")
elif len(name) > 50:
    print("Error: Name can be a maximum of 50 characters")
    name = input("what's your name: ")
else:
    print("name is fine ")
    password = input("what's your password:  ")

print('registered successfully!')



# Divide two numbers by each other
print('give two number for division')
print('with q you can quit the program')
while True:
    adad_aval = input('\nadad_aval: ')
    if adad_aval == 'q':
        break
    adad_dovom = input('\nadad dovom: ')
    if adad_dovom == 'q':
        break
    try:  
        hasel_taghsim = int(adad_aval) / int(adad_dovom)
    except ZeroDivisionError:
        print('taghsim bar zer0 emkan pazir nist')
    else:    
        print(hasel_taghsim)
        break


# nested_loop
for x in range (2):
    for y in range(2):
        print(f"({x},{y})")


numbers = [5 , 2 , 5 , 2 , 2]

for x_count in numbers: 
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)