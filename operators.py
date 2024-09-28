from tkinter import Button, Label
from colorama import Fore, Style
import ctypes
import sys

import random


# Class for creating the button/ squares / coordinates
class Square:

    all = []

    def __init__(self,x ,y, is_mine = False, is_treasure=False):

        self.is_mine = is_mine
        self.is_treasure = is_treasure
        self.square_button = None
        self.x = x
        self.y = y
        self.opened = False

        #Append the object to the Square.all list
        Square.all.append(self)

    #Making the grids
    def square_create(self,location):
        btn = Button(
            location,
            width=5,
            height=2,
            #text=f"{self.x} , {self.y}"
        )
        btn.bind('<Button-3>', self.right_mouse_clicked ) # right clicked
        btn.bind('<Button-1>', self.left_mouse_clicked ) # left clicked
        self.square_create = btn

    #Display player
    '''@staticmethod
    def player_data(location):
        stats = Label(
            location,
            bg='dark grey',
            fg='white',
            text=f"Welcome to Mine and Treasure",
            font=30,
            width=20,
            height=5,
        )
        Square.player_stats = stats

    @staticmethod
    def point_add(location):
        stats2 = Label(
            location,
            bg='dark grey',
            fg='white',
            text=f"Treasure : {Square.point_count} ",
            font=30,
            width=20,
            height=5,
        )
        Square.point_add = stats2'''


    # When player click on the square with left click
    def left_mouse_clicked(self, event ):
        count=0
        if self.is_mine:
            self.display_bomb()
        elif self.is_treasure:
            self.display_treasure()
        else:
            for empty_squares in self.surrounding_squares:
                if self.nums_bombs_around == 0 and empty_squares.is_treasure is False and empty_squares.nums_treasure_around != 1:
                    empty_squares.show_surrounded()
            self.show_surrounded()



    # Get coordination of clicked square
    def get_numsxy(self,x,y):
        for square in Square.all:
            if square.x == x and square.y == y:
                return square

    # Display the bomb if pressed on
    def display_bomb(self):
        self.square_create.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine, Game Over', 2)
        sys.exit()

    # Display the treasure if pressed on
    def display_treasure(self):
        self.square_create.configure(bg='yellow')
        self.opened = True

    #Check if there's any bomb around chosen squares
    @property
    def surrounding_squares(self):
        squares = [
            self.get_numsxy(self.x - 1, self.y - 1),
            self.get_numsxy(self.x - 1, self.y - 0),
            self.get_numsxy(self.x, self.y - 1),
            self.get_numsxy(self.x, self.y + 1),
            self.get_numsxy(self.x + 1, self.y),
            self.get_numsxy(self.x - 1, self.y + 1),
            self.get_numsxy(self.x + 1, self.y - 1),
            self.get_numsxy(self.x + 1, self.y + 1),
        ]

        squares = [square for square in squares if square is not None]
        return squares


    # count how many bombs around the chosen square
    @property
    def nums_bombs_around(self):
        counter_a = 0
        for square in self.surrounding_squares:
            if square.is_mine:
                counter_a += 1
        return counter_a

    # how many treasure around
    @property
    def nums_treasure_around(self):
        counter_b=0
        for square in self.surrounding_squares:
            if square.is_treasure:
                counter_b+=1
        return counter_b

    # Display numbers of bombs then / numbers of treasure around
    def show_surrounded(self):
        self.square_create.configure(text=f" {self.nums_bombs_around} / {self.nums_treasure_around}",fg='blue')
        self.opened = True


    # When user click right mouse
    def right_mouse_clicked(self,event):
        print(event)
        print("Clicked right")

    #Random generate bombs in side board created
    @staticmethod
    def random_bombs():
        bombs_placed = random.sample(
            Square.all,35
        )
        print(bombs_placed)
        for bombs_placed in bombs_placed :
            bombs_placed.is_mine = True

    # Random generate treasure
    @staticmethod
    def random_treasure():
        treasure_placed = random.sample(
            Square.all,5
        )
        print(treasure_placed)
        for treasure_placed in treasure_placed :
            treasure_placed.is_treasure = True

    # Check win
    '''def check_win(self):
        battery = True
        start = True
        while battery is True:
            while start is True:
                if not Square.opened:
                    if Square.count % 2 == 0 and self.left_mouse_clicked:
                        Square.count += 1
                        p_turn_1 = False
                        if p_turn_1 is True and self.display_bomb():
                            Square.lives_count1 -= 1
                    if Square.count % 2 != 0 and self.left_mouse_clicked:
                        Square.count += 1
                        p_turn_1 = True
                        if p_turn_1 is False and self.display_bomb():
                            Square.lives_count2 -= 1
                        if Square.count % 2 == 0 and self.left_mouse_clicked:
                            Square.count += 1
                            p_turn_1 = False
                            if p_turn_1 is True:
                                Square.point1_count += 1
                        if Square.count % 2 != 0 and Square.left_mouse_clicked:
                            Square.count += 1
                            p_turn_1 = True
                            if p_turn_1 is False:
                                Square.point2_count += 1
                if Square.point1_count == 5:
                    print("Game Over, Player 1 win")
                elif Square.point2_count == 5:
                    print("Game Over, Player 2 win")
                elif Square.lives_count1 == 0:
                    print("Game Over, Player 2 win")
                elif Square.lives_count2 == 0:
                    print("Game Over, Player 1 win")'''

    #Convert into coordinate of strings
    def __repr__(self):
        return f"Square({self.x},{self.y})"








