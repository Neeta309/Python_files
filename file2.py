# import file1

print("File2__name__=%s"%__name__)

if __name__ == "__main__":
  print("File2 is being run directly")
  
else:
  print("File2 is being imported")