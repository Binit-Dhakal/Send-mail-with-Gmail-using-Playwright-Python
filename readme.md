# Send Mail with Gmail using Playwright-Python
This script logins to the Google account using your credentials info from configs.py and send the mail.  

# Demo 


## Installation required
- Install all the library we will need
```bash
pip3 install -r requirements.txt
```
- We also have to run
```bash
playwright installverificatio
```
to install browser bundle and everything for playwright. More [detail](https://playwright.dev/python/docs/intro)

## Change configs
Change the configs key to use thin mailer/configs.json. All the keys there are self-explanatory.  

## Run script
```bash
python3 run.py
```

## Note:
Please disable two factor authentication or if you dont want to disable it, input verification code within 30 seconds(the default timeout time in playwright). 
Also note that Google is notorious in making login difficult by showing (Setup recovery password page and many more after login page). I tried to make login smooth as possible 
but it may not work everytime because of the new pages google might throw. Please raise an issuse for page not handled by code with the url of the page and if possible, effective solution to tackle that.


## Future release plan
- [ ] Add support for proxy 

