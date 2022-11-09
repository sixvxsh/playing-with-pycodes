commands = ''
started = False
while True:
    commands = input('> ').lower()
    if commands == 'start':
        if started:
            print('car is already started!')
        else:
            started = True
            print(' car started')
    elif commands == 'stop':
        if not started:
            print('car is already stopped!')
        else:
            started = False
            print('car stopped')
    elif commands == 'help':
        print("""
start -  start to the car
stop - stop to the car
quit - to quit
        """)
    elif commands == 'quit':
        break
    else:
        print("i don't understand that")
    