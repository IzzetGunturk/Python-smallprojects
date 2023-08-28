import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+.<>"

own_character = input("What would you choose for a name? ")
string = lower + upper + numbers + symbols
length = int(input("How Many Characters Do You Want Your Password To Be: "))
password = own_character + "".join(random.sample(string, length))

print("Here Is Your Password:", password)