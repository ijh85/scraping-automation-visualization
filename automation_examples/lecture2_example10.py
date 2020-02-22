'''
lecture2_example10.py. This example first imports the pyautogui module. It
then 1) returns the mouse's position on the screen; 2) return's the screen's
resolution; and 3) tests whether a given coordinate is located on the screen. 
'''

import pyautogui

pyautogui.PAUSE = 3
pyautogui.position()
pyautogui.size()
pyautogui.onScreen(3000, 3000)
pyautogui.onScreen(500, 500)