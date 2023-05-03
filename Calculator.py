from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("465x580")
root.minsize(465, 575)
root.maxsize(465, 584)
root.title("Calculator APPARKY")
root.wm_iconbitmap("calculator.ico")
root.configure(backgroun="yellow")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=20, pady=15, padx=10)

# Frame 1 which include 9, 8, 7 & C

frame = Frame(root, bg="gray")
b1 = Button(frame, text="9", font="lucida 35 bold", )
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame, text="8", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame, text="7", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

b4 = Button(frame, text="C", font="lucida 35 bold", padx=38)
b4.pack(side=RIGHT, padx=10, pady=5)
b4.bind("<Button-1>", click)
frame.pack(fill=X)

# Frame 2 which include 6, 5, 4 & %

frame2 = Frame(root, bg="gray")
b1 = Button(frame2, text="6", font="lucida 35 bold")
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame2, text="5", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame2, text="4", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

b4 = Button(frame2, text="%", font="lucida 35 bold", padx=34)
b4.pack(side=RIGHT, padx=10, pady=5)
b4.bind("<Button-1>", click)
frame2.pack(fill=X)

# Frame 3 whu=ich include 3, 2, 1 & (+, -)

frame3 = Frame(root, bg="gray")
b1 = Button(frame3, text="3", font="lucida 35 bold")
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame3, text="2", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame3, text="1", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

frame0 = Frame(frame3, bg="gray")
b4 = Button(frame0, text="+", font="lucida 35 bold", padx=5)
b4.pack(side=RIGHT, pady=5)
b4.bind("<Button-1>", click)

b5 = Button(frame0, text="-", font="lucida 35 bold", padx=7)
b5.pack(side=RIGHT, pady=5)
b5.bind("<Button-1>", click)
frame0.pack(side=RIGHT, padx=10, fill=X)
frame3.pack(fill=X)

# Frame 4 whu=ich include (.), 0, (=) & (* /)

frame4 = Frame(root, bg="gray")
b1 = Button(frame4, text=".", font="lucida 35 bold", padx=7.1)
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame4, text="0", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame4, text="=", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

frame0 = Frame(frame4, bg="gray")
b4 = Button(frame0, text="*", font="lucida 35 bold", padx=8)
b4.pack(side=RIGHT, pady=5)
b4.bind("<Button-1>", click)

b5 = Button(frame0, text="/", font="lucida 35 bold", padx=10)
b5.pack(side=RIGHT, pady=5)
b5.bind("<Button-1>", click)
frame0.pack(side=RIGHT, padx=10, fill=X)
frame4.pack(fill=X)

frame5 = Frame(root, bg="gray")
b = Button(text="Close", command=quit, font="bold 30", bg="red", fg="yellow")
b.pack(fill=X)
frame5.pack(fil=X)

root.mainloop()
