import random
"""
   1 = stone
  -1 = paper
   0 = scissor
"""
def Game():
    while True:
        try:
            
            comp = random.choice([1, -1, 0])

            your_choice = input("enter your choice: ('s', 'p', or 'c'): ")
            you_dict = {"s": 1, "p": -1, "c": 0}
            reverse_dict = {1: "Stone", -1: "Paper", 0: "Scissor"}

            you = you_dict[your_choice]
#Now we have 2 numbers(variables): comp and you
            print(f"Your choice: {reverse_dict[you]}\nComputer's choice: {reverse_dict[comp]}")
#Game draw condition
            if comp == you:
               print("Game draw")
        
            else:
                if comp == 1 and you == -1:
                    print("You Won!")
                elif comp == 1 and you == 0:
                    print("You Lose!")
                elif comp == -1 and you == 0:
                    print("You Won!")
                elif comp == -1 and you == 1:
                    print("You Lose!")
                elif comp == 0 and you == -1:
                    print("You Lose!")
                elif comp == 0 and you == 1:
                    print("You Won!")
                
                    continue
        except:
            print("Please choose a valid letter: ('s', 'p', or 'c')\nThankyou")
            
Game()
        
