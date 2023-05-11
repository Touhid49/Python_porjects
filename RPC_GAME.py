exit=""
while exit != "e":
  print("Enter Your name to Start the Game")
  print()
  P1Name=input("Enter First player name:")
  p2Name=input("Enter Second player name:")
  print()
  from getpass import getpass as input
  print(" \U0001F600 Epic battle of R P S \U0001F600 ")
  print("")
  print("")
  print(P1Name)
  player1=input("What is your call for R P S :")
  print()
  print(p2Name)
  player2=input("What is your call for R P S:")
  print()
  if (player1=="R" or player1=="r") and (player2=="p" or player2=="P"):
    print("player1 take Rock and player2 take Paper")
    print("So winner is  \U0001F601",P1Name)
    
  elif (player1=="p" or player1=="P") and (player2=="p" or player2=="P"):
    print()
    print("player1 take Paper and player2 also take Paper")
    print("Oh this match is Draw! \U0001F910")
    
  elif (player1=="S" or player1=="s") and (player2=="p" or player2=="P"):
    print("player1 take Scissor and player2  take Paper")
    print("So winner is \U0001F601",P1Name)
  #part 2 from here  
  elif (player1=="P" or player1=="p") and (player2=="R" or player2=="r"): 
    print("player1 take paper and player2 take Rock")
    print("So winner is \U0001F601",P1Name)
    
  elif (player1=="R" or player1=="r") and (player2=="r" or player2=="R"):
    print()
    print("player1 take ROCK and player2 also take ROCK")
    print("Oh this match is Draw! \U0001F910")  
  #part 3 from here
  elif (player1=="S" or player1=="s") and (player2=="R" or player2=="r"): 
    print("player1 take Scissor and player2 take Rock")
    print("So winner is \U0001F601",p2Name)
  elif (player1=="S" or player1=="s") and (player2=="S" or player2=="s"): 
    print("player1 take Scissor and player2 also take Scissor")
    print("Oh this match is Draw! \U0001F910")
  elif (player1=="P" or player1=="p") and (player2=="S" or player2=="s"): 
    print("player1 take Paper and player2 also take Scissor")
    print("So winner is \U0001F601",p2Name)
    
  elif (player1=="R" or player1=="r") and (player2=="S" or player2=="s"): 
    print("player1 take Rock and player2 also take Scissor")
    print("So winner is \U0001F601",P1Name)     
  else:
   print("please type correctly \U0001F607")

  exit=input("press E to exit :")  