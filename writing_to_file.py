import re

# data to be outputted
data = ['Does', 'this', 'work']

# get filename, can't be blank or invalid
# assume valid data for now

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a filename: ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == "":
            problem = "(no spaces allowed)"

        else:
            problem = f"(no {letter}'s allowed"
        has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            print(f"Invalid filename - {problem}")
        else:
            print("you entered a valid filename")

# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")




