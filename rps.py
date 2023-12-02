import random
c=0
u=0
rounds=0
Tie_rounds=0
flag="Yes"
list=["rock","paper","scissors"]
# I am unable to paste the icons as the values in the dictionary part,in the code. When I am copying and pasting the icons,they are not getting reflected in the code. This is b'coz my old system  is n
ot supporting the pasting of the icons. That's why I've written only texts instead of icons.

dict={
      "rock":"Rock",
      "paper":"Paper",
      "scissors":"Scissors",
      "tie":"Tie",
      "win":"Win",
      "lose":"Lose"
      
}
while flag.lower()!="no":
  rounds+=1
  c_input=random.choice(list).lower()
  user_input=input("Which one do you want to choose:Rock,Paper or Scissors?").lower()
  if user_input not in list:
    print("Invalid input")
    continue
  print("Your choice:",dict[user_input],end=" ")
  print("and computer's choice is:",dict[c_input],end=" ")
  
  if user_input==c_input:
    print("It's a Tie",dict["tie"])
    Tie_rounds+=1
  elif (user_input=="rock" and c_input=="scissors") or (user_input=="paper" and c_input=="rock") or (user_input=="scissors" and c_input=="paper"):
    print("You Won",dict["win"])
    u+=1
  else:
    print("Computer won",dict["win"])
    c+=1
  flag=input("Do you want to continue ?")  
if flag=="no" or flag=="No" or flag=="NO":
  print("Total rounds:",rounds)
  print("No. Of Ties:",Tie_rounds)
  print("Your Score:",u,"and computer's score:",c)
if c>u:
  print("computer is winner")
else:
  print("You are Winner. Congratulations!",dict["win"])
  
    