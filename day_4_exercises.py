# #EXERCISE 1
# # food_items = ['ribeye_steak', 'collard_greens', 'white potatoes']
# # non_food_items = ['mouthwash', 'hand_towels', 'dishwashing_liquid']



# # item = input("Enter a grocery item:")

# # if item in food_items:
# #     print(f"{item} is a food item")
    
# # elif item in non_food_items:
# #     print(f"{item} is a non-food item")

# # else:
# #     print("Unknown item")

# #EXERCISE 2: MAKING A BURGER WITH A WHILE LOOP
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}]
# shopping_list = []
# budget = 27.50
# total_cost = 0
# index = 0

# while total_cost <= budget and index < len(items_list):
#     item = items_list[index]
#     item_cost = item['cost' ] * item['amount']
#     if total_cost + item_cost <= budget:
#         shopping_list.append(item['name'])
#         total_cost += item_cost
#     index += 1

# print(shopping_list)   


# #EXERCISE 3: EXTENDING LOGIC WITH NESTING
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}]
# shopping_list = []
# budget = 27.50
# total_cost = 0
# index = 0

# while total_cost <= budget and index < len(items_list):
#     item = items_list[index]
#     item_cost = item['cost' ] * item['amount']
#     if total_cost + item_cost <= budget:
#         shopping_list.append(item['name'])
#         total_cost += item_cost
        
#     for item_name in shopping_list:
#         print(item_name)
#     print('-----------')
#     index += 1
# print(shopping_list)


#EXERCISE 4: BREAKING THEE LOOP
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}]
# shopping_list = []
# budget = 27.50
# total_cost = 0
# index = 0

# while total_cost <= budget and index < len(items_list):
#     item = items_list[index]
#     item_cost = item['cost' ] * item['amount']
#     if total_cost + item_cost <= budget:
#         shopping_list.append(item['name'])
#         total_cost += item_cost
        
#     for item_name in shopping_list:
#         print(item_name)
#     print('-----------')
    
#     if ('burger buns' in shopping_list and
#         'fries' in shopping_list and 'burger patties' in shopping_list):
#         print(f'We can make burgers and fries for ${total_cost}!')
#         break
#     index += 1
# print(shopping_list)


# #EXERCISE 5: ERROR HANDLING WITH TRY-EXCEPT
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}]
# shopping_list = []
# budget = 27.50
# total_cost = 0
# index = 0

# while total_cost <= budget and index < len(items_list):
#     try:
#         item = items_list[index]
#     except: TypeError
#     print('ERROR: The index must be an integer')
#     break

# print(shopping_list)

#EXERCISE 6: CUSTOMIZE YOUR SCRIPT

# items_list = [
#     {"name": "ground_beef", "cost":8.56, "amount": 1},
#     {"name": "onion", "cost":1.66, "amount": 1},
#     {"name": "canned_tomato_sauce", "cost":1.05, "amount": 1},
#     {"name": "canned_kidney_beans", "cost":1.31, "amount": 1},
#     {"name": "stewed_tomatoes", "cost":1.35, "amount": 1},
#     {"name": "chili_powder", "cost":3.87, "amount": 1},
#     {"name": "garlic_powder", "cost":2.75, "amount": 1}]
# shopping_list = []
# budget = 27.50
# total_cost = 0
# index = 0

# while total_cost <= budget and index < len(items_list):
#     item = items_list[index]
#     item_cost = item['cost' ] * item['amount']
#     if total_cost + item_cost <= budget:
#         shopping_list.append(item['name'])
#         total_cost += item_cost
        
#     for item_name in shopping_list:
#         print(item_name)
#     print('-----------')
    
#     if ('ground_beef' in shopping_list and 'onion' in shopping_list and 'canned_tomato_sauce' in shopping_list and                      'canned_kidney_beans' in shopping_list and 'stewed_tomatoes' in shopping_list and 'chili_powder' in shopping_list):
#         print(f'We can make chili for ${total_cost:.2f}!')
#         break
#     index += 1
print(shopping_list)



