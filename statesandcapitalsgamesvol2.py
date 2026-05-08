# Elias Mandeville
# Thursday, 10.2.25
# 

def main():
    # Declare and initialize variables
    # strings for name and menuchoice
    userName = menuChoice = ""
    playAgain = "yes"
    
    # Display Title/Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")
    
    # Prompt for name
    userName = input("First, let me get your name: ")

    # Repeat entire game if user answers yes or no
    # Since we do not know how many times they will want to play again
    # we must use a conditional loop
    while playAgain == "yes":
    
    # Display menu of state options
        print("\nPlease choose from the following menu: ")
        print("A) PA \nB) SC \nC) GA \nD) FL")
        
        
        # Prompt for menuchoice
        menuChoice = input("\nEnter your choice here: ") #"A"
        
        # Selection structure to determine which capital to display to user
        if menuChoice == "A" or menuChoice == "a":
            print("The capital of Pennsylvania is Hassisonburg")
        elif menuChoice =="B" or menuChoice == "b":
            print("The capital of South Carolia is Columbia")
        elif menuChoice == "C" or menuChoice == "c":
            print("The capital of Georgia is Atlanta")
        elif menuChoice == "D" or menuChoice == "d":
            print("The capital of Florida is Tallahassee")
        else:
            print("Sorry, you must choose A,B,C, OR D,")

        # Prompt again
        # This must be inside the loop to give the condition a chance to become false
        playAgain = input("Do you want to play again (yes or no):") #yes

        while playAgain != "yes" and playAgain != "no":
            print("You have to type yes or no")
            playAgain = input("Do you want to play again (yes or no):")
            
        
        
        
    # Display outro
    print(f"\nThank you {userName} for playing my state capitals game!")
    

# Call main function
main()
