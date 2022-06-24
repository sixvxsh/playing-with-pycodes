try:
    age = int(input('age: '))
    income = 500
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('age can not be zero')
except ValueError:
    print('invalid value')


