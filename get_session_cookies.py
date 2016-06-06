#!/usr/bin/env python
# enjin-scraper
# Written in 2016 by David H. Wei <https://github.com/spikeh/>

# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any
# warranty.

# You should have received a copy of the CC0 Public Domain Dedication
# along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
import json
import pickle
from selenium import webdriver

with open('config.json', 'r') as f:
    config = json.load(f)

browser = webdriver.Firefox()
browser.get('http://essencesunstrider.enjin.com/login')

in_xp = "//div[contains(@class, 'input') and contains(@class, 'input-text')]"
inputs = browser.find_elements_by_xpath(in_xp)
username = inputs[0].find_element_by_tag_name('input')
password = inputs[1].find_element_by_tag_name('input')

username.send_keys(config['username'])
password.send_keys(config['password'])

sub_xp = ('//*[@id="section-main"]/div/div[3]/div[2]/div[8]/table/tbody/tr/td/'
          'div/div/div/div/table/tbody/tr/td[2]/form/div[5]/div/input')
submit = browser.find_element_by_xpath(sub_xp)
submit.click()

cookies = browser.get_cookies()
pickle.dump(cookies, open('essence.pkl', 'wb'))
browser.quit()