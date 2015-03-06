import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class Display(tk.Canvas):

    KEYS = {"Left":"Left", "Right":"Right", "Up":"Both", "Down":"Neither"}
    DELAY = 200

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        self.parent = parent
        self.initDisplay()

    def initDisplay(self):
        self.currentEpoch = int(time.time()/30)
        self.savedEpoch = int(time.time()/30)

        self.state = "NA"

        self.bind_all("<Key>", self.onKeyPressed)
        self.create_text(20, 30, anchor=tk.W, text=self.state, tag="state")

        self.after(Display.DELAY, self.onTimer)

    def drawStatus(self):
        status = self.find_withtag("state")
        self.delete(status[0])
        self.create_text(20, 30, anchor=tk.W, text=self.state, tag="state")

    def onKeyPressed(self, e):
        self.synch()

        try:
            key = e.keysym
        except AttributeError:
            key = e

        self.setState(key)
        self.onEvent()

    def setState(self, key):
        if key in Display.KEYS:        
            self.state = Display.KEYS[key]

    def onEvent(self):
        self.drawStatus()

    def onTimer(self):
        self.synch()
        self.onEvent()
        self.after(Display.DELAY, self.onTimer)

    def synch(self):
        self.setCurrentEpoch()
        n = self.checkEpoch()
        if n > 0:
            if n > 1:
                for i in range(n-1):
                    self.updateFile("NA") # Add a note?
            self.updateFile(self.state)
            self.savedEpoch = self.currentEpoch
            self.state = "NA"

    def updateFile(self, data):
        print(data)
        #pass
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
        return self.currentEpoch-self.savedEpoch

class Tracker(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Tracker")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        # Canvas to read out current state and previous state
        self.display = Display(self)
        self.display.grid(row=0, columnspan=2, sticky=(tk.W+tk.E))

        leftButton = tk.Button(self, text="Left", command=self.lbutton)
        leftButton.grid(row=1, column=0)
        rightButton = tk.Button(self, text="Right", command=self.rbutton)
        rightButton.grid(row=1, column=1)
        neitherButton = tk.Button(self, text="Neither", command=self.nbutton)
        neitherButton.grid(row=1, column=2)
        bothButton = tk.Button(self, text="Both", command=self.bbutton)
        bothButton.grid(row=1, column=3)

        exitButton = tk.Button(self, text="Exit", command=self.onExit)
        exitButton.grid(row=2, column=0)

        self.pack()

    def lbutton(self):
        self.display.onKeyPressed("Left")

    def rbutton(self):
        self.display.onKeyPressed("Right")

    def nbutton(self):
        self.display.onKeyPressed("Down")

    def bbutton(self):
        self.display.onKeyPressed("Up")

    def onExit(self):
        self.quit()

def main():
    root = tk.Tk()
    app = Tracker(parent=root)
    app.mainloop()

if __name__ == '__main__':
    main()

