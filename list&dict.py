# Find the number of vowels in the word
w = input('write a thing :   ')
v = ['a', 'i', 'o', 'e', 'u']
found = {}

for letter in w:
    if letter in v:
        found.setdefault(letter , 0)
        found[letter] += 1
for k, v  in found.items():
    print(k, 'was found' , v , 'time(s).')


# Convert numbers to string 
numbers = {
    '1':'one', '2':'two', '3':'three', '4':'four' , '5':'five',
    '6':'six' , '7':'seven', '8':'eight' , '9':'nine'
    }
numb = input('give me a number between 0-9: ')
output = ""
for ch in numb:
    output += numbers.get(ch) + ' '
print(output)
        

# workin with list
numbers = [15,7,54,78,1,5,8,45]

print(8 in numbers)
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [5 , 4 , 6 , 11 , 19]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

# working with set
w = input (' write a thing :')
v = set('aeiou')
found = v.intersection(set(w))

for i in found:
    print(i)
 
w = input('write a thing :   ')
v = {'a', 'i', 'o', 'e', 'u'}
#or v= set('aeiou')

found = v.difference(set(w))
for vowel in found:
    print(vowel)


# working with list method
phrase = '!Salam va vaght bekheyr !'
ph_list = list(phrase)
print(phrase)
print(ph_list)
for i in range(2):
    ph_list.pop()
ph_list.pop(0)


ph_list.remove('v')
ph_list.remove(' ')

ph_list.insert(2 , ph_list.pop(15))
ph_list.insert(3, ph_list.pop(16))
ph_list.insert(4, ph_list.pop(13))
ph_list.insert(5, ph_list.pop(6))
ph_list.insert(6, ph_list.pop(19))


for i in range(13):
    ph_list.pop()
new_phrase = ''.join(ph_list)
print(ph_list)
print(new_phrase)