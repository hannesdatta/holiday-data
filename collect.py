# -*- coding: utf-8 -*-

import holidayapi
import json
import time

# createa file w/ your API key

key = open('keys.txt','r').read()

hapi = holidayapi.v1(key)

countries = ['AU','CN','HK','IN','ID','JP','MY','NZ','PH','SG','KR','TH','TW','VN']


years = range(2004,2014+1)


parameters = {
    # Required
    'country': 'US',
    'year':    2016,
    # Optional
    # 'month':    7,
    # 'day':      4,
    # 'previous': True,
    # 'upcoming': True,
    # 'public':   True,
    # 'pretty':   True,
}

country = countries[0]
year=years[0]


f = open('holidays_gfkproject.json', 'w',encoding = 'utf-8')

for c in countries:
    for y in years:
        print(c + ': ', str(y))
        holidays = hapi.holidays({'country': c, 'year': y})
        f.write(json.dumps(holidays)+'\n')
    time.sleep(2)

f.close()