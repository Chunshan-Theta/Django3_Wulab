# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import sys
from django.http import HttpResponseRedirect
#sys.path.append('/home/gavin/Desktop/Django3server/Django/myproject/RestAPI/models/')
from phd_status.models import MySQL_model as md
import datetime
import json
import requests

###### show view ######

def hello_world3(request):

    return HttpResponseRedirect('./view/Login/')

def view_Login(request):
    template = 'Login.html'
    responds = {'stringData': str(datetime.datetime.now()),}
    return render(request,template,responds )

def view_adduser(request):
    template = 'adduser.html'
    responds = {'stringData': str(datetime.datetime.now()),}
    return render(request,template,responds )

def view_reviewRecords(request):
    md.connectDB()
    if not Ensureinput(request.GET,["Taccount"]) :
        
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
    else:
        stu_name =  str(request.GET['Taccount'])    



    sql = "SELECT `UserRecords`.`RecordType`,`UserRecords`.`status`,`UserRecords`.`deadlines`,`UserRecords`.`note`,`UserRecords`.`UpdateTime`,`UserRecords`.`Record_id` FROM `UserRecords`,`UserList` WHERE `UserRecords`.`user_id` = `UserList`.`user_id` AND `UserList`.`account` = '"+stu_name+"' ORDER BY `UserRecords`.`RecordType` ASC"
    datafromsql = md.exeSQl(sql)
    md.close()


    template = 'reviewRecord_admin.html'
    responds = {'UserRecords': datafromsql,"stu_name":stu_name}
    return render(request,template,responds )

def view_reviewUsers(request):

    md.connectDB()  



    sql = "SELECT * FROM `UserList` WHERE `StuentTypeId` != -1 ORDER BY `StuentTypeId` ASC"
    datafromsql = md.exeSQl(sql)
    md.close()
    

    template = 'reviewUsers.html'
    responds = {'UserRecords': datafromsql}
    return render(request,template,responds )

def view_edit_records(request):

    if not Ensureinput(request.GET,["Records_id","Records_type"]) :
       
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
        """
        Records_id = "3"
        Records_type = "托福成績"  
        """
    else:
        Records_id = request.GET["Records_id"]
        Records_type = request.GET["Records_type"]  


    

    
    template = 'edit_record.html'
    responds = {'Records_id': Records_id,"Records_type":Records_type}
    return render(request,template,responds )
    


def login(request):

    md.connectDB()
    
    if not Ensureinput(request.POST,["account","pws"]) :        
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)

    u_account = request.POST["account"]
    u_pws = request.POST["pws"]

    sql = "SELECT * FROM `UserList` WHERE `account` = '"+u_account+"' AND `passwords` = '"+u_pws+"' ORDER BY `StuentTypeId` ASC"
    datafromsql = md.exeSQl(sql)
    
    md.close()
    request.session['uid'] = 'bar'
    if datafromsql == []:
       return  HttpResponse('not found the user.') 
    else:
        u_id = datafromsql[0][0]
        u_typy = datafromsql[0][3]
        
        

        if u_typy !=-1:            
            return HttpResponseRedirect('../view/reviewRecords/?Taccount='+u_account)
        else:
            return HttpResponseRedirect('../view/reviewUsers/')
        
        return HttpResponse(datafromsql)
    #return  HttpResponse(request.session.get('uid')+request.session.get('uaccount')+request.session.get('utype'))
    #return  HttpResponseRedirect('../initUser/'+account+'/')



def add_user(request):

    md.connectDB()

    if not 'post_account' in request.POST or not 'post_pws' in request.POST or not 'post_studentname' in request.POST:
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
    elif str(request.POST['post_account']) == '' or str(request.POST['post_pws']) == '' or str(request.POST['post_studentname']) == '':
        re = "data of the POST requests are null. "
        return  HttpResponse(re)
    else:
        account = str(request.POST['post_account'])
        pws = str(request.POST['post_pws'])
        studentname= str(request.POST['post_studentname'])
    if not 'post_EnterYear' in request.POST:
        EnterYear = 'CURRENT_TIMESTAMP'
    else:
        EnterYear = str(request.POST['post_EnterYear'])
    sql = "INSERT INTO `UserList` (`user_id`, `account`, `passwords`, `StuentTypeId`, `UserName`, `EnterYear`) VALUES (NULL, '"+account+"', '"+pws+"', '1', '"+studentname+"', "+EnterYear+");"
    datafromsql = md.exeSQl(sql)
    md.close()
    return  HttpResponse(datafromsql)
    #return  HttpResponseRedirect('../initUser/'+account+'/')

    

def init_user(request):

    if not 'Taccount' in request.POST or request.POST["Taccount"]=="":
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
    else:
        account = request.POST["Taccount"]
        md.connectDB()
        datafromsql = md.exeSQl("SELECT `user_id`,`StuentTypeId` FROM `UserList` WHERE `account` = '"+account+"'")
        studentId = str(datafromsql[0][0])
        studenttypeId = str(datafromsql[0][1])
        datafromsql = md.exeSQl("SELECT `step` FROM `UserType` WHERE StuentTypeId = "+studenttypeId+" LIMIT 1")
        stepstring = json.loads(str(datafromsql[0][0]))

        for key,value in stepstring.items():
            #INSERT INTO `UserRecords` (`Record_id`, `user_id`, `RecordType`, `status`, `UpdateTime`, `note`, `deadlines`) VALUES (NULL, '1', '資格考(一)', '-1', CURRENT_TIMESTAMP, NULL, '1995-05-11');
            if not value == '-1':
                deadlines = (datetime.datetime.now() + datetime.timedelta(days=int(value))).strftime("%Y-%m-%d")
            else:
                deadlines = '1995-05-11'
            
            sql = "INSERT INTO `UserRecords` (`Record_id`, `user_id`, `RecordType`, `status`, `UpdateTime`, `note`, `deadlines`) VALUES (NULL, '"+studentId+"', '"+key+"', '-1', CURRENT_TIMESTAMP, NULL, '"+deadlines+"');"
            datafromsql = md.exeSQl(sql)
        
        md.close()


    #return  HttpResponseRedirect('./')
    return  HttpResponse(datafromsql)

def del_records(request):

    if not 'records_id' in request.POST or request.POST["records_id"]=="":
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
    else:
        records_id = request.POST["records_id"]
        md.connectDB()
        datafromsql = md.exeSQl("DELETE FROM `UserRecords` WHERE `UserRecords`.`Record_id` = '"+records_id+"';")      
        
        md.close()

        return  HttpResponse(datafromsql)

# UPDATE `UserRecords` SET `status` = '1',`note` = '安安',`deadlines`='2016-02-02' WHERE `UserRecords`.`Record_id` = 3
def edit_records(request):

    if not Ensureinput(request.POST,["records_id","status"]) :
        
        re = "data of the POST requests aren't complete. "
        return  HttpResponse(re)
        
    
    records_id = request.POST["records_id"]
    status = request.POST["status"]

    md.connectDB()

    updateData =""

    if not request.POST["note"] == "" and "note" in request.POST:
        note = request.POST["note"]
        updateData += ",`note` = '"+note+"'"

    if not request.POST["deadlines"] == "" and "deadlines" in request.POST:
        deadlines = request.POST["deadlines"]
        updateData += ",`deadlines`='"+deadlines+"'"

    
    datafromsql = md.exeSQl("UPDATE `UserRecords` SET `status` = '"+status+"'"+updateData+" WHERE `UserRecords`.`Record_id` = '"+records_id+"';")      
    
    md.close()

    return  HttpResponse(datafromsql)











#local function
def Ensureinput(InputData,InquiryList):
    result = 1

    for item in InquiryList:
        if not item in InputData or InputData[item]=="":
            result = 0




    return result