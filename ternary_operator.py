#Program to demonstrate conditional opeartor
a, b = 10, 20

#Copy value of a if a < b else copy b
min = a if a < b else b
print(min)

print((b,a)[a < b])

print({True:a, False:b}[a < b])

print((lambda: b, lambda: a)[a < b]())

print("Both a and b are equal" if a == b else
      "a is greater" if a > b else "b is greater")

#The above approach can be written as:
if a != b:
  if a > b:
    print("a is greater")
  else:
    print("b is greater")

else:
  print("Both a and b are equal")
  
#One more example for ternary operator
a = 45
b = 67

print(a, " is greater")if (a > b) else print(b, " is greater")

a, b = 98, 57
# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't 
# work if a is 0.
min_num = a < b and a or b# if we will not put the 'and' condition then it will be printing 'True'
print(min_num)