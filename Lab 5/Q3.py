# Create fruits, vegetables and animal products tuples. I. Join the three tuples and assign it to a variable called food_stuff_tp. II. Change the about food_stuff_tp tuple to a food_stuff_lt list III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. IV. Slice out the first three items and the last three items from food_staff_lt list V. Delete the food_staff_tp tuple completely 3. Create a set given below it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} A = {19, 22, 24, 20, 25, 26} B = {19, 22, 20, 25, 26, 24, 28, 27} age = [22, 19, 24, 25, 26, 24, 25, 24] I. Find the length of the set it_companies II. Add 'Twitter' to it_companies III. Insert multiple IT companies at once to the set it_companies IV. Remove one of the companies from the set it_companies V. What is the difference between remove and discard

# I. Create fruits, vegetables, and animal products tuples
fruits = ('guava', 'kiwi', 'avocado')
vegetables = ('cucumbre', 'potato', 'tomato')
animal_products = ('butter', 'chicken', 'milk')

# II. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# III. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# IV. Slice out the middle item or items from the food_stuff_lt list
n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1 : n//2 + 1]
else:
    middle_items = [food_stuff_lt[n//2]]
print("Middle item(s):", middle_items)

# V. Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

# VI. Delete the food_stuff_tp tuple completely
del food_stuff_tp