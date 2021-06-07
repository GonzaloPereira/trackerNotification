import time 
import requests
from bs4 import BeautifulSoup
from plyer import notification

prevData = None

while True:

  page = requests.get("https://postnl.post/details/",{'barcodes':['RU744342303NL']})
  soup = BeautifulSoup(page.content, 'html.parser')
  data = soup.select('.first.detail td')
  if prevData != data:
    notification.notify(
      title = "Yo-yo tracking status has changed",
      message = data[1].get_text(),
      timeout = 10*60*60
    )
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  print(current_time, data[1].get_text(), sep="  ")
  prevData = data
  time.sleep(10*60)
