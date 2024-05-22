#Importing Python Modules
from tkinter import *
import os

#Connecting To (Single-Player_restart.pyw)
def Start_Game():
    setup.destroy()
    os.startfile("Single-Player_restart.pyw")

#__main__
setup = Tk()
setup.geometry("450x450+525+200")
setup_icon = PhotoImage(file="Icon_Image.png")
setup.iconphoto(False,setup_icon)
setup.title("Tic Tac Toe")
setup_Label = PhotoImage(file="Welcome_Image.png")
label = Label(setup,image=setup_Label)
label.place(x=0,y=0)

#Start Game Button
Play_Button = Button(setup,
                     text="Start Game",
                     fg="white",
                     bg="purple",
                     font=("Arial",15),
                     activeforeground="white",
                     activebackground="purple",
                     command=Start_Game,
                     relief=RAISED)
Play_Button.place(x=170,y=375)

#Displaying Window
setup.mainloop()