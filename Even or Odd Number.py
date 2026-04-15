# Write a Python program that asks the user to enter a number.
# Your program should print "Even" if the number is even, and "Odd" if thenumber is odd

number = float(input("Hey user! Enter a Random Number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("Even" if number % 2 == 0 else "Odd")