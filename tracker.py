from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style, Canvas

class Display(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self)

        self.parent = parent
        self.initDisplay()
        self.pack()

    def initDisplay(self):
        self.timer = 30
        self.state = "NA"

        self.drawStatus()
        self.bind_all("<Key>", self.onKeyPressed)

    def drawStatus(self):
        self.create_text(20, 30, anchor=W, text=self.state)

    def onKeyPressed(self, e):
        key = e.keysym

        if key == "Left":
            self.state = "Left"

        if key == "Right":
            self.state = "Right"

        if key == "Up":
            self.state= = "Both"

        if key == "Down":
            self.state = "Neither"

    def onTimer(self):
        self.drawStatus()
        self.after(DELAY, self.onTimer)

    def onEpoch(self):
        self.updateFile()
        # Open file, write last epoch, close file
        # Consider event handlers...
        self.after(EPOCH, self.onEpoch)

    def updateFile(self):

class Tracker(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Tracker")
        self.style = Style()
        self.style.theme_use("default")

        Style().configure("TButton", padding=(0,5,0,5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        # Canvas to read out current state and previous state
        self.display = Display(parent)
        display.grid(row=0, columnspan=2, sticky=W+E)
        #

        leftButton = Button(self, text="Left")
        leftButton.grid(row=1, column=0)
        rightButton = Button(self, text="Right")
        rightButton.grid(row=1, column=1)
        neitherButton = Button(self, text="Neither")
        neitherButton.grid(row=1, column=2)
        bothButton = Button(self, text="Both")
        bothButton.grid(row=1, column=3)

        exitButton = Button(self, text="Exit")
        exitButton.grid(row=2, column=0)

        self.pack()

def main():

    root = Tk()
    app = Tracker(root)
    root.mainloop()

if __name__ == '__main__':
    main()

