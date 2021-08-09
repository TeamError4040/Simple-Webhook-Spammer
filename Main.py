import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("Webhook spam")
print(banner)
msg = input("Spam Message: ")
webhook = input("WebHook URL: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
lol = 1
while lol == 1:
    spam(msg, webhook)
