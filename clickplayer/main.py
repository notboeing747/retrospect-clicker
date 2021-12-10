import time
import random
import mouse as Mouse
from tkinter import *
from tkinter import ttk
from pygame import mixer
from tkinter import Button as button
from pynput.mouse import Button, Controller

mouse = Controller()

mixer.init()
mixer.music.load('default.wav')

master = Tk()
master.title("Gato Clicker")
master.geometry("265x150")

def repeat():
	with open(f"{clicker_profile.get()}.txt", "r") as file:
		global w
		full = file.read()
		delays = list(map(str, full.split()))
		load_button.config(text=clicker_profile.get())

	if Mouse.is_pressed(button='x2'):
		delay = float(random.choice(delays))
		delay_rand = random.randint(20,55)*0.001
		mouse.press(Button.left)
		if "selected" in click_sounds.state(): 
			mixer.music.play()
		time.sleep(delay_rand)
		if delay <= delay_rand:
			delay_rand = delay*0.8
		mouse.release(Button.left)
		time.sleep(delay-delay_rand)
		print(delay-delay_rand+delay_rand)
	
	master.after(1, repeat)

clicker_profile = StringVar()
clicker_profile.set("Jitter")

presets = ["Jitter", "Butterfly", "Custom"]

profile = Label(master, text="Clicker Profile:")
profile.place(x=5, y=5)
conditonals_label = Label(master, text="Options:")
conditonals_label.place(x=5, y=50)
click_sounds = ttk.Checkbutton(master, text="Click Sounds")
click_sounds.place(x=5, y=69)
load_button = OptionMenu(master, clicker_profile, *presets)
load_button.place(x=2, y=21)
load_button.config(bd=1, width=24, anchor="w")

master.after(1, repeat)
master.mainloop()
