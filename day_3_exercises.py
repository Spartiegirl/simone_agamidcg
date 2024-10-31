#EXERCISE 1 WORKING WITH TUPLES

# fruit = ('apples', 1.50, 30)
# bread = ('crossiants', 3.50, 15)
# vegetable = ('eggplants', 2.50, 15)
# grocery_list=[]
# grocery_list.append(fruit)
# grocery_list.append(bread)
# grocery_list.append(vegetable)
# print(grocery_list)

# total_cost_apples = 1.50 * 30
# print(f'Total cost of apples: ${total_cost_apples: .2f}')
# total_cost_crossiants = 3.50 * 15
# print(f'Total cost of crossiants: ${total_cost_crossiants: .2f}')
# total_cost_eggplants = 2.50 * 15
# print(f'Total cost of eggplants: ${total_cost_eggplants: .2f}'}

#Exercise 2 Working with Dictionaries
# apple_dict = {'name': 'apple', 'price': .75, 'quantity': 50}
# lettuce_dict = {'name': 'lettuce', 'price': .95, 'quantity': 25}
# bagel_dict = {'name': 'bagel', 'price': 1.25, 'quantity': 45}

# apple_dict['total_cost'] = apple_dict['price'] * apple_dict['quantity']

# print(f'The total cost of the apples: ${apple_dict['total_cost']:.2f}')

# lettuce_dict['total_cost'] = lettuce_dict['price'] * lettuce_dict['quantity']
# print(f'The total cost of lettuce: ${lettuce_dict['total_cost']:.2f}')

# bagel_dict['total_cost'] = bagel_dict['price'] * bagel_dict['quantity']
# print(f'The total cost of bagels: ${bagel_dict['total_cost']:.2f}')

#EXERCISE 3 SLICING AND SORTING A LIST
# num_list = [16, 47, 1, 3, 5, 9, 15, 2]
# print(num_list[2:])
# print(num_list[:4])
# print(num_list[-3])
# num_list.sort(reverse=True)
# print(num_list)
# print(len(num_list))

#EXERCISE 4 SETS OPERATIONS
dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}

dairy_products.add('ice_cream')
print(dairy_products)

desserts.add('ice_cream')
print(desserts)

dairy_products.remove('milk')
print(dairy_products)

desserts.remove('jello')
print(desserts)

print(dairy_products.intersection(desserts))