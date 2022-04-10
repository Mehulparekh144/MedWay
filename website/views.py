from datetime import date
from enum import unique
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests import request
# from httplib2 import Http
from website.models import detailform, regform , medical
import string
import random
import qrcode
  
# initializing size of string 

global id
global id_

def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return render(request,'index.html')


def login(request):
    # template = loader.get_template('login.html')
    # return HttpResponse(template.render())
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
  

        reg_email = regform.objects.filter(email=email).values()
        reg_pass = regform.objects.filter(password = password).values()


        if (len(reg_email) or len(reg_pass) != 0):
            global id
            id = regform.objects.filter(email=email).values()[0]['uniqueid']
            return render(request, 'details.html')

        else:
            return render(request,'register.html')        
    return render(request,'login.html')



def register(request):
    if (request.method == 'POST'):
        # print('we are using post ')
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        N = 7
  
 
        userid = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
  

        result = regform(name=name, email=email, password=password, phone=phone,uniqueid=userid)
        result.save()
        
    
    return render(request, 'register.html')

def details(request):
    if (request.method == 'POST'):
        age = request.POST['age']
        height = request.POST['height']
        weight = request.POST['weight']
        blood = request.POST['blood']
        pin = request.POST['pin']
        sex = request.POST['sex']
        id_qr = id
        dname = request.POST['dname']
        datetime= request.POST['datetime']
        visit = request.POST['visit']
        medications = request.POST['medications']
        print(dname,datetime,visit,medications)

        result = detailform(age=age,height=height,weight=weight,blood=blood,pin=pin,sex=sex,uniqueid=id_qr)
        result.save()

        medical_result = medical(dname=dname,datetime=datetime,visit=visit,medications=medications,uniqueid=id_qr)
        medical_result.save()

    return account(request)

def account(request):
    reg = regform.objects.filter(uniqueid = id).values()[0]
    details = detailform.objects.filter(uniqueid = id).values()[0]   

    my_dict = {}
    my_dict['id'] = id
    my_dict['name'] = reg['name']
    my_dict['age'] = details['age']
    my_dict['blood_group']= details['blood']
    my_dict['sex'] = details['sex']
    qr_generator(id)
    my_dict['path'] = "/img/qr" + f"{id}" + ".png"
    return render(request,'view.html',my_dict)

def  view(request,given_id):
    global id_
    id_ = request.GET.get("given_id")
    print(id_)

    return render(request,'pin.html')
    # return pin(request)

def pin(request):
    pin_ = request.POST['pin']
    details = detailform.objects.filter(pin = pin_).values()
    id_ = details[0]['uniqueid']
    if(len(details) == 0 ):
        render(request,'pin.html')
    else:
        print(id_)
        med = medical.objects.filter(uniqueid = id_).values()
        reg = regform.objects.filter(uniqueid = id_ ).values() 
        # det = detailform.objects.filter(uniqueid = id_).values()

        print(details)
        print(reg)
        print(med)

        new_dict = {}
        new_dict['detail'] = details[0]
        new_dict['user'] = reg[0]
        i = 1
        for val in med:
            m = "med" + str(i)
            new_dict[m] = val
            i += 1
        print(new_dict)

        return render(request,'fetch.html' ,new_dict)  

def adddetails(request):
    if (request.method == 'POST'):
        id_qr = id
        dname = request.POST['dname']
        datetime= request.POST['datetime']
        visit = request.POST['visit']
        medications = request.POST['medications']
        print(dname,datetime,visit,medications)

        medical_result = medical(dname=dname,datetime=datetime,visit=visit,medications=medications,uniqueid=id_qr)
        medical_result.save()

    return account(request)


def add(request):
    return render(request,'add.html')


def qr_generator(id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(f"localhost:8000/view?id={id}")

    qr.make(fit=True)
    img = qr.make_image(fill_color="BLUE", back_color="white")
    img.save("static/img/qr" + f"{id}" + ".png")
