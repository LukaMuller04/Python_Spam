import pyautogui
import time

# Delay when program starts
time.sleep(5)


# i == how many times you want to spam.

# word == word you want to spam

def random_spam(i,word):
	while( i > 0 ):
	  pyautogui.leftClick()
	  pyautogui.write(word)
	  pyautogui.press('enter')
	  i-= 1
		

# HOW TO USE IT
# 1) build the program
# 2) click the chat you want to spam mesages (YOU HAVE 5 SECONDS FOR THIS!!!)
# 3) dont move your mouse until loop is done. just chill and prank your friend :)
random_spam(69420,"<3")
