# get input from user
numbers = list(map(int, input("Enter a list of numbers: ").split()))

# perform bubble sort
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            # swap the elements if the first element is greater than the second
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# display the sorted list
print("Sorted list is:")
print(numbers)