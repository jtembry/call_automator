from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import argparse
import getpass

parser = argparse.ArgumentParser(description='Flags for Redux tools, video calls, or headless Chrome')
parser.add_argument('--redux', action="store_const", dest='redux', default=0, const='./resources/Redux-DevTools_v2.17.0.crx')
parser.add_argument('--video', action="store_const", dest='video', default=0, const="//button[@id='btnVideo070']")
parser.add_argument('--headless', action="store_const", dest='headless', default=0, const="headless")
parser.add_argument('--taco', action="store_const", dest="taco", default=0, const='use-file-for-fake-video-capture=./resources/taco.mjpeg')
args = parser.parse_args()

def initialize():
	userinput = input('1: local development\
	2: Mayhem\
	3: QA\
	4: Stable ')
	calls = input('Please enter the number of calls you wish to make: ')
	username = input('Username: ')
	password = getpass.getpass("Enter your password: ")

	if userinput == '1':
		website = 'http://localhost:3000/login'
		print('Local')
		login(website, calls, username, password)
	if userinput == '2':
		website = 'https://video-mayhem.cyracomdev.com'
		print('Mayhem')
		login(website, calls, username, password)
	if userinput == '3':
		website = 'https://video.cyracomqa.com'
		print('QA')
		login(website, calls, username, password)
	if userinput == '4':
		website = 'https://video.cyracomdev.com'
		print('Stable')
		login(website, calls, username, password)
	else:
		print('not an option')

def login(website, calls, username, password):
	options = Options()
	options.add_argument('window-size=1920x1080')
	options.add_argument('ignore-certificate-errors') 
	options.add_argument("use-fake-ui-for-media-stream")
	options.add_argument("use-fake-device-for-media-stream")
	options.add_argument("mute-audio")
	# To Enable the notification (Allow Microphone and Camera)
	# Pass the argument 1 to allow and 2 to block
	options.add_experimental_option("prefs", { \
	    "profile.default_content_setting_values.media_stream_mic": 1, 
	    "profile.default_content_setting_values.media_stream_camera": 1,
	    "profile.default_content_setting_values.geolocation": 1, 
	    "profile.default_content_setting_values.notifications": 1 
		})

	if args.redux != 0:
		options.add_extension(args.redux)
		print("Redux Tools On")
	if args.headless != 0:
		options.add_argument(args.headless)
		print("Running Headless")
	if args.taco != 0:
		options.add_argument(args.taco)
		print("Taco Time")

	driver = webdriver.Chrome(executable_path = '/bin/chromedriver', chrome_options = options)
	wait = WebDriverWait(driver, 15)
	driver.get(website)
	time.sleep(1)
	print('Current URL: ', driver.current_url)
	bypass = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'small.mat-hint')))
	time.sleep(1)
	action_chains = ActionChains(driver)
	action_chains.double_click(bypass).perform()
	time.sleep(1)
	checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mat-checkbox-input")))
	action_chains.double_click(checkbox).perform()
	time.sleep(1)
	element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='txtEmail']")))
	element.send_keys(username)
	element.send_keys(Keys.RETURN)
	wait.until(lambda driver: driver.current_url != website)
	userNameInput = wait.until(EC.visibility_of_element_located((By.ID, "userNameInput")))
	userNameInput.send_keys(username)
	passwordInput = wait.until(EC.visibility_of_element_located((By.ID, "passwordInput")))
	passwordInput.send_keys(password)
	submitButton = wait.until(EC.visibility_of_element_located((By.ID, "submitButton")))
	submitButton.send_keys(Keys.RETURN)
	try:
		makeCalls(driver, calls, action_chains, wait)
	finally:
		endTest(driver,0)


def makeCalls(driver, calls, action_chains, wait):
	input('press any button to make calls')
	print('MAKING CALLS')
	time.sleep(1)
	counter = 0
	start_time = 0
	for x in range(int(calls)):
		last_start_time = start_time
		print('Call number: ', counter)
		languageInput = wait.until(EC.visibility_of_element_located((By.ID, "srchLanguages")))
		languageInput.send_keys('Spanish')
		action_chains = ActionChains(driver)
		if args.video != 0:
			btnVideo = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@id, 'btnVideo')]")))
			if btnVideo:
				start_time = time.perf_counter()
			btnVideo.send_keys(Keys.RETURN)
		else:
			btnVoice = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@id, 'btnVoice')]")))
			if btnVoice:
				start_time = time.perf_counter()
			btnVoice.send_keys(Keys.RETURN)
		action_chains.move_by_offset(5, 0)
		action_chains.move_by_offset(-5, 0)
		action_chains.move_by_offset(5, 0)
		action_chains.move_by_offset(-5, 0)
		action_chains.move_by_offset(5, 0)
		action_chains.move_by_offset(-5, 0)
		action_chains.perform()
		btnEnd = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnEndCall']")))
		btnEnd.click()
		counter += 1
		print('difference between call start times: ', start_time - last_start_time)
		time.sleep(2)
	endTest(driver,counter)

def endTest(driver, counter):
	input('press any button to close')
	print('Calls made: ', counter)
	driver.quit()
	driver.close()

initialize()





