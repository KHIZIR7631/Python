import random
import time

print("Welcome to the Timed Math Challenge!")
print("You will have 30 seconds to answer as many equations as possible.")

# set timer for 30 seconds
start_time = time.time()
time_limit = 30

# set counter for correct answers
correct_count = 0

# loop for 30 seconds
while (time.time() - start_time) < time_limit:
    # generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # print the equation to the console
    equation = str(num1) + " * " + str(num2) + " = "
    # get input from the user
    answer = int(input(equation))
    # check if the answer is correct
    if answer == num1 + num2:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect.")

# display the final score
print("Time's up! You got", correct_count, "out of", time_limit, "equations correct.")