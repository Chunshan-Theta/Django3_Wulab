# -*- coding:utf-8 -*-
import os,sys,io
#sys.path.append('/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/jieba_zn')

from RestAPI.models.jieba_zn import jieba
import logging as log
jieba.setLogLevel(60)
log.basicConfig(format='\n%(levelname)s:%(message)s',level=log.INFO)

def cut(sentence):
	a = jieba.lcut(sentence,cut_all=False)
	return a