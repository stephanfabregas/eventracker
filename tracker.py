import time
from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style, Canvas

class Display(Canvas):

    KEYS = {"Left":"Left", "Right":"Right", "Up":"Both", "Down":"Neither"}

    def __init__(self, parent):
        super(Display, self).__init__()

        self.parent = parent
        self.initDisplay()
        self.pack()

    def initDisplay(self):
        self.currentEpoch = 0
        self.savedEpoch = 0
        # self.startTime

        self.state = "NA"

        self.drawStatus()
        self.bind_all("<Key>", self.onKeyPressed)
        # bind the button press events as well

        self.after(DELAY, self.onTimer())

    def drawStatus(self):
        self.create_text(20, 30, anchor=W, text=self.state)

    def onKeyPressed(self, e):
        self.synch()

        key = e.keysym
        self.setState(key)

        self.onEvent()

    # Need to add method(s) for button clicks

    def setState(self, key):
        if key in Display.KEYS:        
            self.state = Display.KEYS[key]

    def onEvent(self):
        self.drawStatus()

    def onTimer(self):
        self.synch()
        self.after(DELAY, self.onTimer())

    def synch(self):
        self.setCurrentEpoch()
        n = checkEpoch()
        if n > 0:
            if n > 1:
                for i in range(n-1):
                    self.updateFile("NA") # Add a note?
            self.updateFile(self.state)
            self.savedEpoch = self.currentEpoch
            self.state = "NA"

    def updateFile(self, data):
        # Open file
        # Write/append data
        # Close file

    def setCurrentEpoch(self):
        t = int(time.time()/30)
        if self.currentEpoch != t:
            self.currentEpoch = t
        # Also look for big changes in time
            # If there's a big change, add a flag

    def checkEpoch(self):
        # return self.currentEpoch-self.savedEpoch

class Tracker(Frame):

    def __init__(self, parent):
        super(Tracker, self).__init__(parent)

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

