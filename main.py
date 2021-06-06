import datetime
import time 
import requests
from bs4 import BeautifulSoup
import pandas as pd
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
  prevData = data
  time.sleep(10*60)
