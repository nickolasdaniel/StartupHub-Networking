from tkinter import *
import piplates.RELAYplate as RELAY

class password:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.passWord = StringVar()
        f = open("password.txt", 'r')
        self.passWord.set(f.readline())
        self.text = StringVar()
        self.text.set("SET PASSWORD: ")
        label = Label(frame, textvariable=self.text)
        label.grid(row = 0)
        entry = Entry(frame, textvariable=self.passWord)
        entry.grid(row=0, column=1)
        self.button = Button(frame, text="Confirm", command=self.Confirm)
        self.button.grid(row = 0, column =3)
    def Confirm(self):
        d=open("password.txt", 'w')
        d.write(self.passWord.get())

class GuiButton:
    def __init__(self, relay, textbutton, master,  status = False):
        frame = Frame(master)
        frame.pack()
        self.relay = relay
        self.status = {True: "STATUS: ON",
                       False: "STATUS: OFF"}
        self.deviceStatus = status
        self.text = StringVar()
        self.text.set(self.status[self.deviceStatus])
        self.button = Button(frame, text=textbutton, command = self.toggle)
        #self.button.pack()
        self.button.grid(row = relay+1)
        self.label = Label(frame, textvariable = self.text)
        #self.label.pack()
        self.label.grid(row = relay+1, column = 1)
    def toggle(self):
        RELAY.relayTOGGLE(0, self.relay)
        self.deviceStatus = not self.deviceStatus
        self.text.set(self.status[self.deviceStatus])

def dec_to_bin(x):
    return int(bin(x)[2:])

class relee:
    def __init__(self, relayNum, root):
        self.relays=[]
        for i in range(1, 8):
            self.relays.append(GuiButton(i, 'Relay '+str(i), root))
    def GetState(self):
        states = RELAY.relaySTATE(0)
        states = dec_to_bin(states)
        for i in range (0, len(self.relays)):
            status = states%10
            states = states/10
            self.relays[i].deviceStatus = status




root = Tk()
p = password(root)
RL = relee(7, root)

root.mainloop()