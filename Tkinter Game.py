from tkinter import *
from tkinter import messagebox
import random


'''
Session: Lab 1X01
Group Members: Hans, Abizer & Yingwei
Due Date: November 3, 2023
Assignment 2: Graphic Interface Using tkinter
Summary: A simple game, between two players, that gives each player three turns to
claim the most space within a 2d grid of squares.
Resources Used : https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
'''


# Variables
window = Tk()  # Window
window.title("Game")  # Window title
screen = Frame(window)
# Setting screen resolution
btnList = []
totalTurns = 0
pl1Cl, pl1Tn, pl1 = "Green", 0, 0
pl2Cl, pl2Tn, pl2 = "Yellow", 0, 0
player = pl1Cl
row, col = 0, 0




# Adding an option to customize the number of grids




# Abizer
# Create a function for the main menu
# In menu create an option for color,row,column & total turns picker and rules of the game
def instructions():
   screen.pack()
   window.geometry('350x300')
   clear()
   instuct = Label(screen, wraplength=200, pady=50, padx=10,
                   text="A simple game, between two players, that gives each player three turns to claim the most "
                        "space within a 2d grid of squares.")
   instuct.pack()
   back = Button(screen, pady=10, padx=10, text='MENU', command=Menu)
   back.pack()




def clear():
   for widget in screen.winfo_children():
       widget.destroy()




# Primary Contributor: Hans
# Game logic and screen
# Includes creating the button screen, game screen, game mechanics and win game condition
class Game:  # A class for the whole game itself
   def __init__(self):
       self.btn = None
       self.winner = Label(text="")
       window.geometry('750x750')
       self.gameBoard = Frame(window)
       self.value = None
       self.create_board()  # Creates the game board
       self.gameBoard.pack()
       self.whoseTurn = Label(text="It is " + player + "'s turn ", pady=10, padx=10)  # A label for knowing whoes
       # turn it is
       self.playerNumbers = Label(
           text=str(pl1) + " " + pl1Cl + " " + str(pl2) + " " + pl2Cl, pady=10, padx=10)  # How many squared each
       # player has
       self.turnsLeft = Label(
           text="There are " + str(totalTurns - pl1Tn) + " turns left! ", pady=10, padx=10)  # How many turns each
       # player has
       self.backButton = Button(pady=5, padx=10, text='Back', command= self.back)
       self.instructionButton = Button(pady=5, padx=10, text='Instructions', command=lambda a=1: self.instuctions())
       self.backButton.pack(pady=10)
       self.instructionButton.pack(pady=10)
       self.whoseTurn.pack(), self.playerNumbers.pack(), self.turnsLeft.pack()  # Packs all the previous labels


   def instuctions(self):
       messagebox.showinfo(title="Instuctions",
                           message="A simple game, between two players, that gives each player three turns to claim the most space within a 2d grid of squares.")


   def back(self):
       self.backButton.pack_forget(), self.instructionButton.pack_forget()
       self.whoseTurn.pack_forget(), self.playerNumbers.pack_forget(), self.turnsLeft.pack_forget()
       self.gameBoard.pack_forget(), self.winner.pack_forget()
       Menu()


   def create_board(self):  # A function for creating the game board
       global row, col, pl1, pl2, pl2Cl  # Some global vriables needed to create the board
       for x in range(row):  # Loop for the amount of rows
           row_btns = []  # Empty array for the button loction
           for y in range(col):  # Loop for the amount of columns
               rand = 0 if pl1 < pl2 else 1 if pl1 > pl2 else random.randint(0, 1)
               # Creates a random rumber if both player tiles are equal
               if rand == 0:  # If one is greater than the other, then add a tile to the lesser player
                   self.value, pl1 = pl1Cl, pl1 + 1  # value is a temporary variable for the current player color
               else:
                   self.value, pl2 = pl2Cl, pl2 + 1  # Under creates the button
               self.btn = Button(self.gameBoard, text="", width=6, height=3, bg=self.value,
                                 command=lambda a=x, b=y: self.play(a, b))
               self.btn.grid(row=x, column=y)  # Creates a grid for the buttons
               row_btns.append(self.btn)  # Adds the button to the current row
           btnList.append(row_btns)  # Adds the rows together


   def play(self, x, y):  # Function for the game mechanics and main logic
       global pl1Cl, pl1Tn, pl1, pl2Cl, pl2Tn, pl2, player  # Global variables
       btn = btnList[x][y]  # Saves the corrdinates for the clicked button to a variable
       if player != btn.cget('bg'):  # Conditional statement for if the player clicked the correct button
           if player == pl1Cl:  # If the player is pl1
               self.colorChange(x, y)  # Calls function to change the grid
               player, pl1Tn = pl2Cl, pl2Tn + 1  # Switches players and adds 1 to player 1's turn
           else:  # If the player is pl2
               self.colorChange(x, y)
               player, pl2Tn = pl1Cl, pl2Tn + 1
               self.checkWin()  # Checks if the win condition
           self.whoseTurn.config(text="It is " + player + "'s turn ")  # Updates the player turn number
           self.playerNumbers.config(text=str(pl1) + " " + pl1Cl + " " + str(pl2) + " " + pl2Cl)  # Updates score
           if pl2Tn <= totalTurns - 1:  # Conditional for updating the turns left
               self.turnsLeft.config(text="There are " + str(totalTurns - pl2Tn) + " turns left! ")
           else:
               self.turnsLeft.config(text="There are no turns left! ")


   def colorChange(self, x, y):  # Function for the logic of changing the colors
       global player, pl1, pl2, col, row  # GLobal variables
       if btnList[x][y].cget('bg') != player:
           btnList[x][y].config(bg=player)
           if player == pl1Cl:
               pl1, pl2 = pl1 + 1, pl2 - 1
           else:
               pl1, pl2 = pl1 - 1, pl2 + 1
       for k in range(0, y):  # Loop for the column values from the edge of board to y button value, left direction
           if btnList[x][k].cget('bg') == player:  # Checks if there is a player color in this direction
               for j in range(y - 1, -1, -1):  # Loop for the column values from the button to the edge
                   if btnList[x][j].cget('bg') != player:
                       # Checks if the color of the range values is a different color from the player's color
                       btnList[x][j].config(bg=player)  # Changes the button color to the players color
                       if player == pl1Cl:  # If player is pl1
                           pl1, pl2 = pl1 + 1, pl2 - 1  # Changes the values for the tiles of each player
                       else:  # If player is pl2
                           pl1, pl2 = pl1 - 1, pl2 + 1
                   else:  # If the color is the players color
                       break  # Ends loop
       for k in range(col - 1, y, -1):  # Same logic as previous direction, but in the right direction
           if btnList[x][k].cget('bg') == player:
               for j in range(y + 1, col):
                   if btnList[x][j].cget('bg') != player:
                       btnList[x][j].config(bg=player)
                       if player == pl1Cl:
                           pl1, pl2 = pl1 + 1, pl2 - 1
                       else:
                           pl1, pl2 = pl1 - 1, pl2 + 1
                   else:
                       break
       for k in range(0, x - 1):  # Up direction
           if btnList[k][y].cget('bg') == player:
               for i in range(x - 1, -1, -1):
                   if btnList[i][y].cget('bg') != player:
                       btnList[i][y].config(bg=player)
                       if player == pl1Cl:
                           pl1, pl2 = pl1 + 1, pl2 - 1
                       else:
                           pl1, pl2 = pl1 - 1, pl2 + 1
                   else:
                       break
       for k in range(row - 1, x, -1):  # Down direction
           if btnList[k][y].cget('bg') == player:
               for i in range(x + 1, row):
                   if btnList[i][y].cget('bg') != player:
                       btnList[i][y].config(bg=player)
                       if player == pl1Cl:
                           pl1, pl2 = pl1 + 1, pl2 - 1
                       else:
                           pl1, pl2 = pl1 - 1, pl2 + 1
                   else:
                       break


   def checkWin(self):  # Function for the win game condition
       if pl2Tn == totalTurns:  # Checks if the turns of player 2 is equal to the total turns
           if pl1 > pl2:  # Checks if pl1 has more tiles than pl2
               self.winner.config(text="Player 1 Wins")
           elif pl1 < pl2:  # If pl2 has more tiles than pl1
               self.winner.config(text="Player 2 Wins")
           else:  # If neither pl1 nor pl2 has more tiles than the other
               self.winner.config(text="It's a Tie, No One Wins")
           self.winner.pack()  # Packs the label for the winner text
           self.instructionButton.pack_forget(), self.whoseTurn.pack_forget(), self.turnsLeft.pack_forget()




class Menu:
   def __init__(self):
       screen.pack()
       window.geometry('350x300')
       clear()
       self.totalTurnsLabel = Label(screen, pady=10, padx=10, text='Turns')
       self.totalTurnsEntry = Entry(screen)


       self.rowLabel = Label(screen, pady=10, padx=10, text='Rows')
       self.rowEntry = Entry(screen)
       # Labeling the columns


       self.colLabel = Label(screen, pady=10, padx=10, text='Columns')
       self.colEntry = Entry(screen)
       self.instructionButton = Button(screen, pady=10, padx=10, text='Instructions', command=instructions)


       self.start = Button(screen, text="START GAME", pady=10, padx=10, command=self.startGame)
       self.totalTurnsLabel.pack(), self.totalTurnsEntry.pack(), self.rowLabel.pack(), self.rowEntry.pack(), self.colLabel.pack(), self.colEntry.pack(), self.instructionButton.pack(
           pady=10), self.start.pack()


   def startGame(self):
       global row, col, totalTurns
       if 2 < int(self.totalTurnsEntry.get()) <= 10 and 1 < int(
               self.rowEntry.get()) <= 12 and 1 < int(self.colEntry.get()) <= 12:
           totalTurns = int(self.totalTurnsEntry.get())
           row = int(self.rowEntry.get())
           col = int(self.colEntry.get())
           screen.pack_forget()
           Game()  # Calls the game




Menu()


window.mainloop()  # Loops the window                                                                                                                        