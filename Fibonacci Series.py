# get input from user
n = int(input("Enter the number of terms: "))

# initialize the first two terms
n1, n2 = 0, 1

# check if the number of terms is valid
if n <= 0:
   print("Invalid input")

# generate the Fibonacci series
else:
   print("Fibonacci Series:")
   for i in range(n):
       print(n1)
       nth = n1 + n2
       # update values of n1 and n2 for next iteration
       n1 = n2
       n2 = nth