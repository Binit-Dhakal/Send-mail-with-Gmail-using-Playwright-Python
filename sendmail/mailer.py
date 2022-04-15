"""
	Contains main mailer logic of :
	- Login to google account
	- Checking if account has been blocked or requires two factor authentication
	- send mail
"""

from playwright.sync_api import sync_playwright, TimeoutError
import datetime
import json
from .configs import configs


def check_for_hindrance(page):
	if "signinoptions/recovery-options-collection" in page.url:
		print("Requires recovery password setup")
	elif "signin/v2/disabled/explanation?" in page.url:
		print("Account is blocked")
	elif "?v=lui" in page.url:  # ask for first time if we want to use html gmail
		page.click("//input[@type='submit']")
	elif "/signin/v2/challenge" in page.url:
		print("Two step verification needed")


def login(page, browser):
	page.goto("https://mail.google.com/mail/u/0/h/", timeout=60000)

	# if already logged in -> checking block url
	check_for_hindrance(page)

	if "https://mail.google.com/mail/u/0/h/" not in page.url:
		if page.url == "https://www.google.com/intl/ne/gmail/about/#":
			cookies = browser.cookies()
			cookie_without = [
				cookie for cookie in cookies if 'google' not in cookie['domain']]
			browser.clear_cookies()
			browser.add_cookies(cookie_without)    
			page.goto("https://mail.google.com/mail/u/0/h/")

		# username
		page.fill("//input[@name='identifier']", configs["EMAIL"])
		page.click("//button[@jsname='LgbsSe']")

		# for checking username or password credentials error
		def credcheck(xpath, who):
			try:
				err = page.wait_for_selector(
					"//div[@aria-live='assertive']/div/span", timeout=20 * 100)
				# print("Wrong username credentials", )
				raise Exception(f"Wrong {who} cred :: " + page.evaluate(f"""document.evaluate(
					"{xpath}", document, null, XPathResult.STRING_TYPE).stringValue;"""))

			except TimeoutError:  # no error found
				pass

			except Exception as e:
				raise Exception(e)

		credcheck("//div[@aria-live='assertive']/div", "email")
		url_1 = page.url
		# password
		page.fill("//input[@name='password']", configs["PASSWORD"])
		
		with page.expect_navigation():
			page.click("//button[@jsname='LgbsSe']")
			credcheck("//div[@aria-live='assertive']/div/span", "password")

		check_for_hindrance(page)
			
def send_mail(page,body):
	page.click("//a[@accesskey='c']")
	page.fill("//textarea[@id='to']", configs["TO_RECEIVER"])
	page.fill("//input[@name='subject']", configs["SUBJECT"])
	page.fill("//textarea[@name='body']", body)

	page.click("//input[@name='nvp_bu_send']")
	try:
		page.locator(
			"//td[@bgcolor='#FAD163' and @role='alert']/b[text()='Your message has been sent.']").wait_for(timeout=5000)
		print("Mail Sent")
	except:  # message not sent
		print("mail not sent")
	return
    
def mailer(page,browser,body):
	login(page, browser)
	send_mail(page,body)
