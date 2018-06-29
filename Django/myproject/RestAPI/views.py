# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import sys
#sys.path.append('/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/')
from RestAPI.models import MySQL_model as md
from RestAPI.models import ftidf
from RestAPI.models import jieba
from RestAPI.models import word2vec
import json
import operator
from collections import OrderedDict

###### show view ######

def hello_world2(request):
    template = 'hello_world.html'
    responds = {'stringData': str(datetime.now()),}
    return render(request,template,responds )




@csrf_exempt 
def ftidf_source(request):
    data = ftidf.source()
    resp = HttpResponse(json.dumps(data))
    resp['Access-Control-Allow-Origin'] = '*'
    
    return resp 

@csrf_exempt 
def ftidf_value(request):
    data = ftidf.value("完整")
    resp = HttpResponse(data)
    resp['Access-Control-Allow-Origin'] = '*'
    
    return resp 


@csrf_exempt 
def jieba_cut(request):
    data=""
    sentence = "做到一般大型空氣清淨機都做不到的事！來自日本研發會的負離子核心技術，根除臭味，消滅霉菌，空氣淨化，最厲害的是耗材不用更換濾網！！！"

    if 's' in request.GET:
        sentence = request.GET['s']
    sentencearray = jieba.cut(sentence)
    for i in sentencearray:
        data+=i
        data+=","
    resp = HttpResponse(data)
    resp['Access-Control-Allow-Origin'] = '*'
    
    return resp 


@csrf_exempt 
def textrank(request):#cut_textrank
    sentence = "做到一般大型空氣清淨機都做不到的事！來自日本研發會的負離子核心技術，根除臭味，消滅霉菌，空氣淨化，最厲害的是耗材不用更換濾網！！！"

    if 's' in request.GET:
        sentence = request.GET['s']
    sentencearray = jieba.cut(sentence)
    re_dict={}


    for i in sentencearray:
        re_dict[str(i)] = ftidf.value(str(i))
    re_dict_str = json.dumps(re_dict, ensure_ascii=False).encode('utf8')
    

    b = json.dumps(sorted(re_dict.items(), key=operator.itemgetter(1)), ensure_ascii=False).encode('utf8')
    
    resp = HttpResponse(b)
    resp['Access-Control-Allow-Origin'] = '*'
    
    return resp 


@csrf_exempt 
def similarly_sentence(request):#similarly_sentence
    topic="基改,基因,基因改良,食品"
    sentence = "做到一般大型空氣清淨機都做不到的事！來自日本研發會的負離子核心技術，根除臭味，消滅霉菌，空氣淨化，最厲害的是耗材不用更換濾網！！！"

    if 's' in request.GET:
        sentence = request.GET['s']
    if 't' in request.GET:
        topic = request.GET['t']
    sentencearray = jieba.cut(sentence)
    topic_source = jieba.cut(topic)
    re_dict={}
    topic=[]
    for i in topic_source:
        if ftidf.value(str(i))>2:
            topic.append(i)
    
    for i in sentencearray:
        re_dict[str(i)] = ftidf.value(str(i))
    re_dict_str = json.dumps(re_dict, ensure_ascii=False).encode('utf8')
    
    b=[]
    for key, value in re_dict.items():
        if value>0:
            b.append([key,value])
    data = {} 
    data['similar']=[]
    data['different']=[]
    for i in b:
        for t in topic:
            value = word2vec.diff2word(t,i[0])
            if value<4:
                data['similar'].append({"topic":t,"subcontent":i[0],"similar":value})
            else:
                data['different'].append({"topic":t,"subcontent":i[0],"similar":value})
    resp = HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf8'))
    resp['Access-Control-Allow-Origin'] = '*'
    
    return resp