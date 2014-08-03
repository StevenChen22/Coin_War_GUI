# Copyright 2014 (c)
# Coin War
# Homework excercise for New Beginnings at PSU 7/27/14 from Bart Massey

import random
from tkinter import *

# Hands (if using hardcoded values, change random_hands to False)
hand1_army = []
hand1_prisoners = []
hand2_army = []
hand2_prisoners = []
random_hands = True

def flip(hand_army):
    """Flips coin 5 times and adds H or T to hand"""
    for i in range(5):
        j = random.randrange(2)
        if j == 1:
            hand_army += "H"
        elif j == 0:
            hand_army += "T"

def capture(winner_army, winner_prisoners, loser_army, loser_prisoners):
    """Distributes coins between players armies and prisoners after a capture"""
    winner_army.extend(loser_army[0])
    loser_army.remove(loser_army[0])

    winner_army.extend(winner_army[0])
    winner_army.remove(winner_army[0])

    winner_army.extend(loser_prisoners)
    del loser_prisoners[:]

    winner_army.extend(winner_prisoners)
    del winner_prisoners[:]

def display_results():
    """Prints each players army followed by their prisoners"""
    print ("Player 1's army consists of:", ', '.join(hand1_army))
    print("Player 1's prisoners consist of:", ', '.join(hand1_prisoners))

    print("Player 2's army consists of:", ', '.join(hand2_army))
    print("Player 2's prisoners consist of:", ', '.join(hand2_prisoners))

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # Create instruction label
        Label(self,
              text = "Coin War"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # Create a button for rules
        Button(self,
               text = "Click for rules",
               command = self.show_rules
               ).grid(row = 1, column = 0, sticky = W)

        # Create a button for game play
        Button(self,
               text = "Click to play",
               command = self.play_game
               ).grid(row = 2, column = 0, sticky = W)

        # Display program area
        self.game_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.game_txt.grid(row = 7, column = 0, columnspan = 4)

    def show_rules(self):
        """ Fill text box with the rules."""
        rules = """
Coin War:
Each player has an "army" of five randomly flipped coins:
heads (H) or tails (T).

The players compare the first coins in their armies. Heads beats Tails.

The player with H captures the coin of the player with T
and puts both player's coins at the end of their Army in that order.

In addition, the player with H then captures the Prisoners of the player
with T and places the opposing Prisoners at the end of their own Prisoners.

If the coins are the same:
Each player puts the matched coin at the end of their Prisoners.
Players with coins still in their Army then put the first remaining coin
in their Army at the end of their sequence of Prisoners.

Victory conditions:
At any point, if either player has no Army, the game is immediately over.

If only one player has an Army, that player wins.

Otherwise, both players must have no Army.

If one player has more H coins than the other in their Prisoners,
that player wins.

Otherwise, the game is a tie.
"""

    # display the rules
    self.game_txt.delete(0.0, END)
    self.game_txt.insert(0.0, rules)

    def play_game(self):
        """Play the game!"""
        text = ""
        # Flip and fill hands
        if random_hands == True:
            flip(hand1_army)
            flip(hand2_army)

        text += display_results()
        # Main loop
        n = True
        while n == True:

            # Break if either team has an empty army
            if len(hand1_army) == 0 or len(hand2_army) == 0:
                n == False
                break

            # Hand 1 is winner
            elif hand1_army[0] == "H" and hand2_army[0] == "T":
                capture(hand1_army, hand1_prisoners, hand2_army, hand2_prisoners)
                text += "Player 1 wins this hand!\n"
                text += display_results()

            # Hand 2 is winner
            elif hand1_army[0] == "T" and hand2_army[0] == "H":
                capture(hand2_army, hand2_prisoners, hand1_army, hand1_prisoners)
                text += "Player 2 wins this hand!\n"
                text += display_results()

            # It's a tie
            elif hand1_army[0] == hand2_army[0]:
                # Put army into prisoners for hand 1
                hand1_prisoners.extend(hand1_army[0])
                hand1_army.remove(hand1_army[0])
                # Check for army size
                if hand1_army != []:
                    hand1_prisoners.extend(hand1_army[0])
                    hand1_army.remove(hand1_army[0])
                # Put army into prisoners for hand 2
                hand2_prisoners.extend(hand2_army[0])
                hand2_army.remove(hand2_army[0])
                # Check for army size
                if hand2_army != []:
                    hand2_prisoners.extend(hand2_army[0])
                    hand2_army.remove(hand2_army[0])

                text += "It's a tie!\n"
                text += display_results()

        # Find's winner if one player has no army.
        # If neither player has an army, finds who has most amount of heads
        if  hand1_army == [] and hand2_army == []:
            hand1_heads = hand1_prisoners.count("H")
            hand2_heads = hand2_prisoners.count("H")
            if hand1_heads > hand2_heads:
                text += "And the winner is... Player 1!"
            elif hand2_heads > hand1_heads:
                text += "And the winner is... Player 2!"
            elif hand2_heads == hand1_heads:
                text += "It's a tie! What are the chances of that?"

        elif hand1_army == []:
            text += "And the winner is... Player 2!"

        elif hand2_army == []:
            text += "And the winner is... Player 1!"

        # display the game
        self.game_txt.delete(0.0, END)
        self.game_txt.insert(0.0, text)

# Create root window.
root = Tk()

# Modify the window.
root.title("Coin War")
root.geometry("500x800")

# Create a frame in the window to hold other widgets and invoke the grid method.
app = Frame(root).grid()

# Instantiate object with the root window as its master.
app = Application(root)

# Run window's even loop.
root.mainloop()
