import json
import time
import random
import pandas as pd
from datetime
import datetime

def generate_date_list(begin_date, end_date):
  date_list = [datetime.strftime(x, '%m-%d') for x in list(pd.date_range(start = begin_date, end = end_date))]
return date_list

second = random.randint(0, 59)

date_list = generate_date_list('20180101', '20181231')

event_list = [{
  'begin_date': '01-01',
  'end_date': '01-01',
  'detail': '元旦节'
}, {
  'begin_date': '02-15',
  'end_date': '02-21',
  'detail': '春节'
}, {
  'begin_date': '04-05',
  'end_date': '04-07',
  'detail': '清明节'
}, {
  'begin_date': '04-29',
  'end_date': '05-01',
  'detail': '劳动节'
}, {
  'begin_date': '06-16',
  'end_date': '06-18',
  'detail': '端午节'
}, {
  'begin_date': '09-22',
  'end_date': '09-24',
  'detail': '中秋节'
}, {
  'begin_date': '10-01',
  'end_date': '10-07',
  'detail': '国庆节'
}, ]

pv_list = []

# 遍历日期数组， 并随机生成一个 PV 值
for day in date_list:
  pv = random.randint(1, 100000)
dct = {
  'date': day,
  'pv': pv
}
pv_list.append(dct)

# print(pv_list)

f = open('info.json', 'w')
f.write(json.dumps({
  "2018": {
    "pv_list": pv_list,
    "event_list": event_list
  }
}))
f.close()