# -*- coding:utf-8 -*-
#!usr/bin/env python
import json
import io
with io.open("/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/word2vec.txt","r",encoding='utf-8') as f:
    Json_file = json.loads(f.read())
'''
print(d)
print(d[u'\u5c07\u4e4b\u652c'])
print(u'\u5c07\u4e4b\u652c')
'''
def location(text):
    uni_text=unicode(text,"utf-8")
    print(Json_file[uni_text])
    return Json_file[uni_text]
def diff(t1,t2):
    x = t1[0]-t2[0]
    y = t1[1]-t2[1]
    print(x,y,(x**2+y**2)**0.5)

def diff2word(t1,t2):
    uni_text_1=t1
    uni_text_2=t2
    try:
        uni_text_1_v=Json_file[uni_text_1]
        uni_text_2_v=Json_file[uni_text_2]
        x = uni_text_1_v[0]-uni_text_2_v[0]
        y = uni_text_1_v[1]-uni_text_2_v[1]
        data = (x**2+y**2)**0.5
        return data*10**8
    except KeyError:
        return 10
''' 
a =location("將之攬")
b =location("然後")
c =location("即使")
d =location("渾厚")
e =location("輕薄")

diff(a,b)
diff(c,b)
diff(d,e)
diff(d,a)
'''