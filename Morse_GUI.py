from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
import time

sho = 0.25
lon = 0.75

pin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

box = Tk()

morse_code = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.",
"G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--",
"N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-",
"U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--.."}

def dit():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sho)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(sho)

def daa():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(lon)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(sho)

def fin():
    time.sleep(lon)

def translate(word):
    morse = ""
    word = word.upper()
    for i in word:
        print(i)
        print(morse_code[i])
        morse = morse + morse_code[i] + "|"
    return morse

def blink():
    global code
    string = code.get() 
    if len(string) > 12:
        print("Try again")
        return
    print (string)
    string = translate(string)
    print(string)
    for i in string:
        if i == ".":
            dit()
        elif i == "-":
            daa()
        else:
            fin()
            
    #GPIO.cleanup()
    #box.destroy()


def close():
    GPIO.cleanup()
    box.destroy()

var = StringVar()
label = Label( box, textvariable=var, relief=RAISED )

var.set("Enter up to 12 characters: A-Z")
label.pack()


code = Entry(box)
code.pack()
code.focus_set()

b = Button(box, text='OK', command=blink)
b.pack(side = 'bottom')

#r_but = Button(box, text = 'GO', bg = 'green', command = lambda: blink(translate(input))
#r_but.grid(row = 0, column = 1)

#stop = Button(box, text = 'Exit', command = close)
#stop.grid(row = 2, column = 2)

box.protocol("WM_DELETE_WINDOW", close)

box.mainloop()
