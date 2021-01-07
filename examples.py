# comment

"""Welcome to Python"""


""" Data Types """
name = 'Lev'
age = 32
is_old = False
sei_1019 = True

print(name)

"""Methods for a string"""

sentence = 'Today is Nocole birthday'

nicole_birthday = sentence.split(' ')
print(nicole_birthday)

new_sentence = (" ").join(nicole_birthday)
print(new_sentence)

print(new_sentence.index('N'))

# Upper and Lower case

print(name.upper())
print(name.lower())

#replace

day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# in keyword
is_day = 'Day' in day_sentence
print(is_day)

# ranges

last_letter = day_sentence[-1]
nicole_range = day_sentence[9:15]
print(nicole_range)

# length

print(len(nicole_range))

# logical operatort
equal_to = 5 == 5
not_equal = 5 != 5

not True
not False

true_story = 5 <= 5


print(9 < 30)

print (5 < 4) or (6 > 30)
print ('Rome' =='rome' or 'Pete'=='pete')
print ('Rome' =='rome' and 'Pete'=='pete')
print ( 5 < age < 6)

print('' or 'Rome')
print(0 or 5)

real_name = name or False

# list (array)

numbers = [3,4,5,6]

print(len(numbers))

numbers[1]
print(numbers[-1])

print(numbers[len(numbers) -1 * 2])

rome = ['Rome']
print(rome * 5)

one_through_five = list(range(5))

print(one_through_five)

for i in range(len(one_through_five)):
    num = one_through_five[i]
    print(num)

anime = ['Your Name','Silent Voice', 'Spirited Away']    

for i in range(len(anime)):
    eiga = anime[i]
    print(eiga)

random_numbers = [45, 88, 4, 17]
sorted_numbers   = random_numbers.sort()
print(sorted_numbers)   
print(random_numbers)
random_numbers.append(33)

print(random_numbers)

reverse_random_numbers = random_numbers[::-1]
print(reverse_random_numbers)
thirty_three = random_numbers.pop()
print(thirty_three)

random_numbers.insert(0, 99)
print(random_numbers)

random_numbers.insert(1, 77)
print(random_numbers)

# help 

# print(help(random_numbers))

print(random_numbers.count(45))

# Dictionaries

car = {
    "color": 'Red',
    "make": 'Tesla',
    "model": "S",
    "all_colors": ['Red', 'White', 'Black'],
    "cool_car": True,
    "other_tesla_products": {
        "product": "Model 3",
        "product2": "Model X",
        "product3" : "Cybertruck"
    }
}

print(car)

print(car["make"])

car["speed"] = 200
print(car)

print(car.get("color"))

print(car.items())
print(car.keys())

# type conversion

int('33')

str(33)

float(33)

bool(0)
bool(3)

# string interpolation
# print('Hello my name is ' + name)
print(f"僕の名前は {name}")

def print_name(someone):
    return someone 

print(print_name('Will'))

def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:
        return 'You made it to adulthood'
    else: return 'You older, nice'   

print(old_enough(21))  

phrase = 'This {} is a phrase {}'
print(phrase.format('sentence', name))
print(phrase)

def add(time):
    return time + 1

print(add(1))    

def subtract(length):
    return length - 3

print(subtract(9))

def random(food):
    sentence = 'I like {}'
    return sentence.format(food)

print(random('pasta'))

