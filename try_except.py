# def AbyB(a, b):
#   try:
#     c = ((a + b ) / (a - b))
  
#   except:
#     print("a/b result is 0")
    
#   else:
#     print(c)
    
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
  
def div_zero():
  try:
    c = 5 / 0
  except:
    print("Zero Division Error.")
  else:
    print(c)
  
div_zero()