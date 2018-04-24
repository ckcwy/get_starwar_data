#!usr/bin/env python3
#coding:utf-8

import urllib.request
import json
import time

headers={}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

species=[]
url= 'https://swapi.co/api/species/'
for i in range(1,40):
	species.append(url+str(i)+'/')
fw=open('../csv_files/getspecies.csv','w')
s1=time.time()
for item in species:
	print(item)
	try:
		request=urllib.request.Request(url=item,headers=headers)
		response=urllib.request.urlopen(request,timeout=30)
		result=response.read()
		result=result.decode('utf-8')
		print(result)
	except Exception as e:
		print(e)
	else:
		fw.write(result+'\n')
	finally:
		print('continue getting data')

s2=time.time()
print('it  has used %ss. '%(s2-s1))


fw.close()