"""
Main configs of the program:
Later addition:
	 - Proxy support
"""

import datetime 

configs = {
	"EMAIL":"",
	"PASSWORD":""
	"TO_RECEIVER":"",	
	"SUBJECT": f"Mail - {str(datetime.datetime.now())}",
	"PROFILE_LOC" : "/home/binit/.config/google-chrome/Profile 70",
	"SS_LOC" : "/home/binit/driver",
	"CHROMEDRIVER_LOC" : "/home/binit/driver/chrome-linux/chrome",	
	"HEADLESS" : "false",
}
