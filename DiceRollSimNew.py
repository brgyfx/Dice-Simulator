#DiceRollingSimulator
import random
import time
dice = random.randint(0,9)
count = 0
count_to = 10
response = input("Would you like to roll a dice? ")
if response == "yes":
    times = int(input("How many times would you like to roll a dice? "))
    count_to = times
while response == "yes" and count < count_to:
    print("You rolled a {}!".format(random.randint(0,9)))
    count = count + 1
    time.sleep(1)
