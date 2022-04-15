"""
	Browser args used to setup playwright browser
"""

from playwright.sync_api import sync_playwright, TimeoutError
from .configs import configs


def browsersetup(p):
	headless = True if configs["HEADLESS"] == "true" else False

	args = [
		'--deny-permission-prompts',
		'--no-default-browser-check',
		'--no-first-run',
		'--deny-permission-prompts',
		'--disable-popup-blocking',
		'--ignore-certificate-errors',
		'--no-service-autorun',
		'--password-store=basic',
		'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
		'--window-size=1400,1000'
	]

	browser = p.chromium.launch_persistent_context(user_data_dir=configs["PROFILE_LOC"], headless=headless, executable_path=configs["CHROMEDRIVER_LOC"], args=args, no_viewport=True)
	return browser

