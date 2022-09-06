import requests 
import time
token ="1612896303:AAGPhZpdMDuiVSZG5XloXZT13j8FjqiDkmI" 
while True:
   print(time.time())
   get= requests.get("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(token,960317749,str(time.time())))
   time.sleep(2)
