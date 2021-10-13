import pyautogui
import random as ran
import time

time.sleep(5)

## Currently This fonction spams 3 random letter words. you can change it by commenting line12. 

#i == how many times you want to spam.

#word == word you want to spam

def random_spam(i,word):
	while( i > 0 ):
	  pyautogui.leftClick()
	  pyautogui.hotkey('ctrl','a','delete')
	  word = chr(ran.randint(97,121)) + chr(ran.randint(97,121)) + chr(ran.randint(97,121))
	  pyautogui.write(word)
	  pyautogui.press('enter')
	  i-= 1
		

# HOW TO USE IT
# 1) build the program
# 2) click the chat you want to spam mesages (YOU HAVE 5 SECONDS FOR This)
# 3) dont move your mouse until loop is done. just chill and prank your friend :)
