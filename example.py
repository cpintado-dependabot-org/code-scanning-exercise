# This is a simple Python script that takes user input and writes it to a file

user_input = input("Enter some text: ")

with open('output.txt', 'w') as f:
    f.write(user_input)

# retrieve all rows of the users mysql database where user=user_input
cursor.execute("SELECT * FROM users WHERE user=%s", (user_input,))



