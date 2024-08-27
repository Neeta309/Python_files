original_string = "hello"
reversed_string = ""

#Using loop
for letter in original_string: 
    reversed_string =  letter + reversed_string
print(reversed_string)  # Output: "olleh"

#Using slicing
reversed_string = original_string[::-1]
print(reversed_string)

#reversed() function
# reversed_string = reversed(original_string)
print(reversed(original_string))


#reversed() with join function
reversed_string = ''.join(reversed(original_string))
print(reversed_string)

