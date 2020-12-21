print("Input 5 values")

# Define the empty list
listOfNumbers = []

# Get 5 values
for i in range(5):
    listOfNumbers.append(input())

# Print these values with their types
for i in range(5):
    # It will print that all their types are strings
    # because input() reads a string from standard input
    print(f'value: {listOfNumbers[i]} type: {type(listOfNumbers[i])}')