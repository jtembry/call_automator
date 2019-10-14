# call_automator
Call automation for a WebRTC app

# Steps
1. Make sure your have downloaded 'Chromedriver.exe' -- https://chromedriver.chromium.org/downloads
2. (OSX) Move 'Chromedriver.exe' to your '/usr/bin' folder
3. (Windows) specify the path where you've saved 'Chromedriver.exe' in the code -- https://chromedriver.chromium.org/getting-started
4. Navigate to folder using terminal (cmd prompt on Windows) and type 'python3 call_automator.' click enter
5. You will be prompted to select your environment, enter your credentials, and choose the number of calls to make.

# Flags
add these to the end of your 'python3 call_automator --example' command to specify different runtime options.
## --headless
Run in Headless Chrome
## --redux
Add the Redux devtools extension to your session (Will not work in headless.)
## --video
Make video calls. Default behavior is audio calls
