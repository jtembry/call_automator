# call_automator
Call automation for a WebRTC app

# Steps
1. Make sure your have downloaded 'Chromedriver.exe' -- https://chromedriver.chromium.org/downloads
2. (OSX) Move 'Chromedriver.exe' to your '/usr/bin' folder
3. (Windows) specify the path where you've saved 'Chromedriver.exe' -- https://chromedriver.chromium.org/getting-started
4. Clone the repo.
5. Navigate to folder and type Python3 call_automator. click enter
6. Select your environment, enter your credentials, and choose the number of calls to make.

# Flags
## --headless
Run in Headless Chrome
## --redux
Add the Redux devtools extension to your session (Will not work in headless.)
## --video
Make video calls. Default behavior is audio calls
