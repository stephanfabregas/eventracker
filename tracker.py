import pygame.mixer as pyg
import serial
import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class Display(tk.Canvas):

    DELAY = 200

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=300, height=20)

        self.parent = parent

        self.create_text(150, 10, anchor=tk.CENTER, text=self.parent.state, tag="state")
        self.after(Display.DELAY, self.onTimer)

    def drawStatus(self):
        status = self.find_withtag("state")
        self.delete(status[0])
        self.create_text(150, 10, anchor=tk.CENTER, text=self.parent.state, tag="state")

    def onTimer(self):
        self.parent.trackSerial()
        self.parent.synch()
        self.drawStatus()
        self.after(Display.DELAY, self.onTimer)

class Tracker(tk.Frame):

    KEYS = {"Left":"Left", "Right":"Right", "Up":"Both", "Down":"Neither",
            "h":"Left", "j":"Neither", "k":"Both", "l":"Right", "0":"Left",
            "1":"Right", "2":"Both", "3":"Neither"}
    STATES = {"Left":0, "Right":1, "Both":2, "Neither":3, "NA":4}
    STATES2 = ["Left", "Right", "Up", "Down", "NA"]
    EPOCH_LENGTH = 30
    SOUND = "smb2_cherry.wav"
    OUTFN = "tracker.csv"

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.currentEpoch = int(time.time()/Tracker.EPOCH_LENGTH)
        self.savedEpoch = int(time.time()/Tracker.EPOCH_LENGTH)
        self.state = "NA"

        pyg.init()
        pyg.music.load(Tracker.SOUND)

        self.bind_all("<Key>", self.onKeyPressed)
        self.initUI()

        self.port = '/dev/ttyACM0'
        self.baudrate = 9600
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)        
        self.trackSerial()


    def initUI(self):

        self.parent.title("Tracker")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        self.display = Display(self)
        self.display.grid(row=0, columnspan=4, sticky=(tk.W+tk.E))

        leftButton = tk.Button(self, text="Left",
                               command=lambda: self.onKeyPressed("Left"))
        leftButton.grid(row=1, column=0)
        rightButton = tk.Button(self, text="Right",
                                command=lambda: self.onKeyPressed("Right"))
        rightButton.grid(row=1, column=1)
        neitherButton = tk.Button(self, text="Neither",
                                  command=lambda: self.onKeyPressed("Down"))
        neitherButton.grid(row=1, column=2)
        bothButton = tk.Button(self, text="Both",
                               command=lambda: self.onKeyPressed("Up"))
        bothButton.grid(row=1, column=3)

        exitButton = tk.Button(self, text="Exit",
                               command=lambda: self.onKeyPressed("q"))
        exitButton.grid(row=2, columnspan=4)

        self.pack()

    def onKeyPressed(self, e):
        try:
            key = e.keysym
        except AttributeError:
            key = e

        if key == "q":
            self.onExit()

        self.setState(key)
        self.ser.write("W"+str(Tracker.STATES[self.state]))
        self.display.drawStatus()

    def setState(self, key):
        if key in Tracker.KEYS:        
            self.state = Tracker.KEYS[key]

    def onExit(self):
        self.synch()
        self.quit()

    def synch(self):
        self.setCurrentEpoch()
        n = self.checkEpoch()
        if n > 0:
            if n > 1:
                for i in range(n-1):
                    self.updateFile(i, "NA, synch problem")
            self.updateFile(0, self.state + ",")
            self.savedEpoch = self.currentEpoch
            self.state = "NA"
            self.ser.write("W"+str(Tracker.STATES[self.state]))
            pyg.music.play()

    def trackSerial(self):
        if self.ser.inWaiting() > 0:
            thisByte = self.ser.read()
            self.ser.flushInput()
            if thisByte == "E":
                self.ser.write("W"+str(Tracker.STATES[self.state]))
            elif thisByte in ["0", "1", "2", "3", "4"]:
                self.setState(Tracker.STATES2[int(thisByte)])
            else:
                self.ser.write("RR")

    def updateFile(self, n, data):
        with open(Tracker.OUTFN, "a") as f:
            f.write(str(self.savedEpoch+n+1) + "," + data + "\n")

    def setCurrentEpoch(self):
        t = int(time.time()/Tracker.EPOCH_LENGTH)
        if self.currentEpoch != t:
            self.currentEpoch = t

    def checkEpoch(self):
        return self.currentEpoch-self.savedEpoch

def main():
    root = tk.Tk()
    app = Tracker(parent=root)
    app.mainloop()

if __name__ == '__main__':
    main()

