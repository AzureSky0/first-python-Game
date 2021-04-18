"""Application = "Simple Monster Combat Game{Monster tournament}"
_version_0.01
Target Users: anyone
Target System: GNU/Linux
Interface: Command-line
Objective:
    project: create a game where you can select desired Monster [Red,Blue] and have commands like [Start,Status,Fight,Forfeit,Quit,and fight commands as:
                                                                                                                                                               1.Punch - Attack Command
                                                                                                                                                               2.Shield - Defend Command
                                                                                                                                                               3.Elemental_Boost - Give a boost according to corresponding Monster ] 
    condition: should give output according to the Command and be easy to use. 
Data required : None
Desired_output : None
Maintainer : akshatsahu007@gmail.com"""

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55


#///////////////
#LINE SECTION: 

Fancy_Divider1="""|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=|"""
Fancy_Individual_Divider1="|==================================|"
Fancy_Line1="""|===================================================================================================================|
|===================================================================================================================|"""

#STATEMENT AND OTHER IDENTIFIER.

Welcome_Statement='!!!..>>>>><<<<>>>>>..Welcome to Monster Championship..>>>>><<<<>>>>>..!!!'

Selection_Finishing_Statement=" Now lets begin  lets begin the Tournament..!!!"

Intro_Instruction_Statement=f"""TO Begin Your Journey, 
First Chose a Monster You Like:"""

Round_1_Beginning_Statement=f"""
                        //*******ROUND - 1*******\\
Are You Ready..."""

Intro_Status= f"""  
{Fancy_Line1}
|                                                                                                                   |
{Fancy_Divider1}
|       ||       >RED<                   |          >GREEN<                 |         >BLUE<                  ||    |
{Fancy_Divider1}
|       ||  Health = 100                 |     Health = 150                 |    Health =  100                ||    |
|       ||  Attack = 40                  |     Attack = 30                  |    Attack =  25                 ||    |
|       ||  Defence = 25                 |     Defence = 30                 |    Defence =  40                ||    |
|       ||  Elemental_Boost = Attack+10  |     Elemental_Boost = Attack+7   |    Elemental_Boost = Attack+5   ||    |
|       ||                    Defence+5  |                       Defence+7  |                     Defence+10  ||    |
{Fancy_Divider1}
|                                                                                                                   |
{Fancy_Line1}
"""
Individual_Status_RED=f"""
        {Fancy_Individual_Divider1}
        ||           >RED<                ||
        {Fancy_Individual_Divider1}
        ||  Health = 100                  ||
        ||  Attack = 40                   ||
        ||  Defence = 25                  ||
        ||  Elemental_Boost = Attack+10   ||
        ||                    Defence+5   ||
        {Fancy_Individual_Divider1}
"""
Individual_Status_BLUE=f"""
        {Fancy_Individual_Divider1}
        ||           >BLUE<               ||
        {Fancy_Individual_Divider1}
        ||  Health = 100                  ||
        ||  Attack = 25                   ||
        ||  Defence = 40                  ||
        ||  Elemental_Boost = Attack+5    ||
        ||                    Defence+10  ||
        {Fancy_Individual_Divider1}
"""
Individual_Status_GREEN=f"""
        {Fancy_Individual_Divider1}
        ||           >GREEN<              ||
        {Fancy_Individual_Divider1}
        ||  Health = 150                  ||
        ||  Attack = 30                   ||
        ||  Defence = 30                  ||
        ||  Elemental_Boost = Attack+7    ||
        ||                    Defence+7   ||
        {Fancy_Individual_Divider1}
"""

Selected_Monster=""


#/////////////////...............///////////////////...............///////////////////...........//////////////////

#STRUCTURE:
  
print('\n'+Fancy_Line1)
print(Welcome_Statement)
input('->')
print(Intro_Instruction_Statement)
print(Intro_Status)



Selected_Monster=""
#Monster_Name
Monster_RED_Name="'><<<..RED..>>><'"
Monster_GREEN_Name="'><<<.GREEN.>>><'"
Monster_BLUE_Name="'><<<.BLUE..>>><'"
#individual_Stats
    #attack
Monster_RED_Attack=40
Monster_BLUE_Attack=25
Monster_GREEN_Attack=30
Monster_RED_Original_Attack=40
Monster_BLUE_Original_Attack=25
Monster_GREEN_Original_Attack=30
    #Defence
Monster_RED_Defence=25
Monster_BLUE_Defence=40
Monster_GREEN_Defence=30
Monster_RED_Original_Defence=25
Monster_BLUE_Original_Defence=40
Monster_GREEN_Original_Defence=30
    #Health
Monster_RED_Health=100
Monster_BLUE_Health=100
Monster_GREEN_Health=150
Monster_RED_Original_Health=100
Monster_BLUE_Original_Health=100
Monster_GREEN_Original_Health=150
    #Elemental_Boost
Monster_BLUE_Boosted_Attack=5
Monster_BLUE_Boosted_Defence=10
Monster_RED_Boosted_Attack=10
Monster_RED_Boosted_Defence=5
Monster_GREEN_Boosted_Attack=7
Monster_GREEN_Boosted_Defence=7

    #you will find it at line no.....in Elemental boost conditional section.

Zero_Health=0

#/////////////////...............///////////////////...............///////////////////...........//////////////////

#STRUCTURE:



Individual_Image_RED="""
-----------------
|               |
| |||||||||||   |
| ||        ||  |
| ||         || |
| ||         || |
| ||        ||  |
| ||       ||   |
| ||||||||||    |
| ||     ||     |
| ||      ||    |
| ||       ||   |
| ||        ||  |
| ||         || |
|               |
-----------------"""
    
Individual_Image_BLUE="""
---------------------
|                   |
|   ||||||||||      |
|   ||       ||     |
|   ||        ||    |
|   ||        ||    |
|   ||       ||     |
|   ||      ||      |
|   ||||||||||      |
|   ||      ||      |
|   ||       ||     |
|   ||        ||    |
|   ||       ||     |
|   ||||||||||      |
|                   |
---------------------"""

Individual_Image_GREEN="""
------------------
|                |
|     |||||||    |
|    ||     ||   |
|   ||       ||  |
|  ||         || |
| ||          || |
| ||             |
| ||             |
| ||             |
| ||             |
|  ||            |
|   ||     ||||| |
|    ||    || || |
|     ||||||| || |
|                |
------------------"""

Individual_Image_VS='*Vs*'



Monster_RED_Health_Display=""

Player_Monster_Image=''
Player_Monster_Health=""
Player_Monster_Health_Display=""

Player_Monster_Name=""
Opponenet_1_Monster_Name=""
Opponenet_2_Monster_Name=""

#Combat Sentence
Command_Instruction_statement=f"""Enter 'Attack' or 'A' - To attack
Enter 'Shield' or 'S' - To use shield
Enter 'Elemental Boost' or "E" - To use boost
Enter 'Quit' or 'Q' - To Quit the match. """


Player_Monster_Defending_Sentence=f"""{Player_Monster_Name} used Shield."""

Player_Monster_Elemental_Boosting_Sentence=f"""{Player_Monster_Name} used Elemental Boost."""

Opponenet_1_Monster_Attacking_Sentence=f"""{Opponenet_1_Monster_Name} used Attack."""

Opponenet_1_Monster_Defending_Sentence=f"""{Opponenet_1_Monster_Name} used Shield."""

Opponenet_1_Monster_Elemental_Boosting_Sentence=f"""{Opponenet_2_Monster_Name} used Elemental Boost"""

Opponenet_2_Monster_Attacking_Sentence=f"""{Opponenet_2_Monster_Name} used Attack."""

Opponenet_2_Monster_Defending_Sentence=f"""{Opponenet_2_Monster_Name} used Shield."""

Opponenet_2_Monster_Elemental_Boosting_Sentence=f"""{Opponenet_2_Monster_Name} used Elemental Boost"""
Current_Individual_Monster_Status_Index=""
Player_Monster_Status_Index=f"""{Current_Individual_Monster_Status_Index}"""

#Script
Level_2=False
New_Game=False

while New_Game is False:

    Monster_Chosen=False

    while Monster_Chosen is False:

        Selected_Monster=input('Enter the monster name= ')
    
        if Selected_Monster.upper() == 'RED':
            print (" So you have chosen an Attack type monster RED.") 
            print (Individual_Status_RED)
            Choice_confermation=input("BUT,Are you sure...(Y/N) -> ")
            if Choice_confermation.upper()=="Y":
                Monster_Chosen = True
        
        elif Selected_Monster.upper() == 'BLUE':
            print (" So you have chosen a Defence type monster BLUE.")
            print (Individual_Status_BLUE)
            Choice_confermation=input("BUT,Are you sure...(Y/N) -> ")
            if Choice_confermation.upper()=="Y":
                Monster_Chosen = True
     
        elif Selected_Monster.upper() == 'GREEN':
            print (" So you have chosen a Balance type monster GREEN.")
            print (Individual_Status_GREEN)
            Choice_confermation=input("BUT,Are you sure...(Y/N) -> ")
            if Choice_confermation.upper()=="Y":
                Monster_Chosen = True
              
        else:
            print ("I can't understand that....|>.<|, ")
    print(Fancy_Divider1,)
    print(Selection_Finishing_Statement)
    print(Fancy_Line1)
    print(Round_1_Beginning_Statement)
    input("""Press Enter to Begain->""")


    if Selected_Monster.upper() == 'RED':
        Player_Monster_Image=Individual_Image_RED
        Player_Monster_Name=Monster_RED_Name
        Player_Monster_Attack=Monster_RED_Attack
        Player_Monster_Defence=Monster_RED_Defence
        Player_Monster_Health=Monster_RED_Health
        Player_Monster_Original_Health=Monster_RED_Original_Health
        Player_Monster_Original_Attack=Monster_RED_Original_Attack
        Player_Monster_Original_Defence=Monster_RED_Original_Defence
        Player_Monster_Elemental_Boost=f"""Elemental_Boost = Attack+10   ||
            ||                    Defence+5   ||"""
        Player_Monster_Boosted_Attack=Monster_RED_Boosted_Attack
        Player_Monster_Boosted_Defence=Monster_RED_Boosted_Defence
    
        Opponenet_1_Image=Individual_Image_GREEN
        Opponenet_1_Monster_Name=Monster_GREEN_Name
        Opponenet_1_Monster_Attack=Monster_GREEN_Attack
        Opponenet_1_Monster_Defence=Monster_GREEN_Defence
        Opponenet_1_Monster_Health=Monster_GREEN_Health
        Opponenet_1_Monster_Original_Attack=Monster_GREEN_Original_Attack
        Opponenet_1_Monster_Original_Defence=Monster_GREEN_Original_Defence
        Opponenet_1_Monster_Original_Health=Monster_GREEN_Original_Health
    
    
        Opponenet_2_Image=Individual_Image_BLUE
        Opponenet_2_Monster_Name=Monster_BLUE_Name
        Opponenet_2_Monster_Attack=Monster_BLUE_Attack
        Opponenet_2_Monster_Defence=Monster_BLUE_Defence
        Opponenet_2_Monster_Health=Monster_BLUE_Health
        Opponenet_2_Monster_Original_Attack=Monster_BLUE_Original_Attack
        Opponenet_2_Monster_Original_Defence=Monster_BLUE_Original_Defence
        Opponenet_2_Monster_Original_Health=Monster_BLUE_Original_Health

    elif Selected_Monster.upper() == 'GREEN':
        Player_Monster_Image=Individual_Image_GREEN
        Player_Monster_Name=Monster_GREEN_Name
        Player_Monster_Attack=Monster_GREEN_Attack
        Player_Monster_Defence=Monster_GREEN_Defence
        Player_Monster_Health=Monster_GREEN_Health
        Player_Monster_Original_Health=Monster_GREEN_Original_Health
        Player_Monster_Original_Attack=Monster_GREEN_Original_Attack
        Player_Monster_Original_Defence=Monster_GREEN_Original_Defence
        Player_Monster_Elemental_Boost=f"""Elemental_Boost = Attack+7    ||
            ||                    Defence+7   ||"""
        Player_Monster_Boosted_Attack=Monster_GREEN_Boosted_Attack
        Player_Monster_Boosted_Defence=Monster_GREEN_Boosted_Defence
    
        Opponenet_1_Image=Individual_Image_BLUE
        Opponenet_1_Monster_Name=Monster_BLUE_Name
        Opponenet_1_Monster_Attack=Monster_BLUE_Attack
        Opponenet_1_Monster_Defence=Monster_BLUE_Defence
        Opponenet_1_Monster_Health=Monster_BLUE_Health
        Opponenet_1_Monster_Original_Attack=Monster_BLUE_Original_Attack
        Opponenet_1_Monster_Original_Defence=Monster_BLUE_Original_Defence
        Opponenet_1_Monster_Original_Health=Monster_BLUE_Original_Health
    
        Opponenet_2_Image=Individual_Image_RED
        Opponenet_2_Monster_Name=Monster_RED_Name
        Opponenet_2_Monster_Attack=Monster_RED_Attack
        Opponenet_2_Monster_Defence=Monster_RED_Defence
        Opponenet_2_Monster_Health=Monster_RED_Health
        Opponenet_2_Monster_Original_Attack=Monster_RED_Original_Attack
        Opponenet_2_Monster_Original_Defence=Monster_RED_Original_Defence
        Opponenet_2_Monster_Original_Health=Monster_RED_Original_Health
    
    elif Selected_Monster.upper() == 'BLUE':
        Player_Monster_Image=Individual_Image_BLUE
        Player_Monster_Name=Monster_BLUE_Name
        Player_Monster_Attack=Monster_BLUE_Attack
        Player_Monster_Defence=Monster_BLUE_Defence
        Player_Monster_Health=Monster_BLUE_Health
        Player_Monster_Original_Health=Monster_BLUE_Original_Health
        Player_Monster_Original_Attack=Monster_BLUE_Original_Attack
        Player_Monster_Original_Defence=Monster_BLUE_Original_Defence
        Player_Monster_Elemental_Boost=f"""Elemental_Boost = Attack+5    ||
            ||                    Defence+10  ||"""
        Player_Monster_Boosted_Attack=Monster_BLUE_Boosted_Attack
        Player_Monster_Boosted_Defence=Monster_BLUE_Boosted_Defence
    
    
        Opponenet_1_Image=Individual_Image_GREEN
        Opponenet_1_Monster_Name=Monster_GREEN_Name
        Opponenet_1_Monster_Attack=Monster_GREEN_Attack
        Opponenet_1_Monster_Defence=Monster_GREEN_Defence
        Opponenet_1_Monster_Health=Monster_GREEN_Health
        Opponenet_1_Monster_Original_Attack=Monster_GREEN_Original_Attack
        Opponenet_1_Monster_Original_Defence=Monster_GREEN_Original_Defence
        Opponenet_1_Monster_Original_Health=Monster_GREEN_Original_Health
    
    
        Opponenet_2_Image=Individual_Image_RED
        Opponenet_2_Monster_Name=Monster_RED_Name
        Opponenet_2_Monster_Attack=Monster_RED_Attack
        Opponenet_2_Monster_Defence=Monster_RED_Defence
        Opponenet_2_Monster_Health=Monster_RED_Health
        Opponenet_2_Monster_Original_Attack=Monster_RED_Original_Attack
        Opponenet_2_Monster_Original_Defence=Monster_RED_Original_Defence
        Opponenet_2_Monster_Original_Health=Monster_RED_Original_Health
    


    Current_Individual_Monster_Status_Index=f"""
            {Fancy_Individual_Divider1}
            ||      {Player_Monster_Name}         ||
            {Fancy_Individual_Divider1}
            ||  Health ={Player_Monster_Health}                   ||
            ||  Attack ={Player_Monster_Attack}                    ||
            ||  Defence ={Player_Monster_Defence}                   ||
            ||  {Player_Monster_Elemental_Boost}
            {Fancy_Individual_Divider1}
        """




    Combat_Beginning_Sentence=f"""
                                {Player_Monster_Name} {Individual_Image_VS} {Opponenet_1_Monster_Name}
    """
    #combat IDentifier
    Damage_Done_By_Player= (Player_Monster_Attack - round(Opponenet_1_Monster_Defence/10))
    Damage_Done_By_Opponenet_1_Monster= (Opponenet_1_Monster_Attack - round(Player_Monster_Defence/10))




    Opponenet_2_Monster_Health_Display =f"""[{Opponenet_2_Monster_Health}*'|']"""

    Player_Monster_Health_Display = f"""[{Player_Monster_Health}*'|']"""

    Monster_RED_Health_Display = f"""[{Monster_RED_Health}*'|']"""

    Monster_BLUE_Health_Display = f"""[{Monster_BLUE_Health}*'|']"""

    Monster_GREEN_Health_Display = f"""[{Monster_GREEN_Health}*'|']"""

    #Combat Script(Round-1)

    Combat_ON=True
    
    
        
    while Combat_ON is True :
        
        Confermation=""
        print(Combat_Beginning_Sentence)
        print(Current_Individual_Monster_Status_Index)
        input('press Enter->')
        print(f"""{Player_Monster_Image}{Individual_Image_VS}{Opponenet_1_Image}""")
        print(Command_Instruction_statement)

        Player_Monster_Health=Player_Monster_Original_Health
        Player_Monster_Attack=Player_Monster_Original_Attack
        Player_Monster_Defence=Player_Monster_Original_Defence
        Opponenet_1_Monster_Attack=Opponenet_1_Monster_Original_Attack
        Opponenet_1_Monster_Defence=Opponenet_1_Monster_Original_Defence
        Opponenet_1_Monster_Health=Opponenet_1_Monster_Original_Health


    
        Round_1_Retry=False
        while Round_1_Retry is False:
            Player_Turn=True


            Game_Command=input("Enter->")
            

            if Game_Command.upper()=='ATTACK' or Game_Command.upper()=='A' and Player_Turn is True and Player_Monster_Health > Zero_Health:
                Opponenet_1_Monster_Health_Display = round(Opponenet_1_Monster_Health/10)*'|'
                Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'
                print(f"""P:{Player_Monster_Health_Display}                                OP-1:{Opponenet_1_Monster_Health_Display}""")
                Opponenet_1_Monster_Health-=Damage_Done_By_Player

                print(f"""{Player_Monster_Name} used Attack.""")
                print(f'''Dmg-{Damage_Done_By_Player}''')

                print('\n')
                Player_Turn=False
                Opponent_Turn=True

                if Opponenet_1_Monster_Health > Zero_Health and Opponent_Turn is True:
                    import random
                    import math
                    Random_Opponenet_Move_Count=random.random()*100
                    Random_Opponenet_Move_Count=round(Random_Opponenet_Move_Count)

                    if Random_Opponenet_Move_Count >= 0 and Random_Opponenet_Move_Count <= 60:
                        print(f'{Opponenet_1_Monster_Name} used Attack')
                        Player_Monster_Health-=Damage_Done_By_Opponenet_1_Monster
                        Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'

                        print(f'''Dmg-{Damage_Done_By_Opponenet_1_Monster}''')
                    
                    elif Random_Opponenet_Move_Count >= 61 and Random_Opponenet_Move_Count <= 85:
                        print(f'{Opponenet_1_Monster_Name} used Shield')
                        print("Increasing: Defence by 5%.")
                        Opponenet_1_Monster_Defence+= Opponenet_1_Monster_Defence*5
    
                    elif Random_Opponenet_Move_Count >= 85 and Random_Opponenet_Move_Count <= 100:
                        print(f'{Opponenet_1_Monster_Name} used E.Boost')
                        print("Increasing : Defence by 7 and Attack by 7 ")
                        Opponenet_1_Monster_Defence+= 7
                        Opponenet_1_Monster_Attack+= 7
        
                else:
                    print('Your Monster Won')
                    Round_1_Retry_comformation=input("Enter 'R' to retry the round one or 'N' for next level: ")
                    if Round_1_Retry_comformation.upper()=="R":
                        Round_1_Retry= True
                    elif Round_1_Retry_comformation.upper()=="N":
                        Round_1_Retry=True
                        Combat_ON= False
                        New_Game=True
                        Level_2=True 
            
            

            if Game_Command.upper()=="SHIELD" or Game_Command.upper()=="S" and Player_Turn is True and Player_Monster_Health > Zero_Health:
                Opponenet_1_Monster_Health_Display = round(Opponenet_1_Monster_Health/10)*'|'
                Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'
                print(f"""P:{Player_Monster_Health_Display}                                OP-1:{Opponenet_1_Monster_Health_Display}""")

                print(f'{Player_Monster_Name} used Shield')
                print("Increasing: Defence by 5%.")
                Player_Monster_Defence+= Player_Monster_Defence * 5

                print('\n')
                Player_Turn=False
                Opponent_Turn=True

                if Opponenet_1_Monster_Health > Zero_Health and Opponent_Turn is True:
                    import random
                    import math
                    Random_Opponenet_Move_Count=random.random()*100
                    Random_Opponenet_Move_Count=round(Random_Opponenet_Move_Count)

                    if Random_Opponenet_Move_Count >= 0 and Random_Opponenet_Move_Count <= 60:
                        print(f'{Opponenet_1_Monster_Name} used Attack')
                        Player_Monster_Health-=Damage_Done_By_Opponenet_1_Monster
                        Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'
                    
                        print(f'''Dmg-{Damage_Done_By_Opponenet_1_Monster}''')

                    if Random_Opponenet_Move_Count >= 61 and Random_Opponenet_Move_Count <= 85:
                        print(f'{Opponenet_1_Monster_Name} used Shield')
                        print("Increasing: Defence by 5%.")
                        Opponenet_1_Monster_Defence+= Opponenet_1_Monster_Defence * 5

                    if Random_Opponenet_Move_Count >= 85 and Random_Opponenet_Move_Count <= 100:
                        print(f'{Opponenet_1_Monster_Name} used E.Boost')
                        print("Increasing : Defence by 7 and Attack by 7 ")
                        Opponenet_1_Monster_Defence+= 7
                        Opponenet_1_Monster_Attack+= 7
                
                        


                else:
                    print('Your Monster Won')
                    Round_1_Retry_comformation=input("Enter 'R' to retry the round one or 'N' for next level: ")
                    if Round_1_Retry_comformation.upper()=="R":
                        Round_1_Retry= True
                    if Round_1_Retry_comformation.upper()=="N":
                        Round_1_Retry=True
                        Combat_ON= False
                        New_Game=True
                        Level_2=True


            if Game_Command.upper()=="ELEMENTAL_BOOST" or Game_Command.upper()=="E" and Player_Turn is True and Player_Monster_Health > Zero_Health:
                Opponenet_1_Monster_Health_Display = round(Opponenet_1_Monster_Health/10)*'|'
                Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'
                print(f"""P:{Player_Monster_Health_Display}                                OP-1:{Opponenet_1_Monster_Health_Display}""")
            
                print(f'{Player_Monster_Name} used Elemental Boost.')
                print(f"Increasing : Defence by {Player_Monster_Boosted_Defence} and Attack by {Player_Monster_Boosted_Attack} ")
                Player_Monster_Defence+= Player_Monster_Boosted_Defence
                Player_Monster_Attack+= Player_Monster_Boosted_Attack
            
                print('\n')
                Player_Turn=False
                Opponent_Turn=True

                if Opponenet_1_Monster_Health > Zero_Health and Opponent_Turn is True:
                    import random
                    import math
                    Random_Opponenet_Move_Count=random.random()*100
                    Random_Opponenet_Move_Count=round(Random_Opponenet_Move_Count)
                
                    if Random_Opponenet_Move_Count >= 0 and Random_Opponenet_Move_Count <= 60:
                        print(f'{Opponenet_1_Monster_Name} used Attack')
                        Player_Monster_Health-=Damage_Done_By_Opponenet_1_Monster
                        Player_Monster_Health_Display = round(Player_Monster_Health/10)*'|'
                    
                        print(f'''Dmg-{Damage_Done_By_Opponenet_1_Monster}''')
                        Player_Turn = True
                    
                    if Random_Opponenet_Move_Count >= 61 and Random_Opponenet_Move_Count <= 85:
                        print(f'{Opponenet_1_Monster_Name} used Shield')
                        print("Increasing: Defence by 5%.")
                        Opponenet_1_Monster_Defence+= Opponenet_1_Monster_Defence * 5
                        Player_Turn = True

                    if Random_Opponenet_Move_Count >= 85 and Random_Opponenet_Move_Count <= 100:
                        print(f'{Opponenet_1_Monster_Name} used E.Boost')
                        print("Increasing : Defence by 7 and Attack by 7 ")
                        Opponenet_1_Monster_Defence+= 7
                        Opponenet_1_Monster_Attack+= 7
                        Player_Turn = True                
                

                else:
                    print('Your Monster Won')
                    Round_1_Retry_comformation=input("Enter 'R' to retry the round one or 'N' for next level: ")
                    if Round_1_Retry_comformation.upper()=="R":
                        Round_1_Retry= True
                    if Round_1_Retry_comformation.upper()=="N":
                        Round_1_Retry=True
                        Combat_ON= False
                        New_Game=True
                        Level_2=True

            if Game_Command.upper()=="QUIT" or Game_Command.upper()=='Q' and Player_Turn is True and Player_Monster_Health > Zero_Health:
                Confermation= input("Are you sure(Y/N)-> ")
                if Confermation.upper()=="Y":


                    print('Your Monster is Disappointed in You........')
                    input()
                    Round_1_Retry=True
                    Combat_ON=False 
                    New_Game=True
            
            
            if Player_Monster_Health < Zero_Health:                
                print("Your Monster Lost the Match. ")
                Round_1_Retry_comformation=input("Do you want to retry or quit (R/Q)=> ")
                if Round_1_Retry_comformation.upper()=="R":
                    Round_1_Retry=True
                if Round_1_Retry_comformation.upper()=="Q":
                    print('Your Monster is Disappointed in You........')
                    Round_1_Retry=True
                    Combat_ON=False 
                    New_Game=True

            



                


    
        






while Level_2 is True:
    print("Please wait for the next update")
    break



    
input("""Press Enter to End->""")
    
New_Game=False


