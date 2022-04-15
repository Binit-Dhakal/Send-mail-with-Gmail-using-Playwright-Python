"""
Contains logic for starting the playwright browser 
"""

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import datetime 

from .browser_setup import browsersetup
from .mailer import mailer 
from .configs import configs

def start(body):
	with sync_playwright() as p:
		flag = True
		try:
			browser = browsersetup(p) 
			page = browser.new_page() 
			stealth_sync(page)
		except Exception as e:
			print("Browser setup error", e.name)
			flag = False

		if flag == True:
			try:
				mailer(page, browser,body)
			except Exception as err:
				page.screenshot(
					path=f"{configs['SS_LOC']}/{datetime.datetime.now().strftime('%m-%d@%H-%M')}.png")
									
				try:
					print(err.message.replace("=", "").replace("\n", "").split("logs")[0])
				except:
					print(err)
		browser.close()
	

