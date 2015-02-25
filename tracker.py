from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style, Canvas

class Display(Canvas):

    def __init__(self, parent):
        super(Display, self).__init__()

        self.parent = parent
        self.initDisplay()
        self.pack()

    def initDisplay(self):
        self.epoch = 0
        self.savedEpoch = 0
        # self.startTime
        # self.currentTime

        self.state = "NA"

        self.drawStatus()
        self.bind_all("<Key>", self.onKeyPressed)
        # bind the button press events as well

        self.after(DELAY, self.onTimer())

    def drawStatus(self):
        self.create_text(20, 30, anchor=W, text=self.state)

    def onKeyPressed(self, e):
        # Check if in new epoch, checkEpoch method
        key = e.keysym

        # Update state (maybe a setState method)
        if key == "Left":
            self.state = "Left"

        if key == "Right":
            self.state = "Right"

        if key == "Up":
            self.state= = "Both"

        if key == "Down":
            self.state = "Neither"

        self.onEvent()

    def onEvent(self):
        # Use self.state to update the canvas
        self.drawStatus()

    def onTimer(self):
        # Open file, write last epoch, close file
        # Maybe not first... check logic
        self.updateFile()
        # Need to figure out how to prioritize this event...
        # Track system time to check current Epoch #,
        # Update self.currentTime
        # Update self.epoch
        # For range(checkEpoch (# unsaved epochs) - 1):
            # Update epoch
            # UpdateFile with NA
            # If not, 

    def updateFile(self):
        # Open file
        # Write/append current epoch
        # Update last written epoch: self.savedEpoch
        # Close file

    def checkEpoch(self):
        # return self.epoch-self.savedEpoch

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

