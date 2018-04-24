#!usr/bin/env python3
#coding:utf-8

import urllib.request
import json
from time import sleep
url='https://swapi.co/api/films/'
films=[]
for i in range(1,8):
	films.append(url+str(i)+'/')

headers={}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fw=open('../csv_files/films.txt','w')

for item in films:
	print(item)
	request=urllib.request.Request(url=item,headers=headers)
	response=urllib.request.urlopen(request,timeout=20)
	result=response.read()
	result=result.decode('utf-8')
	fw.write(result+'\n')
	sleep(0.5)
fw.close()