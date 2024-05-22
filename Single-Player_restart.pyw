#Importing Python Modules
from tkinter import *
import random
from tkinter import messagebox
import os

#__main__
window = Tk()
window.title("TIC TAC TOE")
window.geometry("450x450+525+200")
window.resizable(height=False,width=False)
Icon_Image = PhotoImage(file="Icon_Image.png")
window.iconphoto(False,Icon_Image)

list_button=[]
dict = {"button1":0,"button2":0,"button3":0,
        "button4":0,"button5":0,"button6":0,
        "button7":0,"button8":0,"button9":0}

com = True
tie = True

#Messagebox To Play Again
def restart(root):
    restart = messagebox.askyesno("Match Has Been Over",
                                  "Do You Want To Play Again")
    if restart:
        root.destroy()
        os.startfile("Single-Player_restart.pyw")
    else:
        root.destroy()
        root = Tk()
        root.geometry("450x450+525+200")
        root.resizable(height=False, width=False)
        root.title("Time To Say Good Bye")
        icon = PhotoImage(file="Bye_Image.png")
        root.iconphoto(False, icon)
        Thankyouimage_list = ["ThankYou_Image1.png",
                              "ThankYou_Image2.png",
                              "ThankYou_Image3.png",
                              "ThankYou_Image4.png",
                              "ThankYou_Image5.png"]

        ThankYou_Image = PhotoImage(file=random.choice(Thankyouimage_list))
        Label_ThankYou = Label(root, image=ThankYou_Image)
        Label_ThankYou.pack()
        root.after(5000, root.destroy)
        root.mainloop()

#Win Image - Window
def PlayerWin():
    window.destroy()
    root = Tk()
    root.geometry("450x450+525+200")
    root.resizable(height=False,width=False)
    root.title("Result!!!")
    icon = PhotoImage(file="trophy.png")
    root.iconphoto(False,icon)
    Win_Image = PhotoImage(file="Win_Image.png")
    Label_Win = Label(root,image=Win_Image)
    Label_Win.pack()
    root.after(1000,lambda x=root: restart(x))
    root.mainloop()

#Lose Image - Window
def PlayerLose():
    window.destroy()
    root = Tk()
    root.geometry("450x450+525+200")
    root.resizable(height=False, width=False)
    root.title("Result!!!")
    icon = PhotoImage(file="trophy.png")
    root.iconphoto(False, icon)
    Lose_Image = PhotoImage(file="Lose_Image.png")
    Label_Lose= Label(root, image=Lose_Image)
    Label_Lose.pack()
    root.after(1000,lambda x=root:restart(x))
    root.mainloop()

#Messagebox Display When Game Tied
def Game_Tie():
    global tie
    if tie:
        restart =messagebox.askyesno("Match Has Been Tied",
                                     "Do You Want To Play Again")
        if restart:
            window.destroy()
            os.startfile("Single-Player_restart.pyw")
        else:
            window.destroy()
            root = Tk()
            root.geometry("450x450+525+200")
            root.resizable(height=False, width=False)
            root.title("Time To Say Good Bye")
            icon = PhotoImage(file="Bye_Image.png")
            root.iconphoto(False, icon)
            Thankyouimage_list=["ThankYou_Image1.png",
                                "ThankYou_Image2.png",
                                "ThankYou_Image3.png",
                                "ThankYou_Image4.png",
                                "ThankYou_Image5.png"]

            ThankYou_Image = PhotoImage(file=random.choice(Thankyouimage_list))
            Label_ThankYou= Label(root, image=ThankYou_Image)
            Label_ThankYou.pack()
            root.after(5000,root.destroy)
            root.mainloop()
        tie=False

#Check For Win Or Lose Or Tie Condition
def result():
    global dict
    global com
    l1 = []
    l2 = []
    l3 = []
    #Checking Buttons Text
    if dict["button1"] == "X":
        l1.append(1)
    elif dict["button1"] == 0:
        l2.append(1)
    else:
        l3.append(1)
    if dict["button2"] == "X":
        l1.append(2)
    elif dict["button2"] == 0:
        l2.append(2)
    else:
        l3.append(2)
    if dict["button3"] == "X":
        l1.append(3)
    elif dict["button3"] == 0:
        l2.append(3)
    else:
        l3.append(3)
    if dict["button4"] == "X":
        l1.append(4)
    elif dict["button4"] == 0:
        l2.append(4)
    else:
        l3.append(4)
    if dict["button5"] == "X":
        l1.append(5)
    elif dict["button5"] == 0:
        l2.append(5)
    else:
        l3.append(5)
    if dict["button6"] == "X":
        l1.append(6)
    elif dict["button6"] == 0:
        l2.append(6)
    else:
        l3.append(6)
    if dict["button7"] == "X":
        l1.append(7)
    elif dict["button7"] == 0:
        l2.append(7)
    else:
        l3.append(7)
    if dict["button8"] == "X":
        l1.append(8)
    elif dict["button8"] == 0:
        l2.append(8)
    else:
        l3.append(8)
    if dict["button9"] == "X":
        l1.append(9)
    elif dict["button9"] == 0:
        l2.append(9)
    else:
        l3.append(9)

    if 1 in l1 and 2 in l1 and 3 in l1:
        button1["bg"] = "powder blue"
        button2["bg"] = "powder blue"
        button3["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button2["fg"] = "#00ff00"
        button3["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 1 in l3 and 2 in l3 and 3 in l3:
        button1["bg"] = "powder blue"
        button2["bg"] = "powder blue"
        button3["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button2["fg"] = "#00ff00"
        button3["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 4 in l1 and 5 in l1 and 6 in l1:
        button4["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button6["bg"] = "powder blue"
        button4["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button6["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 4 in l3 and 5 in l3 and 6 in l3:
        button4["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button6["bg"] = "powder blue"
        button4["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button6["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 7 in l1 and 8 in l1 and 9 in l1:
        button7["bg"] = "powder blue"
        button8["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button7["fg"] = "#00ff00"
        button8["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)


    elif 7 in l3 and 8 in l3 and 9 in l3:
        button7["bg"] = "powder blue"
        button8["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button7["fg"] = "#00ff00"
        button8["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)


    elif 1 in l1 and 4 in l1 and 7 in l1:
        button1["bg"] = "powder blue"
        button4["bg"] = "powder blue"
        button7["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button4["fg"] = "#00ff00"
        button7["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 1 in l3 and 4 in l3 and 7 in l3:
        button1["bg"] = "powder blue"
        button4["bg"] = "powder blue"
        button7["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button4["fg"] = "#00ff00"
        button7["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 2 in l1 and 5 in l1 and 8 in l1:
        button2["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button8["bg"] = "powder blue"
        button2["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button8["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 2 in l3 and 5 in l3 and 8 in l3:
        button2["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button8["bg"] = "powder blue"
        button2["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button8["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 3 in l1 and 6 in l1 and 9 in l1:
        button3["bg"] = "powder blue"
        button6["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button3["fg"] = "#00ff00"
        button6["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 3 in l3 and 6 in l3 and 9 in l3:
        button3["bg"] = "powder blue"
        button6["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button3["fg"] = "#00ff00"
        button6["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 1 in l1 and 5 in l1 and 9 in l1:
        button1["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 1 in l3 and 5 in l3 and 9 in l3:
        button1["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button9["bg"] = "powder blue"
        button1["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button9["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    elif 3 in l1 and 5 in l1 and 7 in l1:
        button3["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button7["bg"] = "powder blue"
        button3["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button7["fg"] = "#00ff00"

        #Disabling Buttons When Player Win
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        com=False
        window.after(ms=3000,func=PlayerWin)

    elif 3 in l3 and 5 in l3 and 7 in l3:
        button3["bg"] = "powder blue"
        button5["bg"] = "powder blue"
        button7["bg"] = "powder blue"
        button3["fg"] = "#00ff00"
        button5["fg"] = "#00ff00"
        button7["fg"] = "#00ff00"

        #Disabling Buttons When Player Lose
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        window.after(3000,PlayerLose)

    else:
        l_values=list(dict.values())
        if 0 not in l_values:
            Game_Tie()

#Player 2(Computer) Move
def computer_play():
    if com:
        global dict
        l1=[]
        l2=[]
        l3=[]
        if dict["button1"] == "X":
            l1.append(1)
        elif dict["button1"] == 0:
            l2.append(1)
        else:
            l3.append(1)
        if dict["button2"] == "X":
            l1.append(2)
        elif dict["button2"] == 0:
            l2.append(2)
        else:
            l3.append(2)
        if dict["button3"] == "X":
            l1.append(3)
        elif dict["button3"] == 0:
            l2.append(3)
        else:
            l3.append(3)
        if dict["button4"] == "X":
            l1.append(4)
        elif dict["button4"] == 0:
            l2.append(4)
        else:
            l3.append(4)
        if dict["button5"] == "X":
            l1.append(5)
        elif dict["button5"] == 0:
            l2.append(5)
        else:
            l3.append(5)
        if dict["button6"] == "X":
            l1.append(6)
        elif dict["button6"] == 0:
            l2.append(6)
        else:
            l3.append(6)
        if dict["button7"] == "X":
            l1.append(7)
        elif dict["button7"] == 0:
            l2.append(7)
        else:
            l3.append(7)
        if dict["button8"] == "X":
            l1.append(8)
        elif dict["button8"] == 0:
            l2.append(8)
        else:
            l3.append(8)
        if dict["button9"] == "X":
            l1.append(9)
        elif dict["button9"] == 0:
            l2.append(9)
        else:
            l3.append(9)

        #Affending Conditions For Player 2(Computer) Move
        if (1 in l3 and 2 in l3 and (dict["button3"] == 0)):
            button3["text"] = "O"
            dict["button3"] = "O"
        elif (1 in l3 and 3 in l3 and (dict["button2"] == 0)):
            button2["text"] = "O"
            dict["button2"] = "O"
        elif (2 in l3 and 3 in l3 and (dict["button1"] == 0)):
            button1["text"] = "O"
            dict["button1"] = "O"
        elif (4 in l3 and 5 in l3 and (dict["button6"] == 0)):
            button6["text"] = "O"
            dict["button6"] = "O"
        elif (4 in l3 and 6 in l3 and (dict["button5"] == 0)):
            button5["text"] = "O"
            dict["button5"] = "O"
        elif (5 in l3 and 6 in l3 and (dict["button4"] == 0)):
            button4["text"] = "O"
            dict["button4"] = "O"
        elif (7 in l3 and 8 in l3 and (dict["button9"] == 0)):
            button9["text"] = "O"
            dict["button9"] = "O"
        elif (7 in l3 and 9 in l3 and (dict["button8"] == 0)):
            button8["text"] = "O"
            dict["button8"] = "O"
        elif (8 in l3 and 9 in l3 and (dict["button7"] == 0)):
            button7["text"] = "O"
            dict["button7"] = "O"
        elif (1 in l3 and 4 in l3 and (dict["button7"] == 0)):
            button7["text"] = "O"
            dict["button7"] = "O"
        elif (1 in l3 and 7 in l3 and (dict["button4"] == 0)):
            button4["text"] = "O"
            dict["button4"] = "O"
        elif (4 in l3 and 7 in l3 and (dict["button1"] == 0)):
            button1["text"] = "O"
            dict["button1"] = "O"
        elif (2 in l3 and 5 in l3 and (dict["button8"] == 0)):
            button8["text"] = "O"
            dict["button8"] = "O"
        elif (2 in l3 and 8 in l3 and (dict["button5"] == 0)):
            button5["text"] = "O"
            dict["button5"] = "O"
        elif (5 in l3 and 8 in l3 and (dict["button2"] == 0)):
            button2["text"] = "O"
            dict["button2"] = "O"
        elif (3 in l3 and 6 in l3 and (dict["button9"] == 0)):
            button9["text"] = "O"
            dict["button9"] = "O"
        elif (3 in l3 and 9 in l3 and (dict["button6"] == 0)):
            button6["text"] = "O"
            dict["button6"] = "O"
        elif (6 in l3 and 9 in l3 and (dict["button3"] == 0)):
            button3["text"] = "O"
            dict["button3"] = "O"
        elif (1 in l3 and 5 in l3 and (dict["button9"] == 0)):
            button9["text"] = "O"
            dict["button9"] = "O"
        elif (1 in l3 and 9 in l3 and (dict["button5"] == 0)):
            button5["text"] = "O"
            dict["button5"] = "O"
        elif (5 in l3 and 9 in l3 and (dict["button1"] == 0)):
            button1["text"] = "O"
            dict["button1"] = "O"
        elif (3 in l3 and 5 in l3 and (dict["button7"] == 0)):
            button7["text"] = "O"
            dict["button7"] = "O"
        elif (3 in l3 and 7 in l3 and (dict["button5"] == 0)):
            button5["text"] = "O"
            dict["button5"] = "O"
        elif (5 in l3 and 7 in l3 and (dict["button3"] == 0)):
            button3["text"] = "O"
            dict["button3"] = "O"
        else:
            #Defending Conditions For Player 2(Computer) Move
            if (1 in l1 and 2 in l1 and (dict["button3"] == 0)):
                button3["text"] = "O"
                dict["button3"] = "O"
            elif (1 in l1 and 3 in l1 and (dict["button2"] == 0)):
                button2["text"] = "O"
                dict["button2"] = "O"
            elif (2 in l1 and 3 in l1 and (dict["button1"] == 0)):
                button1["text"] = "O"
                dict["button1"] = "O"
            elif (4 in l1 and 5 in l1 and (dict["button6"] == 0)):
                button6["text"] = "O"
                dict["button6"] = "O"
            elif (4 in l1 and 6 in l1 and (dict["button5"] == 0)):
                button5["text"] = "O"
                dict["button5"] = "O"
            elif (5 in l1 and 6 in l1 and (dict["button4"] == 0)):
                button4["text"] = "O"
                dict["button4"] = "O"
            elif (7 in l1 and 8 in l1 and (dict["button9"] == 0)):
                button9["text"] = "O"
                dict["button9"] = "O"
            elif (7 in l1 and 9 in l1 and (dict["button8"] == 0)):
                button8["text"] = "O"
                dict["button8"] = "O"
            elif (8 in l1 and 9 in l1 and (dict["button7"] == 0)):
                button7["text"] = "O"
                dict["button7"] = "O"
            elif (1 in l1 and 4 in l1 and (dict["button7"] == 0)):
                button7["text"] = "O"
                dict["button7"] = "O"
            elif (1 in l1 and 7 in l1 and (dict["button4"] == 0)):
                button4["text"] = "O"
                dict["button4"] = "O"
            elif (4 in l1 and 7 in l1 and (dict["button1"] == 0)):
                button1["text"] = "O"
                dict["button1"] = "O"
            elif (2 in l1 and 5 in l1 and (dict["button8"] == 0)):
                button8["text"] = "O"
                dict["button8"] = "O"
            elif (2 in l1 and 8 in l1 and (dict["button5"] == 0)):
                button5["text"] = "O"
                dict["button5"] = "O"
            elif (5 in l1 and 8 in l1 and (dict["button2"] == 0)):
                button2["text"] = "O"
                dict["button2"] = "O"
            elif (3 in l1 and 6 in l1 and (dict["button9"] == 0)):
                button9["text"] = "O"
                dict["button9"] = "O"
            elif (3 in l1 and 9 in l1 and (dict["button6"] == 0)):
                button6["text"] = "O"
                dict["button6"] = "O"
            elif (6 in l1 and 9 in l1 and (dict["button3"] == 0)):
                button3["text"] = "O"
                dict["button3"] = "O"
            elif (1 in l1 and 5 in l1 and (dict["button9"] == 0)):
                button9["text"] = "O"
                dict["button9"] = "O"
            elif (1 in l1 and 9 in l1 and (dict["button5"] == 0)):
                button5["text"] = "O"
                dict["button5"] = "O"
            elif (5 in l1 and 9 in l1 and (dict["button1"] == 0)):
                button1["text"] = "O"
                dict["button1"] = "O"
            elif (3 in l1 and 5 in l1 and (dict["button7"] == 0)):
                button7["text"] = "O"
                dict["button7"] = "O"
            elif (3 in l1 and 7 in l1 and (dict["button5"] == 0)):
                button5["text"] = "O"
                dict["button5"] = "O"
            elif (5 in l1 and 7 in l1 and (dict["button3"] == 0)):
                button3["text"] = "O"
                dict["button3"] = "O"

            else:
                #Random Move By Player 2(Computer)
                if l2 != []:
                    rand_choice = random.choice(l2)
                    if rand_choice == 1:
                        button1["text"] = "O"
                        dict["button1"] = "O"
                    elif rand_choice == 2:
                        button2["text"] = "O"
                        dict["button2"] = "O"
                    elif rand_choice == 3:
                        button3["text"] = "O"
                        dict["button3"] = "O"
                    elif rand_choice == 4:
                        button4["text"] = "O"
                        dict["button4"] = "O"
                    elif rand_choice == 5:
                        button5["text"] = "O"
                        dict["button5"] = "O"
                    elif rand_choice == 6:
                        button6["text"] = "O"
                        dict["button6"] = "O"
                    elif rand_choice == 7:
                        button7["text"] = "O"
                        dict["button7"] = "O"
                    elif rand_choice == 8:
                        button8["text"] = "O"
                        dict["button8"] = "O"
                    elif rand_choice == 9:
                        button9["text"] = "O"
                        dict["button9"] = "O"
        result()

#Finding Which Button Clicked
def click_place(click_placer):
    global dict
    xclick_cor=click_placer.winfo_x()
    yclick_cor = click_placer.winfo_y()
    if yclick_cor==0:
        if xclick_cor==0:
            dict["button1"] ="X"
        elif xclick_cor==150:
            dict["button2"] = "X"
        else:
            dict["button3"] = "X"
    elif yclick_cor==150:
        if xclick_cor == 0:
            dict["button4"] = "X"
        elif xclick_cor == 150:
            dict["button5"] = "X"
        else:
            dict["button6"] = "X"
    else:
        if xclick_cor == 0:
            dict["button7"] = "X"
        elif xclick_cor == 150:
            dict["button8"] = "X"
        else:
            dict["button9"] = "X"


#Inserting X To Clicked Button(Player 1)
def play(click_button):
    global dict
    if click_button["text"] == " ":
        click_button["text"] = "X"
        click_place(click_placer=click_button)
        result()
        computer_play()
    else:
        #Messagebox When Button Pressed Twice
        messagebox.showinfo("Already Clicked",
                            "Button Already Clicked")

#__main__
k=0
x_cor=0
y_cor=0
for i in range(3):
    for j in range(3):
        #Creating Buttons
        list_button.append(Button(window,
                                  text=" ",
                                  relief=SUNKEN,
                                  font=("Arial",100),
                                  bg="black",
                                  fg="white",
                                  activebackground="black",
                                  activeforeground="white"))

        list_button[k]["command"] = lambda x=list_button[k]: play(x)
        list_button[k].place(x=x_cor, y=y_cor, height=150, width=150)
        k+=1
        x_cor+=150
    y_cor+=150
    x_cor=0

#Renaming Button From Default Names
button1 = list_button[0]
button2 = list_button[1]
button3 = list_button[2]
button4 = list_button[3]
button5 = list_button[4]
button6 = list_button[5]
button7 = list_button[6]
button8 = list_button[7]
button9 = list_button[8]

#Displaying Window
window.mainloop()