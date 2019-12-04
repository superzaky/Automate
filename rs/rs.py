import pyautogui
import random
import time
while True:
	hor = random.randint(392,419)
	ver = random.randint(576,603)
	tim = random.uniform(0.2,0.4)
	timee = random.uniform(1.1,1.8)
	spawntime = 1 
	# spawntime = 6 
	waitime = random.uniform(1, 2)
	awayHor = random.randint(489,589)
	awayVer = random.randint(476,503)
	towardVer = random.randint(228,234)
	# time.sleep(12)
	time.sleep(1)
	im = pyautogui.screenshot()
	# if im.getpixel((197,456)) == (35, 41, 44):    # Checks if a point at health bar has turned dark

	guard_head_loc = pyautogui.locateOnScreen('./rs/screenshots/guard_head.PNG')
	print('head lcoation = ' )
	print( guard_head_loc)
	if guard_head_loc != None:
		pyautogui.moveTo(guard_head_loc.width, guard_head_loc.height,tim)
		pyautogui.click()
		print('click')
	

	# if im.getpixel((479,490)) == (142, 29, 30): #Checks if regenerate ability is lit up (meaning out of combat)
	time.sleep(spawntime) # wait for spawns , in case that cause "out of combat"
	# if im.getpixel((479,490)) == (142, 29, 30):

	guard_body_loc = pyautogui.locateOnScreen('./rs/screenshots/guard_body.PNG', grayscale=True, confidence=.5)
	print('guard_body_loc lcoation = ' )
	print( guard_body_loc)
	if guard_body_loc != None:
		pyautogui.moveTo(guard_body_loc.width, guard_body_loc.height, tim)
		pyautogui.click()
		print('click2')

	# pyautogui.moveTo(int(awayHor),int(awayVer),timee)
	# pyautogui.click()
	# print('click2')
	# time.sleep(waitime)


	# pyautogui.moveTo(658,towardVer,timee)
	# pyautogui.click()
	# print('click3')
	# pyautogui.moveTo(int(hor),int(ver),timee)
	# else:
	# 	continue
