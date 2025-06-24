from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        if check_winner():
            label_status.config(text=player + " wins!")
        elif not empty_spaces():
            label_status.config(text="Tie!")
        else:
            player = players[1] if player == players[0] else players[0]
            label_status.config(text=player + " turn")

def check_winner():
   
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label_status.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic Tac Toe")

players = ["x", "o"]
player = random.choice(players)

label_status = Label(text=player + " turn", font=('consolas', 40))
label_status.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame_board = Frame(window)
frame_board.pack()

buttons = [[0 for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame_board, text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()



