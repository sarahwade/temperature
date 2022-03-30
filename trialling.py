to_round = [1/1, 1/2, 1/3]
print(to_round)

for item in to_round:
    if item%1 == 0:
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(item))


# number checking
def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("Too Cold!!")
            else:
                return response

        except ValueError:
            print("Please enter a number")


# main routine
# run this code twice (for two valid responses in test plan)
number = temp_check(-273)
print(f"You chose {number}")

number = temp_check(-459)
print(f"You chose {number}")
