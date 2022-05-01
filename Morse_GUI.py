from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
import time

#define length of short and long pause inbetween dits and daas
sho = 0.25
lon = 0.75

#define and setup output pin
pin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

#initialise tkinter instance
box = Tk()

#define a morse dictionary, - representing daa, . representing dit
morse_code = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.",
"G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--",
"N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-",
"U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--.."}

#blink for a time equal to sho
def dit():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sho)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(sho)

#blink for a time equal to lon
def daa():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(lon)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(sho)

#punctuate letters with another long pause
def fin():
    time.sleep(lon)

#translates user input string into morse via the morse dictionary
def translate(word):
    morse = ""
    word = word.upper()
    
    for i in word:
        morse = morse + morse_code[i] + "|"
    return morse

#gets string from user, validates it as less than 13 characters long
def blink():
    global code
    string = code.get() 
    
    if len(string) > 12:
        print("Error: string of =< 12 only")
        return
    
    string = translate(string)
    print(string)
    
    #blinks the LED on pin by parsing the morse in a loop
    for i in string:
        if i == ".":
            dit()
        elif i == "-":
            daa()
        else:
            fin()
    
    #ends program and cleans up board
    GPIO.cleanup()
    box.destroy()



#creates label for window to alert user, 12 characters or less accepted
var = StringVar()
label = Label(box, textvariable=var)
var.set("Enter up to 12 characters: A-Z")
label.pack()

#creates widget for user entry
code = Entry(box)
code.pack()

#creates button to initiate blink of LED
b = Button(box, text='OK', command=blink)
b.pack(side = 'bottom')

#loops until interrupt
box.mainloop()
