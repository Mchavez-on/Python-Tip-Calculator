def orderEntry():
  user_food = []
  stop = False
  while stop == False:
    food_item = input('what food item did you order? ')
    user_food.append(food_item)
    stopQ = input("have another item? ")
    if stopQ == 'no':
      stop = True
  return user_food

def orderPrice(finalFoodList):
  user_price = []
  for f in finalFoodList:
    food_price = float((input('what was the price of ' + f + ' ' )))
    user_price.append(food_price)
  return user_price

def taxes(finalFoodPrices):
  sum = 0
  for p in finalFoodPrices:
    sum += p
  tax = sum*.1
  withTax = sum + tax
  return withTax

def tipAndBill(subtotal):
  user_tip = float(input("Please enter your desired tip as a decimal "))
  total = round(subtotal + (subtotal*user_tip), 2)
  print("Your total cost plus your generous tip is $" + str(total))

def main():
  while True:
      finalChoice=input('Welcome to the Tip Calculator. Do you have items to enter (yes/no) ')
      if finalChoice=='no':
          break    
      elif finalChoice=='yes':
          finalFoodList = orderEntry()
          finalFoodPrices = orderPrice(finalFoodList)
          subtotal = taxes(finalFoodPrices)
          tipAndBill(subtotal)
          break
  print('Have a great day!')

main()
