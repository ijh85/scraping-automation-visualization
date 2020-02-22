'''
lecture2_example12.py. Import subprocess and pyautogui. Launch
LaTeX, add boilerplate code, and compile.  
'''

import subprocess
import pyautogui
import time

# Define function to return center of image.

imagePath = '../images/'

def returnCenter(filename, path=imagePath):
	path = imagePath
	location = pyautogui.locateOnScreen(path+filename)
	center = pyautogui.center(location)
	return center

# Launch LaTeX.

subprocess.Popen('open /Applications/TeXShop.app', shell=True)

# Create LaTeX document.

time.sleep(2)
pyautogui.typewrite('\\documentclass[12pt]{article}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\begin{document}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\title{The Fisher Equation}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\author{}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\date{}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\maketitle', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\begin{equation}', interval=0.05)
pyautogui.press('enter')
pyautogui.typewrite('i \\approx r + \pi', interval=0.05)
pyautogui.press('enter')
pyautogui.typewrite('\\end{equation}', interval=0.05)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite('\\end{document}', interval=0.05)

# Typeset document.

typesetCenter = returnCenter('typeset.png')
pyautogui.moveTo(typesetCenter, duration=0.25)
pyautogui.click()
time.sleep(2)
pyautogui.press('enter')
