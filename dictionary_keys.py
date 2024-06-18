#Valid dictionary keys

my_dict = {
    "name" : "Alice",
    42 : "integer as key",
    3.14 : "float as key",
    (1, 2) : "tuple as key",
    True : "boolean as key"
}


#Invalid dictionary keys
#This will raise a TypeError because lists are mutable

# try:
#     invalid_dict = {[1, 2] : "lists as key"}

# except TypeError as e:
#     print(e)#unhashable type: 'list'
    

#Custom objects as keys
class MyKey:
    def __init__(self, value):
        self.value = value
        
        
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return isinstance(other, MyKey) and self.value == other.value
    
    
key1 = MyKey(1)#When both the objects having the same values then, python will overwrite the second value and when we print the custom_dict, then it will
key2 = MyKey(1)# print the address with the value2 only.
key3 = MyKey(2)# It will print the third value also but not all the threes, because here the argument given to the constructor is different, it will
#treated as a different key.

print(key1 == key2)

custom_dict = {key1 : "value1", key2: "value2", key3: "value3"}
print(custom_dict)
