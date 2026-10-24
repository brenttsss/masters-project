import numpy as np

usr_input = int(input("Please enter a number: "))

print(f"Here is the {usr_input} times table")

for i in range(1, 13):
    print(f"{i} x {usr_input} = {i * usr_input}")