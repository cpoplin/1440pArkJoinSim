import pyautogui as pag
import time
import sys
import keyboard
import easygui as eg
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# --- IMPORTANT: Now, modify all your image paths in sim_attempt.py ---
# For example, if you had:
# image_path = 'join_game.png'
#
# You MUST change it to:
join_game_path = resource_path('join_game.png')
# location = pag.locateCenterOnScreen(join_game_path, confidence=0.7)

# Do this for ALL your images:
accept_path = resource_path('accept.png')
back_path = resource_path('back.png')
cancel_path = resource_path('cancel.png')
join_path = resource_path('join.png')
search_path = resource_path('search.png')
start_path = resource_path('start.png')
testing_path = resource_path('testing.png')


#simple enterbox
server_number = user_name = eg.enterbox(
    msg="Please enter the server number to sim into, close the sim with f5:",
    title="Server Input",
    default="2411" # Optional: default text in the input field
)

def on_f5_press():
    eg.msgbox(
    msg="User has pressed f5, exiting program",
    title="Sim Exited"
    )
    global running
    running = False
    print("exiting program, f5 pressed")
    sys.exit(0)

keyboard.add_hotkey('f5', on_f5_press)




running = True

while running:
    time.sleep(1)
    join_button_found = False
    try: 
        #look for the join game button
        join_location = pag.locateCenterOnScreen(join_game_path, confidence=0.7)
        pag.click(join_location.x, join_location.y)
        time.sleep(.5)
    except pag.ImageNotFoundException:
        pass
    try:
        #look for the search
        search_location = pag.locateCenterOnScreen(search_path, confidence=0.7)
        pag.click(search_location.x, search_location.y)
        pag.write(server_number)
        pag.click(1653, 451)
        time.sleep(1)
        pag.click(1653, 451)
        time.sleep(.5)
    except pag.ImageNotFoundException:
        pass
    try:
        #look for the join
        join_location = pag.locateCenterOnScreen(join_path, confidence=0.7)
        pag.click(join_location.x, join_location.y)
        time.sleep(.5)
    except pag.ImageNotFoundException:
        pass
    try:
        #look for the cancel button
        cancel_location = pag.locateCenterOnScreen(cancel_path, confidence=0.7)
        pag.click(cancel_location.x, cancel_location.y)
        time.sleep(.5)
        back_location = pag.locateCenterOnScreen(back_path, confidence=0.7)
        pag.click(back_location.x, back_location.y)
        time.sleep(.5)
    except pag.ImageNotFoundException:
        pass
    try:
        #look for the accept button that appears after a jebait
        accept_location = pag.locateCenterOnScreen(accept_path, confidence=0.7)
        pag.click(accept_location.x, accept_location.y)
        time.sleep(.5)
        start_location = pag.locateCenterOnScreen(start_path, confidence=0.7)
        pag.click(start_location.x, start_location.y)
        time.sleep(.5)
    except pag.ImageNotFoundException:
        pass
        
