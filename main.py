print('Welcome to the Elite 101 Chatbox!!')
name = input('Please Enter Your name:  ')

print(f'Hello, {name}!!')
age = input('How old are you??  ')

print(f'Wow, {age} is a great age to be!! \nHow can I help you today?')

# option menu
print('\nPlease choose from the following options: \n1. Placeholder Option 1 \n2. Placeholder Option 2 \n3. Placeholder Option 3 \n4. Exit the conversation')
  
choice = input('Enter your choice number: ')

if choice == '4': 
  print(f'Thank you for chatting with the Elite 101 Chatbox, {name}!! \nBye Now!')
else:
  print('Sorry, I did not understand your choice. Please start again.')
  