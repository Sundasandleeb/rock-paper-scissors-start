import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock,paper,scissors]
user_choice= input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissor? \n")
choice = int(user_choice)
print ("You choosed")
print(game[choice])

#computer_choice = len(game)
computer_says = random.randint(0,2)
print("Computer choosed")
print(game[computer_says])



if choice==0 and computer_says ==2 :
  print("You won")


elif choice == 2 and computer_says == 1 :
  print("You won")
elif choice ==1 and computer_says == 0 :
  print("you won")
elif choice==computer_says :
  print("Match draw")
elif choice>=3 and choice<0 :
  print("you chosed invalid number")
else:
  print("Computer won")



    
      
      
      

  
  