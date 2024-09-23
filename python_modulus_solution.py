# Python Modulus Solution

# Task 1: Find the remainder of a division problem
num1 = 10
num2 = 3
remainder = num1 % num2
print(f"The remainder of {num1} divided by {num2} is: {remainder}")

# Task 2: Checking for odd or even numbers
number = int(input("Enter an integer: (Example: 4 or 17)\n"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# Task 3: Converting hours to hours and minutes
total_minutes = 150
hours = total_minutes // 60 # floor division
minutes = total_minutes % 60 # modulus operator
print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")


# Task 4: Finding the last digit of a number
# When a number is divided by 10,
# the remainder is always the last digit of that number
number = 12345
last_digit = number % 10
print(f"The last digit of {number} is: {last_digit}")