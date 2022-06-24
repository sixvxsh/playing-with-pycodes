commands = ''
started = False
while True:
    commands = input('> ').lower()
    if commands == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('car started')