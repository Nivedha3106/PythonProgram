import getpass

ag = 'Y'

inp = ['rock', 'paper', 'sccissors']

while (ag == 'Y'):
    while True: 
        PlayerA = getpass.getpass("Player A, It's your turn now, enter your choice :")
        PlayerA = PlayerA.lower()
        if PlayerA in inp: 
            break
        else: 
            print("Player A, you have entered wrong words!!")
    while True: 
        PlayerB = getpass.getpass("Player B, It's your turn now, enter your choice :")
        PlayerB = PlayerB.lower()
        if PlayerB in inp: 
            break
        else: 
            print("Player B, you have entered wrong words!!")
    
    if ((PlayerA == "rock" and PlayerB == "paper") or (PlayerA == "paper" and PlayerB == "scissors") or (PlayerB == "scissors" and PlayerA == "rock")):
        print(PlayerB, "beats", PlayerA, "Congratulations PlayerB!!!")
    elif ((PlayerA =="rock" and PlayerB == "scissors") or (PlayerA == "paper" and PlayerB == "rock") or (PlayerA == "scissors" and PlayerB == "paper")):
        print (PlayerA, "beats", PlayerB, "Congratulations PlayerA!!!")
    elif (PlayerA == PlayerB):
        print ("It's tie")
        
    ag = input ("Do you wanna play again (Y/N):")

        
# ag = input ("Do you wanna play again (Y/N):")

