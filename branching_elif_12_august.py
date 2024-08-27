purchase_price = 42.70
sales_price = float(input("How much did you sell for? "))

price_diff = round(abs(sales_price - purchase_price), 2)


if price_diff > purchase_price:
  print("There was a huge change in value.")
  
elif price_diff < purchase_price / 10:
  print("There was very little change in value.")
  
if purchase_price <= sales_price:
  print("You made a profit of $ "+ str(price_diff))
  
else:
  loss = purchase_price - sales_price
  print("You had a loss of $ "+ str(price_diff))
  
print(purchase_price / 10)