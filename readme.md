# Send Mail with Gmail using Playwright-Python
This script logins to the Google account and send the mail.

# Demo 
![](assets/sendmail.mp4)

## Motivation
I was trying to use Gmail api to send email for one of my project and was having hard time working with it, So I made this just for fun.

## Installation required
- Install all the library we will need
```bash
pip3 install -r requirements.txt
```
- We also have to run
```bash
playwright install
```
to install browser bundle and everything for playwright. More [detail](https://playwright.dev/python/docs/intro)

## Change configs
Change the configs key in mailer/configs.json. All the keys there are self-explanatory.  

## Run script
```bash
python3 run.py
```


## Future release plan
- [ ] Add support for proxy 

