message = input("Please enter your message.")

if len(message) > 0:
  print("Thanks. Your message has been sent.")
  
else:
  print("Your message was blank.")
  new_message = input("Enter a new message.")
  
  if len(new_message) == 0:
    print("Message still empty. Existing.")