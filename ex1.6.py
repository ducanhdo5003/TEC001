numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)

print("The five greatest numbers are:")
print(numbers[:5])