#Coffee Shop
#Simulator that calculates a receipt based on
#how many items the user wants to order.

#The price of a cup of coffee is $5 and the price of a muffin is $4.
#Calculate 6% tax on the subtotal.


#constants
price_coffee = 5.00
muffin_price = 4.00
tea_price = 3.00
croissants_price = 3.00
tax_rate = 0.06

#step 1: asking the user for the number of coffees and muffins
num_coffees = int(input('Number of coffees bought? '))
num_muffins = int(input('Number of muffins bought? '))
num_teas = int(input('Number of teas bought? '))
num_croissant = int(input('Number of croissants bought? '))

#step 2: calculate
coffee_cost = num_coffees * price_coffee
muffin_cost = num_muffins * muffin_price
tea_cost = num_teas * tea_price
croissant_cost = num_croissant * croissants_price
subtotal = coffee_cost + muffin_cost + tea_cost + croissant_cost

#step 3: calculate tax
tax = subtotal * tax_rate
total = subtotal + tax

#step 4: display receipt
print(' ')
print('*' * 30)
print('My Coffee and Muffin Shop')
print(' ')
print(f'{num_coffees} Coffees at ${price_coffee} each: ${coffee_cost: 6.2f}')
print(f'{num_muffins} Muffins at ${muffin_price} each: ${muffin_cost: 6.2f}')
print(f'{num_teas} Teas at ${tea_price} each: ${tea_cost: 6.2f}')
print(f'{num_croissant} Croissants at ${croissants_price} each: ${croissant_cost: 6.2f}')
print(f'6% tax: ${tax:6.2f}')
print('------------------------------')
print(f'Total: ${total:6.2f}')
print('*' * 30)

#step 5: thank the user
print(' ')
print('Thank you so much for visiting My Coffee Shop!! We hope to see you again soon!')
