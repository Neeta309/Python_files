#__name__ is one such special variable. If the source file is executed as the main program, the interpreter sets 
#the __name__ variable to have a value "__main__ ". If this file is being imported from another module, __name__ will be set to the module's name.
#__name__ is a built-in variable which evaluates to the name of the current module.
#Thus it can be used to check whether the current script is being run on its own or being imported somewhere else
#By combining it with if statement

import file2
print("File1__name__=%s"%__name__)

if __name__ == "__main__":
  print("File1 is being run directly")

else:
  print("File1 is being imported")