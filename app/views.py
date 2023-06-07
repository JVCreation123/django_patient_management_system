from django.shortcuts import render
from django.http import HttpResponse,request
from django.shortcuts import redirect
from .models import *
import smtplib
import ssl
from email.message import EmailMessage
import random
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt


def Home(request):
   
    selectdata=Announcement_md1.objects.all()
    return render(request,"app/index.html",{'key3':selectdata})


def HomePage(request):
    return render(request,"app/home.html")
    

def RegisterPage(request):
    return render(request,"app/register.html")


def Otpdata(request):
    ddata3 = Pateintlogin1.objects.all() 
    return render(request,"app/emailotp.html",{'key3':ddata3})

def Otpdata2(request):
     return redirect('Otpdata')

def DeleteData3(request,pk):
    ddata2 = Pateintlogin1.objects.get(id=pk) 
    ddata2.delete()
    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')

def Memberdata(request):
    ddata4 = Patientdata1.objects.all() 
    return render(request,"app/memberdata.html",{'key4':ddata4})

def Memberdata2(request):
     return redirect('Memberdata')

def DeleteData4(request,pk):
    ddata2 = Patientdata1.objects.get(id=pk) 
    ddata2.delete()
    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')

def Appointmentdata(request):
    ddata5 = Bookdata1.objects.all() 
    return render(request,"app/appointmentdata.html",{'key5':ddata5})

def Appointmentdata2(request):
     return redirect('Appointmentdata')

def DeleteData5(request,pk):
    ddata2 = Bookdata1.objects.get(id=pk) 
    ddata2.delete()
    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')


def Paymentdata3(request):
    ddata6 = Paymentdata1.objects.all() 
    return render(request,"app/paymentdata.html",{'key6':ddata6})

def Paymentdata4(request):
     return redirect('Paymentdata3')

def DeleteData6(request,pk):
    ddata2 = Paymentdata1.objects.get(id=pk) 
    ddata2.delete()

    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')


def Prescription(request):
        return render(request,"app/prescription.html")


def Prescriptiondata2(request):
    if request.method=="POST":
        name = request.POST.get('name')
        medicine = request.POST.get('medicine')
        date = request.POST.get('date')

        user = Prescriptiondata1.objects.create(Name=name, Medicine = medicine, Date = date)
        return redirect('Prescription')
    


def regdata(request):
    if request.method == "POST":
        email_receiver=request.POST.get('email_receiver')
        otp=request.POST.get('otp')      
     
   
        otp = random.randrange(1111,9999)
        otp = str(otp)
      

        email_sender = 'jayrajsinhvaghela1108@gmail.com'
    
        email_password = 'mxrkvpcmewwygaak'
        email_receiver = email_receiver
        subject = "LOGIN OTP"
        body = """
        Welcome to Astha Clinic
        Your OTP is : """ + otp   #.format(otp)
        em = EmailMessage()
        em['from'] = email_sender
        em['to'] = email_receiver
        em['subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
        login1=Pateintlogin1(Email=email_receiver,Otp=otp)
        login1.save()
       

        return redirect('OtpPage')
    else:
        return HttpResponse('error')



def OtpPage(request):
    return render(request,"app/otpp.html")

def otppp(request):
    if request.method == "POST":
        otp=request.POST.get('otp') 


    user2 = Pateintlogin1.objects.filter(Otp=otp)
    
    if user2:
            return redirect('User_panel')
    else:
            messages.warning(request,'Enter Valid OTP')
            return render(request,"app/otpp.html")



def Admin_Login(request):
    return render(request,"app/ad_login.html")

def Loginadmin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        admin=Admin_log1.objects.create(Email=email,Password=password)
        ademail="jay@gmail.com"
        adpassword="Admin"

        
        if adpassword==password and ademail==email:
                all_data=Patientdata1.objects.all()
                return render(request,"app/Ad_editpage.html",{'key1':all_data})
                
        else:
                messages.warning(request,'Enter Valid Credential')
                return render(request,"app/ad_login.html")
        
def DeleteData2(request,pk):
    ddata2 = Patientdata1.objects.get(id=pk) , Prescriptiondata1.objects.get(id=pk)
   
    ddata2.delete()
    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')




def Ad_Announcement_info(request):
    return render(request,"app/Dr_editpage.html")

def Ad_indexdata(request):
    username = request.POST['username']
    email = request.POST['email']
    announce = request.POST['announce']
    date=request.POST['date']
    

    newuser = Announcement_md1.objects.create(Firstname = username, Email=email, Announce=announce, Date=date)
    # return redirect('Home')
    return redirect('../')    

            
               

def R1(request):
    return render(request,"app/u_login.html")


def Dr_Login(request):
    return render(request,"app/dr_login.html")

def Logindoctor(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        drln=Doctor_log1.objects.create(Email=email,Password=password)
    
        dremail="sunilpatelmbbs123@gmail.com"
        drpassword="Sunil@mbbs123"
        if dremail==email and drpassword==password:
            all_data=Patientdata1.objects.all()
            return render(request,"app/Dr_editpage.html",{'key1':all_data})
        else:
            messages.warning(request,'Invalid Login')
            return render(request,"app/dr_login.html")
    

def DeleteData2(request,pk):
    ddata2 = Patientdata1.objects.get(id=pk) 
    ddata2.delete()
    return HttpResponse('<h1>Deleted Successfull.......!!!!!!</h1>')



def Announcement_info(request):
    return render(request,"app/Dr_editpage.html")

def indexdata(request):
    username = request.POST['username']
    email = request.POST['email']
    announce = request.POST['announce']
    date=request.POST['date']
   

    newuser = Announcement_md1.objects.create(Firstname = username, Email=email, Announce=announce, Date=date)
    # return redirect('Home')
    return redirect('../')    





def User_panel(request):
    all_data=Patientdata1.objects.all()
    return render(request,"app/user_panel.html",{'key1':all_data})

    
def User_login(request):
    return render(request,"app/u_login.html")

def InsertData(request):
    username = request.POST['username']
    email = request.POST['email']
    flexRadioDefault = request.POST['flexRadioDefault']
    date=request.POST['date']

    newuser = Patientdata1.objects.create(Firstname = username, Email=email, Gender=flexRadioDefault, Date=date)
    return redirect('User_panel')

    
def EditPage(request,pk):
    get_data = Patientdata1.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata = Patientdata1.objects.get(id=pk)
    udata.Firstname = request.POST['username']
    udata.Email = request.POST['email']
    udata.Gender = request.POST['flexRadioDefault']
    udata.Date = request.POST['date']


    udata.save()
    return redirect('User_panel')

def DeleteData(request,pk):
    ddata = Patientdata1.objects.get(id=pk) 
    ddata.delete()
    return redirect('User_panel')

def Download(request,pk):
        current_user = request.user
        user_id=current_user.id
        alldata = Prescriptiondata1.objects.get(id=pk)
        return render(request,"app/pdfdownload.html",{'key8':alldata})


def Book_appoint(request):
    return render(request,"app/book_app.html")



def bookapk(request):
    if request.method == "POST":
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        visit=request.POST.get('visit')
        adate=request.POST.get('adate')
        atime=request.POST.get('atime')

        contact=Bookdata1(name=name,gender=gender,dob=dob,visit=visit,adate=adate,atime=atime)
        contact.save();       

        return render(request, "app/payment.html")

    

def Payment(request):
    return render(request, "app/payment.html")

     
def Payform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        cvv = request.POST.get('cvv')
        cardno = request.POST.get('cardno')
        email_receiver = request.POST.get('email_receiver')
        otp = request.POST.get('otp')


        otp = random.randrange(1111,9999)
        otp = str(otp)


        email_sender = 'dhrumilparekh1273@gmail.com'
    
        email_password = 'spoldfcfzqqoevus'
        email_receiver = email_receiver
        subject = "PAYMENT OTP"
        body = """
        Welcome to Astha Clinic
        Your OTP is : """ + otp  +"""\nDo not share it with anyone!!"""  #.format(otp)
        em = EmailMessage()
        em['from'] = email_sender
        em['to'] = email_receiver
        em['subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

        data = Paymentdata1(Name = name , Cvv = cvv , Card = cardno,Email = email_receiver,Otp = otp)
        data.save()
        return redirect('Payotp2')
    else:
        return HttpResponse('Error')
        


def Payotp2(request):
    return render(request,"app/Payotp.html")

def Payotpp(request):
    if request.method == "POST":
        otp=request.POST.get('otp') 


    user2 = Paymentdata1.objects.filter(Otp=otp)
    
    if user2:
            last_added_form = Bookdata1.objects.latest('id')

            return render(request,"app/final.html",{'last_added_form': last_added_form})
    
    else:
            messages.warning(request,'Enter Valid OTP')
            return render(request,"app/Payotp.html")




@csrf_exempt
def success(request):
    return render(request, "index.html")

def contact_us(request):
 

            if request.method == 'POST' :
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')

            # for i in range(1,2):
                email_sender = 'jayrajsinhvaghela1108@gmail.com'

                email_password = 'mxrkvpcmewwygaak'
                email_receiver = "jayrajsinhvaghela446@gmail.com"
                subject1 = "CONTAC SUBMIT DETAILS"

                body = """
                Welcome- Admin - to ASTHA CLINIC\n\nName: """ + name + """\nEmail: """ + email + """\nSubject: """+subject+"""\nMessage: """ + message 
                em = EmailMessage()
                em['from'] = email_sender
                em['to'] = email_receiver
                em['subject'] = subject1
                em.set_content(body)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())
                    
                    return redirect('Thankyou')

def Thankyou(request):
     return render(request,"app/thankyou.html")    