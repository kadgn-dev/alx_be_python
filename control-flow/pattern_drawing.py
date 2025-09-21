# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Draw the square pattern using a while loop and nested for loop
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next row
    row += 1
