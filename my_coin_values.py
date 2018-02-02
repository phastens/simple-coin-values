# -*- coding: utf-8 -*-
#!/usr/bin/python

import urllib2
import json
from tabulate import tabulate
from termcolor import colored

# Add currency name from coinmarketcap URL
list_curr = ["bitcoin"]

# Add the ammount of coin you have as "bitcoin":3.86
dict_amount = {"bitcoin":1}

# Put at what price you bought it "bitcoin":765
dict_buying_prices = {"bitcoin":100}


dict_prices = {}
dict_percent = {}
dict_percent_d = {}
dict_percent_w = {}
total = 0
total_earned = 0
final_list = []
headers = ["Name", "Price", "Percent 1h", "Percent 1d", "Percent 1w", "Quantity", "Value", "\x1b[0mEarned\x1b[0m"]
def colorT(number):
    if float(number) < 0:
        return "red"
    else:
        return "green"

for currencie in list_curr:
    url = 'https://api.coinmarketcap.com/v1/ticker/' + currencie + '/?convert=EUR'
    response_json = urllib2.urlopen(url)
    data = json.loads(response_json.read())
    value = data[0]['price_usd']
    percent_h = data[0]['percent_change_1h']
    percent_d = data[0]['percent_change_24h']
    percent_w = data[0]['percent_change_7d']
    dict_prices[currencie] = value
    dict_percent[currencie] = percent_h
    dict_percent_d[currencie] = percent_d
    dict_percent_w[currencie] = percent_w
    try:
        value = float(dict_prices[currencie]) * float(dict_amount[currencie])
        plus_value = value - (float(dict_amount[currencie]) * float(dict_buying_prices[currencie]))
    except ValueError:
        value = 0
        plus_value = 0
    color = colorT(plus_value)
    color_percent_h = colorT(percent_h)
    color_percent_d = colorT(percent_d)
    color_percent_w = colorT(percent_w)
    final_list.append([currencie,
                      dict_prices[currencie],
                      colored(dict_percent[currencie], color_percent_h),
                      colored(dict_percent_d[currencie], color_percent_d),
                      colored(dict_percent_w[currencie], color_percent_w),
                      dict_amount[currencie],
                      round(value,1),
                      colored(round(plus_value,1), color)])
    total += value
    total_earned += plus_value
color = colorT(total_earned)
final_list.append([''])
final_list.append(['TOTAL', colored(str(int(total)), 'green')])
final_list.append(['EARNED', colored(str(int(total_earned)), color)])
print tabulate(final_list, headers=headers, tablefmt="simple", numalign="right")
