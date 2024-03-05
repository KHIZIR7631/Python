# get input from user
string = input("Enter a string: ")

# initialize a variable to store the count
count = 0

# iterate through each character in the string
for char in string:
    # if the character is an integer, increment the count
    if char.isdigit():
        count += 1

# display the count of integers in the string
print("The string contains", count, "integers.")