# __Challenge__

# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

num1 = 1
num2 = 2
    
sum = 0

while (num1 < 4000000):
    if num1 % 2 == 0:
        sum += num1
    result = num1 + num2
    num1 = num2
    num2 = result

print(f"Sum of Even-Valued fibonacci terms: {sum}")