import threading
import time
import win32api, win32con
import keyboard
import PySimpleGUI as sg
import webbrowser

# === Globals ===
delayLeft = 2
delayRight = 0.1
script_running = False

# === Functions ===
def rightClicker():
    print("rightClicker activated")
    time.sleep(10)
    global script_running, delayRight
    while not keyboard.is_pressed('alt') and script_running:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(delayRight)

def leftClicker():
    print("leftClicker activated")
    time.sleep(12)
    global script_running, delayLeft
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

# === GUI Code ===
def main():
    right_delays = [round(x * 0.1, 1) for x in range(11)]
    
    layout = [
        [sg.Text('Left click delay: '), sg.Slider(range=(1, 10), default_value=2, orientation='h', size=(20, 20)), sg.Text('seconds')],
        [sg.Text('Right click delay: '), sg.Spin(values=right_delays, initial_value=0.1, size=(5, 5)), sg.Text('seconds')],
        [sg.Text('Default delay is recommended')],
        [sg.Button('Start Duping'), sg.Button('Help'), sg.Button('Subscribe'), sg.Button('Exit')],
        [sg.StatusBar('Script not running', key='-STATUS-')]
    ]

    window = sg.Window('Item Frame Duper by ryk_cbaool', layout, size=(450, 180), font='bold', icon='item_frame.ico')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Help':
            sg.popup('Instructions', 'Leave the delays as-is unless needed.\nAfter clicking Start, you have 10 seconds to switch to Minecraft.\nHold ALT to stop the script.')
        elif event == 'Subscribe':
            webbrowser.open('https://www.youtube.com/@ryk_cbaool?sub_confirmation=1')
        elif event == 'Start Duping':
            webbrowser.open('https://www.youtube.com/@ryk_cbaool?sub_confirmation=1')
            window['Start Duping'].update(disabled=True)
            window['-STATUS-'].update('Script is now running...')
            global delayLeft, delayRight, script_running
            delayLeft = int(values[0])
            delayRight = float(values[1])
            script_running = True
            sg.popup_notify('Hold ALT to stop duping')
            start_clicking_threads()
            script_running = False
            window['-STATUS-'].update('Script is not running')
            window['Start Duping'].update(disabled=False)

    window.close()


if __name__ == '__main__':
    main()

