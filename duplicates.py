numbers = [2,2,4,4,6,8,4,6,1]
uniques = []

for x in numbers:
    if x not in uniques :
        uniques.append(x)
print(uniques)
print(numbers)