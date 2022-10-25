import random as rd

def rock_paper_sciccors(s):
    play_list = ['rock', 'paper', 'scissors']

    if s in play_list:
        print("Your choice is", s)
        comp_choice = rd.choice(play_list)
        print("The computer chose: ", comp_choice)

        if ((s == 'rock')and (comp_choice == 'scissors')) or ((s == 'paper') and (comp_choice == 'rock')) or ((s == 'scissors') and (comp_choice == 'paper')):
            return print("You won!!")
        elif (s == comp_choice):
            return print("That is a draw. Lets go play again.")
        else:
            return print("You lose!!")

    else:
        print("Invalid choice")

for i in range(3):
    rock_paper_sciccors(input("Enter your choice: "))
    print("***************************************************************")