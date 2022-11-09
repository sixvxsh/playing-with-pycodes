import random 

guess_pc = random.randint(1,99)
guess_count = 0
guess_limit = 3
guess = int(input('guess: '))
guess_count += 1
while guess_count < guess_limit:
    if guess < guess_pc:
        print('mine is bigger')
        guess = int(input('guess: '))
        guess_count += 1
    if guess > guess_pc:
        print('mine is smaller')
        guess = int(input('guess: '))
        guess_count += 1
    if guess == guess_pc:
        print("you won")
        break
     
else:
    print('Sorry , you failed!')
    print (f"the guess pc was", guess_pc)
        

