# -*- coding:utf-8 -*-
import os,sys,io
#sys.path.append('/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/jieba_zn')

import logging as log
log.basicConfig(format='\n%(levelname)s:%(message)s',level=log.INFO)


import json 

tfidf_ditc = {}

with io.open("/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/ftidf_data.txt","r",encoding='utf-8') as f:
    tfidf_ditc = json.loads(f.read())
    log.info(tfidf_ditc)


def value(word):
	if word in tfidf_ditc:
		if len(word)<2:
			a = tfidf_ditc[word]-5
		else:
			a = tfidf_ditc[word]

	else:
		a = 3
	return a

def source():
	return tfidf_ditc