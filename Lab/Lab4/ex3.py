import random

computer = random.randint(0,2)
user = int(input("scissor(0), rock(1), paper(2):"))
option = ["scissor", "rock", "paper"]
if computer == 0 and user == 0:
    print(f"The computer is {option[0]}. You are {option[0]} too. It is a draw")
elif computer == 1 and user == 0:
    print(f"The computer is {option[1]}. You are {option[0]}. You lose")
elif computer == 2 and user == 0:
    print(f"The computer is {option[2]}. You are {option[0]}. You won")
elif computer == 0 and user == 1:
    print(f"The computer is {option[0]}. You are {option[1]}. You won")
elif computer == 0 and user == 2:
    print(f"The computer is {option[0]}. You are {option[2]}. You lose")
elif computer == 1 and user == 1:
    print(f"The computer is {option[1]}. You are {option[1]} too. It is a draw")
elif computer == 1 and user == 2:
    print(f"The computer is {option[1]}. You are {option[2]}. You won")
elif computer == 2 and user == 1:
    print(f"The computer is {option[2]}. You are {option[1]}. You won")
elif computer == 2 and user == 2:
    print(f"The computer is {option[2]}. You are {option[2]} too. It is a draw")
else: 
    print("error")