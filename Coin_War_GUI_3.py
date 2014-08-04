# Copyright 2014 (c)
# Coin War
# Homework excercise for New Beginnings at PSU 7/27/14 from Bart Massey

import random
from tkinter import *

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

class CoinWar(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, root):
        """ Initialize Frame. """
        super().__init__(root)

        self.grid()

        """ Create widgets to get story information and to display story. """
        # Create instruction label
        Label(self,
              text = "Coin War"
              ).grid(row = 0, column = 1, columnspan = 2, sticky = E + W)

        # Create a button for rules
        Button(self,
               text = "Click for rules",
               command = self.show_rules
               ).grid(row = 1, column = 0, sticky = E + W)

        # Create a button for game play
        Button(self,
               text = "Click to play",
               command = self.play_game
               ).grid(row = 2, column = 0, sticky = E + W)

        # Display program label
        self.game_txt = label(self, justify = LEFT)
        self.game_txt.grid(row = 3, column = 0, columnspan = 4)

    def display_results(self):
        """Prints each players army followed by their prisoners"""
        self.game_txt += ("Player 1's army =", self.join(self.hand1_army))
        self.game_txt += ("Player 1's prisoners =", self.join(self.hand1_prisoners))

        self.game_txt += ("Player 2's army =", self.join(self.hand2_army))
        self.game_txt += ("Player 2's prisoners =", self.join(self.hand2_prisoners))

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
        # Hands (if using hardcoded values, change self.random_hands to False)
        self.hand1_army = []
        self.hand1_prisoners = []
        self.hand2_army = []
        self.hand2_prisoners = []
        self.random_hands = True
        self.game_txt = ""

        if self.random_hands == True:
            """Flips coin 5 times and adds H or T to hand1_army"""
            for i in range(5):
                j = random.randrange(2)
                if j == 1:
                    self.hand1_army += "H"
                elif j == 0:
                    self.hand1_army += "T"
            """Flips coin 5 times and adds H or T to hand2_army"""
            for i in range(5):
                j = random.randrange(2)
                if j == 1:
                    self.hand2_army += "H"
                elif j == 0:
                    self.hand2_army += "T"

        self.game_txt += display_results(self)

        # Main loop
        n = True
        while n == True:

            # Break if either team has an empty army
            if len(self.hand1_army) == 0 or len(self.hand2_army) == 0:
                n == False
                break

            # Hand 1 is winner
            elif self.hand1_army[0] == "H" and self.hand2_army[0] == "T":
                    capture(hand1_army, hand1_prisoners, hand2_army, hand2_prisoners)
                    self.game_txt += "Player 1 wins this hand!\n"
                    self.game_txt += display_results(self)

            # Hand 2 is winner
            elif self.hand1_army[0] == "T" and self.hand2_army[0] == "H":
                    capture(hand2_army, hand2_prisoners, hand1_army, hand1_prisoners)
                    self.game_txt += "Player 2 wins this hand!\n"
                    self.game_txt += display_results(self)

            # It's a tie
            elif self.hand1_army[0] == self.hand2_army[0]:
                    # Put army into prisoners for hand 1
                    self.hand1_prisoners.extend(self.hand1_army[0])
                    self.hand1_army.remove(self.hand1_army[0])
                    # Check for army size
                    if self.hand1_army != []:
                        self.hand1_prisoners.extend(self.hand1_army[0])
                        self.hand1_army.remove(self.hand1_army[0])
                    # Put army into prisoners for hand 2
                    self.hand2_prisoners.extend(self.hand2_army[0])
                    self.hand2_army.remove(self.hand2_army[0])
                    # Check for army size
                    if self.hand2_army != []:
                        self.hand2_prisoners.extend(self.hand2_army[0])
                        self.hand2_army.remove(hand2_army[0])

                    self.game_txt += "It's a tie!\n"
                    self.game_txt += display_results()

        # Find's winner if one player has no army.
        # If neither player has an army, finds who has most amount of heads
        if  self.hand1_army == [] and self.hand2_army == []:
            self.hand1_heads = self.hand1_prisoners.count("H")
            self.hand2_heads = self.hand2_prisoners.count("H")
            if self.hand1_heads > self.hand2_heads:
                self.game_txt += "And the winner is... Player 1!"
            elif self.hand2_heads > self.hand1_heads:
                self.game_txt += "And the winner is... Player 2!"
            elif self.hand2_heads == self.hand1_heads:
                self.game_txt += "It's a tie! What are the chances of that?"

        elif self.hand1_army == []:
            self.game_txt += "And the winner is... Player 2!"

        elif self.hand2_army == []:
            self.game_txt += "And the winner is... Player 1!"

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
app = CoinWar(root)

# Run window's even loop.
root.mainloop()
