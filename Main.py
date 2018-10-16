import tkinter
from Fighter import Fighter
from Ball import Ball

def key(event):
    ping.move(event.char)
    pong.move(event.char)

def loop():
    if ball.move(ping, pong):
        root.after(12, loop)
    else:
        print("Game Over!")

width = 300
height = 300

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=width, height=height)
root.bind("<Key>", key)


ping = Fighter(10, 10, height, "w", "s", canvas)
pong = Fighter(280, 10, height, "o", "l", canvas)
ball = Ball(width // 2 - 5, height // 2 - 5, width, height, canvas)

canvas.create_line(width // 2, 0, width // 2, height)

canvas.pack()

root.after(0, loop)
root.mainloop()