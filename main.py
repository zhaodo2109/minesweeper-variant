import settings
from tkinter import *
import utilities
from operators import *


root = Tk()
#  settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Mine and Treasure")
root.resizable(False,False)

# sidebar
side_frame= Frame(
    root,
    bg='beige', #can change later
    width=utilities.width_pec(40),
    height=settings.HEIGHT,
)

# game interface
game_frame = Frame (
    root,
    bg='black',
    width=utilities.width_pec(75),
    height=utilities.height_pec(75),
)

side_frame.place(x=800,y=0)
game_frame.place(x=40,y=38)

# Display grids

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        sq = Square(x,y)
        sq.square_create(game_frame)
        sq.square_create.grid(
            column=x,row=y
        )

# Random generate bombs and treasure
Square.random_bombs()
Square.random_treasure()

for square in Square.all :
    #print(square.is_mine)
    #print(square.is_treasure)
    pass

#run window
root.mainloop()
