# This is a simple Python script that takes user input and writes it to a file

user_input = input("Enter some text: ")

with open('output.txt', 'w') as f:
    f.write(user_input)
