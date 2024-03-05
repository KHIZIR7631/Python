# get input from user
number = int(input("Enter a number: "))

# initialize a variable to store the reversed number
reverse = 0

# reverse the number
while(number > 0):
    remainder = number % 10     # get the last digit of the number
    reverse = reverse*10 + remainder    # add the last digit to the reverse number
    number = number // 10       # remove the last digit from the number

# display the reversed number
print("The reversed number is", reverse)