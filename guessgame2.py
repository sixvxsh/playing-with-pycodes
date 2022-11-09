import random

guess_pc = random.randint(x=1 , y=99)
print(guess_pc)
mymind = input('tell a thing to computer: ')
my_numb_is_smaller = 's'
my_numb_is_bigger = 'b'
equal = 'e'

while mymind != 'e':
    if mymind == 's':
        guess_pc1 = random.randint( 1 , guess_pc)
        print(guess_pc1)
        mymind = input('tell a thing to computer: ')
    if mymind == 'b':
        guess_pc2= random.randint( guess_pc , 99)
        print(guess_pc2)
        mymind = input('tell a thing to computer: ')


print('we win')


    

    




    
    

