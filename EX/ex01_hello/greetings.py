"""EX01 Greetings."""

# ask for a greeting
greeting = input("Enter a greeting: ")
# ask for a recipient
recipient = input("Enter a recipient: ")
# ask how many times to repeat
repeat = int(input("How many times to repeat: "))

print(f"{greeting} {recipient}! " * int(repeat))
