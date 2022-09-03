"""Cha-ching."""

# ask for sum
amount = int(input("Enter a sum: "))
coins = 0
# check how many 50 cent coins in sum
coins += int(amount / 50)
# find how many cents left
modulo = amount % 50

coins += int(modulo / 20)
modulo = modulo % 20

coins += int(modulo / 10)
modulo = modulo % 10

coins += int(modulo / 5)
modulo = modulo % 5

coins += int(modulo / 1)
# print out amount of coins needed
print(f"Amount of coins needed: {coins}")
