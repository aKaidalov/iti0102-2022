"""Print Hello."""

# ask for a name
name = input("What is your name")
# ask for first random number
num1 = int(input(f"\nHello, {name}! Enter a random number: "))
# ask for second random number
num2 = int(input("\nGreat! Now enter a second random number: "))
# print out sum
print(f"\n{num1} + {num2} = " + str(num1 + num2))