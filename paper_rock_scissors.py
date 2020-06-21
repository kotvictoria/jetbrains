import random
a = input()
b = random.randint(1,3)
#1 scissors, 2 paper, 3 rock
if a == "scissors" and b == 3:
    print("Sorry, but computer chose rock")
elif a == "scissors" and b == 2:
    print("Well done. Computer chose paper and failed")
elif a == "scissors" and b == 1:
    print("There is a draw (scissors)")

elif a == "paper" and b == 1:
    print("Sorry, but computer chose scissors")
elif a == "paper" and b == 3:
    print("Well done. Computer chose rock and failed")
elif a == "paper" and b == 2:
    print("There is a draw (paper)")

elif a == "rock" and b == 2:
    print("Sorry, but computer chose paper")
elif a == "rock" and b == 1:
    print("Well done. Computer chose scissors and failed")
elif a == "rock" and b == 3:
    print("There is a draw (rock)")