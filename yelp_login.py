# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:12:23 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

s= requests.session()
resp = s.get("https://www.yelp.com/login")
soup = BeautifulSoup(resp.text, 'html5lib')
csrf = soup.find('form', id = 'ajax-login').find('input', 'csrftok')['value']
print(csrf)

form_data = {
    'email' : 'dennis.dlin2@gmail.com',
    'password' : 'XXXXXXXX',
    'csrftok' : csrf
    }

resp = s.post("https://www.yelp.com/login", data = form_data)
print(resp.text)
#print('The Front Porch' in resp.text)
