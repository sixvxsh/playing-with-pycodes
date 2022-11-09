number = int(input('please input your number: '))
tedad_maghsom = 0
for i in range(1, number+1):
    if number % i == 0:
        tedad_maghsom += 1
if tedad_maghsom == 2:
    print('prime')
else:
    print('not prime')
