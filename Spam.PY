import pyautogui
import random as ran
import time

time.sleep(3)

word = ""




def random_spam(i,word):
	while( i > 0 ):
	  pyautogui.leftClick()
	  pyautogui.hotkey('ctrl','a','delete')
	  word = chr(ran.randint(97,121)) + chr(ran.randint(97,121)) + chr(ran.randint(97,121))
	  pyautogui.write(word)
	  pyautogui.press('enter')
	  i-= 1



def open_browser(i,Browser_name):
	while( i > 0):
	  pyautogui.press("win")
	  word = Browser_name
	  pyautogui.write(word)
	  pyautogui.press("enter")
	  i-= 1


def Web_Serch(word):


	pyautogui.press("win")
	pyautogui.typewrite("brow")
	pyautogui.press("enter")
	time.sleep(0.5)
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	pyautogui.press("f11")
	pyautogui.leftClick()
	pyautogui.leftClick()
	time.sleep(3)


def volMax(i):
	while(i > 0):
		#pyautogui.press("volumeUp")
		pyautedgei.press("space")
		i-=1  


def browser_Depace(i):
	for i in range(i):
		pyautogui.press("tab")


def dowloand_pass_edge():

	#open Browser
	open_browser(1,"edge")
	time.sleep(1)


   #Go To settings
	pyautogui.hotkey('alt','f')
	pyautogui.typewrite("s")

   
   #Go To Passwords
	time.sleep(2)
	browser_Depace(8)
	pyautogui.press("enter")


   #Dowloand Passwords
	browser_Depace(8)
	pyautogui.press("enter")
	pyautogui.press('down')
	pyautogui.press("enter")
	time.sleep(0.5)
	pyautogui.press("enter")
	time.sleep(0.5)
	pyautogui.press("enter")





#dowloand_pass_edge()
#Web_Serch("MY Name")
random_spam(90,"")
#open_browser(5,"edge")
#Web_Serch("https://www.youtube.com/watch?v=FSuFRasPMLQ&list=RDFSuFRasPMLQ&start_radio=1")