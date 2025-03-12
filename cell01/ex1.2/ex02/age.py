current_age = 17
user_input = input(f"Enter your current age (default: {current_age}): ")

if user_input.isdigit():
    current_age = int(user_input)

my_age = current_age + 42

print(my_age)