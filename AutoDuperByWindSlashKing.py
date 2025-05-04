import threading
import time

import win32api, win32con
import keyboard
import PySimpleGUI as sg
import webbrowser

import sys
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
import os

delayLeft = 2
delayRight = 0.1
script_running = False

def rightClicker():
    print("rightClicker activated")
    time.sleep(10)
    global script_running
    global delayRight
    while not keyboard.is_pressed('alt') and script_running:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(delayRight)

def leftClicker():
    print("leftClicker activated")
    time.sleep(12)
    global script_running
    global delayLeft
    while not keyboard.is_pressed('alt') and script_running:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(delayLeft)

def start_clicking_threads():
    t1 = threading.Thread(target=rightClicker)
    t2 = threading.Thread(target=leftClicker)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Script Finished Clicking")
    sg.popup_ok('Finished Duping', title='Script Stopped')

def main():
    menu = ['&Discord', ['ryk_cbaool2025']], ['&Youtube', ['Subscribe']]
    layout = [
        [sg.Menu(menu)],
        [sg.Text('Left click delay: '), sg.Slider(range=(1, 10), default_value=2, orientation='h', size=(20, 20)), sg.Text('seconds')],
        [sg.Text('Right click delay: '), sg.Spin(initial_value=0, values=(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0), size=(5, 5)), sg.Text('seconds')],
        [sg.Text('Default delay is recommended')],
        [sg.Button('Start Duping'), sg.Button("Help"), sg.Text('', size=(22, 0)), sg.Button('Exit')],
        [sg.StatusBar('Script not running', key='-STATUS-')]
    ]
    window = sg.Window('Item Frame Duper by WindSlashKing', layout, size=(450, 180), font='bold', icon=r"item_frame.ico")

    while True:
        event, values = window.read()
        if event == 'Help':
            sg.popup('Instructions', 'I recommend leaving the click delays as they are.\nWhen you start the script you have 10 seconds to switch to Minecraft and get into position. To stop the script hold the ALT key for a few seconds.')
        if event == 'Start Duping':
            window['Start Duping'].update(disabled=True)
            print('pressed button - activate script')
            window['-STATUS-'].update('Script is now running...')

            # Open YouTube subscription link
            webbrowser.open('https://www.youtube.com/@ryk_cbaool?sub_confirmation=1')

            global delayLeft
            global delayRight
            delayLeft = int(values[1])
            delayRight = float(values[2])
            global script_running
            script_running = True
            sg.popup_notify('Hold ALT to stop duping')
            start_clicking_threads()
            script_running = False
            window['-STATUS-'].update('Script is not running')
            window['Start Duping'].update(disabled=False)
        if event == 'Subscribe':
            webbrowser.open('https://www.youtube.com/@ryk_cbaool?sub_confirmation=1')
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()

if __name__ == '__main__':
    main()
