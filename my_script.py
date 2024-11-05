# my_list = [0, 1, 2, 3, 4, 5]
# print(my_list[1:4])
# print(my_list[:3])
# print(my_list[2:])
# print(my_list[0:5:2])
# print(my_list[-3:])
# my_favorite_movies =['And Justice for All', 'Annie Hall', 'The Equalizer', 'Outlaw of Josey Wales', 'Rocky' ]
# my_favorite_movies.append('Star Wars')
# print(my_favorite_movies)
# my_favorite_movies.remove('Annie Hall')
# print(my_favorite_movies)
# my_list = (0, 1, 2, 3, 4, 5)
# print(my_list[4:6])
# colors = ['red', 'blue', 'green']
# colors.insert(2, 'yellow')
# print(colors)
# colors.insert(5, 'purple')
# print(colors)
# dimensions = ( 30, 40, 63)
# print(dimensions[1])
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# print(numbers[2:6])
# fruits = ('apple', 'banana')
# vegetables = ('carrot', 'lettuce')
# groceries = (fruits + vegetables)
# print(groceries)

# book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
# print(book['author'])

# profile = {'name': 'Mary', 'age': 35, 'city': 'Philadelphia'}
# profile['city'] = 'London'
# print(profile)



# student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
# student.pop('subject')
# print(student)


# print(student.keys())
# print(student.values())

# student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
# student.pop('subject')
# print(student)

# print(student.keys())
# print(student.values())


# fruits = {'apple', 'banana', 'cherry'}
# fruits.add('orange')
# print(fruits)

# fruits.remove('banana')
# print(fruits)

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a.union(set_b))
# print(set_a.intersection(set_b))

# set_x = {'cat', 'dog', 'fish'}
# set_y = {'dog', 'bird'}
# print(set_x.difference(set_y))

#CONDITIONAL STATEMENTS
# number = int(input('Give me a number:'))
# if number % 2 == 0:
#     print('even')
# else: 
#     print('odd')
    
# temperature = int(input('What is the temperature in Celsius:'))
# if temperature < 15:
#     print('Cold')
# elif temperature in range(15, 25):
#     print('Warm')
# else :
#     print('Hot')

# age = int(input('Enter your age:'))
# citizenship = input('Are you a citizen (yes/no):').lower()
# if age >= 18:
#     if citizenship == 'yes':
#         print('Eligible to vote')
#     else:
#         print('Not eligible: Must be a citizen')
# else: 
#     print('Not eligible: Must be a 18 or older')

#FOR AND WHILE LOOPS
# items = ['bread', 'peanuts', 'milk', 'butter']
# for item in items:
#     print(item)      
    
# grocery_list = []

# print("Enter your grocery items (type 'done' to finish):")
# while True:
#     item = input('>')
    
#     if item .lower() == 'done':
#         break
#     elif item:
#         grocery_list.append(item)
#         print(f'Added {item} to your list.')
# print(grocery_list)

# grocery_list = {'apples': {'price': 1.50, 'quantity': 4},'bread': {'price': 2.50, 'quantity': 3},'ice cream': {'price': 3.00, 'quantity': 2}}
# for item, details in grocery_list.items():
#     total_cost = details['price'] * details['quantity']
#     print(f'{item}: ${total_cost: .2f}')

#LOOP CONTROL: BREAK, CONTINUE AND PASS  

# for item in  ['football', 'soccer', 'basketball', 'baseball']:
#     if item == 'baseball':
#        break
# print(f'{item} is popular')

# green_vegetables = ['broccoli', 'green_beans', 'turnips']
# orange_vegetables = []

# for item in ['carrots','broccoli', 'green_beans', 'turnips']:
#     if item in green_vegetables:
#         continue
#     orange_vegetables.append(item)
# print(orange_vegetables)

# for item in ['BMW', 'Buick', 'Telsa', 'Porsche']:
#     if item == 'Telsa':
#         pass
#     print(item)

