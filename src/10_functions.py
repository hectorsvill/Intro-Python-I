# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE

def iseven(num):
    return (num % 2) == 0
# print(iseven(44))
# print(iseven(41))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

answer = "even" if iseven(num) == True  else "odd" 
print(answer)
