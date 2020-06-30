# -*- coding: utf-8 -*-

import json

file = open('holidays_gfkproject.json', 'r', encoding = 'utf-8').readlines()
output = 'holidays_gfkproject.csv'

fields = ['country','date','public','name']

g=open(output, 'w', encoding = 'utf-8')

cnt=0
for f in fields:
    cnt+=1
    sep = '\t'
    if (cnt==len(fields)): sep ='\n'
    g.write(f+sep)

    
for i in file:
    obj = json.loads(i.replace('\n',''))
    for h in obj.get('holidays'):
        cnt=0
        for f in fields:
            cnt+=1
            sep = '\t'
            if (cnt==len(fields)): sep ='\n'
            g.write(str(h.get(f))+sep)
g.close()