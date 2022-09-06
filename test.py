import requests 
import time
token ="1612896303:AAGPhZpdMDuiVSZG5XloXZT13j8FjqiDkmI" 
while True:
   t=time.strftime("%I:%M:%S")
   print(t)
   get= requests.get("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(token,960317749,t))
   time.sleep(60)
