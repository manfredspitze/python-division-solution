## Python: Division Operator

### On GitHub Online

---

- Create a GitHub repo named: **python-division**
    - Upload your project files to the repo
    - No need to share your repo with your teacher
    - Teacher will discuss your work with you during Teacher  Time

- Create a NEW folder on your workstation desktop
- Use VS Code to add your Python file to this new folder

---

### Add a Comment Block

```python
# Student name
# Current date
# Project name
```

### Your Tasks

- Use comments to label each task in your script
- Use f-strings to display the output for each task

#### Find Remainder

- Assign integers to two variables
- Define a third variable to store the result of the calculation
- Use the modulus operator (`%`) to tell Python to divide the first number by the second number and find the remainder
- Display both numbers and the remainder in your f-string

#### Odd or Even?

- Prompt the user to enter an integer (a number without a decimal point)
- Use an `if-else` statement and the modulus `%` operator to determine whether the integer is odd or even
  - HINT: If the number divided by 2 has no remainder, the number is even; otherwise, the integer is odd
- Print a sentence that tells the user if the integer is even or odd

#### Hours & Minutes

- Assign between 150 and 250 minutes to a variable named `total_minutes`
- Calculate and store the number of hours by using the floor division operator (`//`) to divide `total_minutes` by 60
- Calculate and store the number of minutes by using the modulus operator (`%`) to to divide `total_minutes` by 60
- Display a message that tells the user how many hours and minutes your total minutes is equal to
  - For example: You have 128 total minutes, so your message would read:
  - *128 total minutes is equal to 2 hours and 8 minutes.*

#### Calculate The Average

- Define three variables (such as `num1`, `num2` and `num3`)
- Either assign numbers to each variable or prompt the user to enter three numbers
- Define a third variable named `number_count` and assign it the number of numbers you're working with in this problem
- Use a set of parentheses ( ) and the division operator (/) to calculate the average of your three numbers
- Use an f-string to display all three numbers and the average of the three numbers

#### The Last Digit

- Assign a number (such as 44567 or 12492) to a variable named `number`
- Use the modulus operator (`%`) to divide `number` by 10; assign the result to a variable called `last_digit`
- Use an f-string to display a message that tells the user what the number and the last digit of the number are
