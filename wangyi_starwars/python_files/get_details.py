#!usr/bin/env python3
#coding:utf-8

import urllib.request
import json
from time import sleep

headers={}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"


films=[]
fr=open('../csv_files/films.txt','r')
for line in fr:
	line=json.loads(line.strip('\n'))
	films.append(line)
fr.close()

#获取详细数据 characters planets starships vehicles species
targets=['characters','planets','starships','vehicles','species']
for target in targets:
	fw=open('../csv_files/'+target+'.csv','w')
	data=[]
	for item in films:
		tmp=item[target]
		for t in tmp:
			if t in data:
				continue
			else:
				data.append(t)

			while 1:
				print(t)

				try:
					request=urllib.request.Request(url=t,headers=headers)
					respones=urllib.request.urlopen(request,timeout=20)
					result=respones.read()
					result=result.decode('utf-8')
				except Exception as e:
					print(e)
				else:
					fw.write(result+'\n')
					break
				finally:
					pass
	print(len(data))
	fw.close()