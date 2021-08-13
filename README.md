SRP irrigation schedule checker

This app will check the SRP irrigation schedule and return the posted irrigation start time.

*Ver1 - SRP_Check.py
You will need to input your SRP account# in the code(replace the x's) before running and also the path address to your downloaded chromedriver(add path addres before \chromedriver.exe).
*Make sure to download the chromedriver version that matches your current browser version.  Version can be seen in 'About' menu in browser.

*Ver2 - SRPcheck_GUI.py
Now editing code with account number and chromium path is no longer needed.  Complete proccess to check SRP irrigation schedule can be done via graphical user interface.  Just run the python code, fill in the blanks and hit the "Get schedule" button. 

Chromedriver downloads URL:
https://sites.google.com/a/chromium.org/chromedriver/downloads


*Ver1.1 Update 09Aug21, added options for Selenium webdriver to run headless so that browser does not need to load visually.

*Ver2.0 Update 12Aug21, created GUI for SRP irrigation schedule checker.  Now just input SRP account number into first input box and set path to chromium driver using file explorer with PATH button or paste the complete PATH into the second input box.

Requirements:
chromedriver(download URL listed above)

Libraries:
Selenium
logging
*V2(additional libraries)
tkinter