import tkinter as tk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
red=11
green=13
yellow=15
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
def RedLight():
    GPIO.output(green,GPIO.LOW)
    GPIO.output(yellow,GPIO.LOW)
    GPIO.output(red,GPIO.HIGH)
def GreenLight():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.HIGH)
    GPIO.output(yellow,GPIO.LOW)
def BlueLight():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(yellow,GPIO.HIGH) 
def Quit():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(yellow,GPIO.LOW)
    GPIO.cleanup()
    window.destroy()
window = tk.Tk()
window.title('Traffic Light Control')
red_button = tk.Button(window, text='Turn RED', command=RedLight, bg='red', height=1, width=30)
red_button.pack()
green_button = tk.Button(window, text='Turn GREEN', command=GreenLight, bg='green', height=1, width=30)
green_button.pack()
yellow_button = tk.Button(window, text='Turn YELLOW', command=BlueLight, bg='blue', height=1, width=30)
yellow_button.pack()
exit_button = tk.Button(window, text='QUIT', command=Quit, bg='grey', height=1, width=30)
exit_button.pack()
window.mainloop()
