from Tkinter import *

master = Tk()

canvas = Canvas(master, width=800, height=800, bg='white')
canvas.pack()

rectangle3 = canvas.create_rectangle(30, 30, 100,100, fill = "red")

def callback(event):
    print "clicked at", event.x, event.y
    if (event.x > 30 and event.x < 100) and (event.y > 31 and event.y < 100):
        print("YEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")



canvas.bind("<Button-1>", callback)

mainloop()
