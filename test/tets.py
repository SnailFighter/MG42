import requests
import logging


print('hello world')

resp = requests.get("https://pub.alimama.com/")

logging.info("test -----------------------")


print(requests.get('https://wx.qq.com/'))
