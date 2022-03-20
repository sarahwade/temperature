# quick component to degrees C to F.
# Function takes in value, does conversion and puts answer into a list

def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


def to_c(from_f):
    centigrade = (from_f * 5/9) - 32
    return centigrade


# Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = f"{item} degrees C is {answer} degrees F"
    converted.append(ans_statement)

print(converted)
