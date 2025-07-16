# import random

# def get_choices(): #funct
#     player_choice =input("Enter a choice(rock,paper,scissors): ")  #var+input
#     options = ["rock","paper","scissors"] #list
#     computer_choice=random.choice(options)
#     chocies={"player":player_choice,"computer":computer_choice}    #dict 
#     return chocies

# # choices=get_choices()
# # print(choices)

# def check_win(player, computer): #func+arguement
#     print(f"You chose {player},computer chose {computer}")
#     if player == computer:
#         return "Its a tie!"
#     elif player =="rock":
#       if computer =="scissors":
#        return "Rock smashes scissors! You win"
#       else:
#        return "paper covers rock! You lose😔"
#     elif player =="paper":
#       if computer =="rock":
#        return "paper covers rock! You win"
#       else:
#        return "scissors cuts paper! You lose😔"
#     elif player =="scissors":
#       if computer =="paper":
#        return "scissors cuts paper! You win"
#       else:
#        return "rock smashes scissors! You lose😔"
#     # return[player, computer]

# choices = get_choices()
# result = check_win(choices["player"], choices["computer"])

# print(result)


# name = "Venkatesh"
# age = float(20)

# print(isinstance(name,str))
# print(isinstance(age,float))

age=20
age*=20
print(age)
