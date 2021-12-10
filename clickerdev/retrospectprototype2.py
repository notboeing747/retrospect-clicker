from tkinter import *
from tkinter import ttk
from tkinter import Button as button
import pynput
import tkinter as tk
import time
import os
import sys
import html
import time
import random
import requests
import pyautogui
import configparser
import keyboard
import mouse as Mouse
from sys import platform
from pygame import mixer
from colorama import Fore
from pynput.mouse import Button, Controller

mixer.init()
master = Tk()
mouse = Controller()


master.geometry("400x200")
master.title("Retrospect")
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=3)

configParser = configparser.RawConfigParser()   
configFilePath = 'config.txt'
configParser.read(configFilePath)

fishing_rod_macro_key = configParser.get('config', 'fishing_rod_macro_key')
fishing_rod_slot = configParser.get('config', 'fishing_rod_slot')
fishing_rod_min_clickdelay = int(configParser.get('config', 'fishing_rod_min_clickdelay'))
fishing_rod_max_clickdelay = int(configParser.get('config', 'fishing_rod_max_clickdelay'))
fishing_rod_slot_switch_min_delay = int(configParser.get('config', 'fishing_rod_slot_switch_min_delay'))
fishing_rod_slot_switch_max_delay = int(configParser.get('config', 'fishing_rod_slot_switch_max_delay'))

def print_value1(val):
    max_cps_slider = round(float(val),1)
    cps_max.config(text=max_cps_slider)
    return w.get()

def print_value2(val):
    min_cps_slider = round(float(val),1)
    cps_min.config(text=min_cps_slider)
    return ss.get()
    
def print_value3(val):
    min_cps_slider = round(float(val),1)
    cps_min_rmb.config(text=min_cps_slider)
    return yy.get()
    
def print_value4(val):
    min_cps_slider = round(float(val),1)
    cps_max_rmb.config(text=min_cps_slider)
    return nn.get()

cps_max = ttk.Label(master, text="1", style="BW.TLabel")
cps_max.place(x=241,y=6)
cps_min = ttk.Label(master, text="1", style="BW.TLabel")
cps_min.place(x=241,y=25)
cps_min_rmb = ttk.Label(master, text="1", style="BW.TLabel")
cps_min_rmb.place(x=241,y=55)
cps_max_rmb = ttk.Label(master, text="1", style="BW.TLabel")
cps_max_rmb.place(x=241,y=75)
maxlabel = ttk.Label(master, text="Max LMB", style="BW.TLabel")
maxlabel.place(x=280,y=25)
minlabel = ttk.Label(master, text="Min LMB", style="BW.TLabel")
minlabel.place(x=280,y=6)
maxlabelrmb = ttk.Label(master, text="Min RMB", style="BW.TLabel")
maxlabelrmb.place(x=280,y=55)
minlabelrmb = ttk.Label(master, text="Max RMB", style="BW.TLabel")
minlabelrmb.place(x=280,y=75)
delaylabel = ttk.Label(master, text="", style="BW.TLabel")
delaylabel.place(x=2,y=180)
w = ttk.Scale(master, from_=1, to=20, orient=HORIZONTAL, command=print_value1)
w.place(x=137,y=6)
ss = ttk.Scale(master, from_=1, to=20, orient=HORIZONTAL, command=print_value2)
ss.place(x=137,y=25)
yy = ttk.Scale(master, from_=1, to=20, orient=HORIZONTAL, command=print_value3)
yy.place(x=137,y=55)
nn = ttk.Scale(master, from_=1, to=20, orient=HORIZONTAL, command=print_value4)
nn.place(x=137,y=75)
c = ttk.Checkbutton(master, text='Rod Macro', onvalue=1, offvalue=0)
c.place(x=2, y=5)
cc = ttk.Checkbutton(master, text='Click Sounds', onvalue=1, offvalue=0)
cc.place(x=2, y=25)
y = ttk.Checkbutton(master, text='RMB Clicker', onvalue=1, offvalue=0)
y.place(x=2, y=45)
vv = ttk.Checkbutton(master, text='Show Delay', onvalue=1, offvalue=0)
vv.place(x=2, y=65)

def task():
    if Mouse.is_pressed(button='x2'):
        randds = random.random()*0.1
        rands = random.random()*0.01
        randscop = 1.0/random.randint(int(w.get()),int(ss.get()))-rands*0.6
        randluck = random.randint(0,1000)
        mouse.press(Button.left)
        if "selected" in cc.state(): 
            mixer.music.load('default.wav')
            mixer.music.play()
        if randluck <=5:
            randscop = 0.032-(random.random()*0.01)
        if randluck >=800:
            randscop = 0.13-(random.random()*0.01)
        time.sleep(randds*0.61)
        mouse.release(Button.left)
        time.sleep(randscop*0.45)
        if "selected" in vv.state(): 
            delaylabel.config(text=f"Delay: [{round(randscop*0.45+randds*0.61, 3)} ms]")
        else:
            delaylabel.config(text="")
        
    if "selected" in y.state():
        if Mouse.is_pressed(button='x'):
            rands = random.random()*0.01
            randscop = 1/random.randint(int(yy.get()),int(nn.get()))-rands*0.6
            mouse.press(Button.right)
            if "selected" in cc.state(): 
                mixer.music.load('click1.wav')
                mixer.music.play()
            time.sleep(randscop*0.7)
            mouse.release(Button.right)
            time.sleep(randscop*0.3)
    if "selected" in c.state():
        if keyboard.is_pressed(fishing_rod_macro_key):
            keyboard.press(fishing_rod_slot)
            keyboard.release(fishing_rod_slot)
            time.sleep(random.randint(fishing_rod_slot_switch_min_delay,fishing_rod_slot_switch_max_delay)*0.001)
            mouse.click(Button.right)
            time.sleep(random.randint(fishing_rod_min_clickdelay,fishing_rod_max_clickdelay)*0.001)
            mouse.click(Button.right)
            time.sleep(random.randint(fishing_rod_slot_switch_min_delay,fishing_rod_slot_switch_max_delay)*0.001)
            keyboard.press("1")
            keyboard.release("1")

    master.after(1, task)

master.after(1, task)
master.mainloop()

mainloop()
