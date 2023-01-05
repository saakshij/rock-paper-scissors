import random
print("This is Rock, Paper, Scissors! You probably know that since you are here but lets recap the rules. You will have to choose rock, paper or scissors. You choose the number of rounds. Remember, Rock beats Scissors, Scissors beats Paper and Paper beats Rock. This will be randomly generated so you will have no clue what the computer will choose A.K.A your opponent. Have fun! \n")
rep = True
while rep == True: 
  num = 0
  user_point = 0
  comp_point = 0
  rounds = 0
  tie = 0
  rounds = int(input("How many rounds would you like to play? : "))
  while num < rounds:
    while True: 
      ran = random.randint(1,3)
      user = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors : "))
      if user == 1 or user == 2 or user == 3: 
        break
      else: 
        print("Wrong input! Try again.")
    if user == 1:
      if ran == 2:
        comp_point += 1
      elif ran == 3:
        user_point += 1
      elif ran == 1: 
        tie += 1
    if user == 3:
      if ran == 1:
        comp_point += 1
      elif ran == 2:
        user_point += 1
      elif ran == 3: 
        tie += 1 
    if user == 2:
      if ran == 1:
        user_point += 1
      elif ran == 3:
        comp_point += 1
      elif ran == 2:
        tie += 1
    num += 1
    
 # print("The number of points you have: {}".format(user_point))
  #print("The number of points the computer has: {}".format(comp_point))
  #print("The number of ties you and the computer had in this game: {}".format(user_point))
  
  if user_point > comp_point: 
    print("Your points : {}".format(user_point))
    print("Computer's points : {}".format
    (comp_point))
    print("Number of ties : {}".format(tie))
    print("Y O U   H A V E    W O N!   Y O U    P R O B A B L Y    J U S T   G O T   L U C K Y!")
  elif user_point == comp_point: 
    print("Your points : {}".format(user_point))
    print("Computer's points : {}".format
    (comp_point))
    print("Number of ties : {}".format(tie))
    print("A  TIE! OHHH THAT SUCKS FOR YOU!")
  else:
    print("Your points : {}".format(user_point))
    print("Computer's points : {}".format(comp_point))
    print("Number of ties : {}".format(tie))
    print("YOU  L O S T  T O  A C O M P U T E R      W H A T   A    R E G R E T!")

  replay = input("\nWould you like to try again? Y for yes, N for no : ").lower()
  if replay == 'y':
    rep = True
  elif replay == 'n':
    rep = False
   
