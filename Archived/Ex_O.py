# __Challenge__

# Among the first 861 thousand square numbers, what is the sum of all the odd squares?

sum_of_squares = 0

for number in range(1, 861001):
    square = number**2
    if (square)%2 == 1:
        sum_of_squares += square

print("Sum of odd squares is:", sum_of_squares)