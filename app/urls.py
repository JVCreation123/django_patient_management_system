from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path("",views.Home,name="Home"),
    path("home/",views.HomePage,name="HomePage"),
    path("register/",views.RegisterPage,name="RegisterPage"),
    path("emailotp/",views.Otpdata,name="Otpdata"),
    path("add/emailot/",views.Otpdata2,name="otpdata"),

    path("thankyou/",views.Thankyou,name="Thankyou"),
    path("memberdata/",views.Memberdata,name="Memberdata"),
    path("add/member/",views.Memberdata2,name="member1"),

    path("appointmentdata/",views.Appointmentdata,name="Appointmentdata"),
    path("add/appoint/",views.Appointmentdata2,name="appoint1"),

    path("paymentdata/",views.Paymentdata3,name="Paymentdata3"),
    path("add/pay/",views.Paymentdata4,name="pay1"),

    path("prescription/",views.Prescription,name="Prescription"),
    path("drr/presc/",views.Prescriptiondata2,name="presc1"),


    path("reg/",views.regdata,name="reg"),
    
    path("otpp/",views.OtpPage,name="OtpPage"),
    path("otp1/",views.otppp,name="otp1"),
    path("otp1/u_login/",views.R1,name="otp2"),





    path("contact_us1/",views.contact_us,name="contact_us1"),

    # path("otpp/",views.verify_otp,name="otpp"),


    path("dr_login/",views.Dr_Login,name="Dr_Login"),
    path("drr/",views.Logindoctor,name="Logindoctor"),

    path("index/",views.Home,name="Home"),
    path("index/Dr_editpage/",views.Announcement_info,name="Announcement_info"),
    path("indexdd/",views.indexdata,name="indexdd"),



    path("ad_login/",views.Admin_Login,name="Admin_Login"),
    path("add/",views.Loginadmin,name="Loginadmin"),
    

    path("index/",views.Home,name="Home"),
    path("index/Ad_editpage/",views.Ad_Announcement_info,name="Ad_Announcement_info"),
    path("indexdd/",views.Ad_indexdata,name="indexdd"),

    # path("Em_otp/",views.Em_otp,"Em_otp"),



    path("user_panel/",views.User_panel,name="User_panel"),

    path("pdfdownload/<int:pk>",views.Download,name="download"),
    
    path("user_panel/u_login/",views.User_login,name="User_login"),
    path("user_panel/book_app/",views.Book_appoint,name="Book_appoint"),

    path("book/",views.bookapk,name="book"),
    # path("user_panel/book/",views.BookSlot,name="BookSlot"),
    path("payment/",views.Payment, name="Payment"),

    path("Payotp/",views.Payform, name="Payform"),
    path("Payotp2/",views.Payotp2, name="Payotp2"),
    path("Payotp2/final/",views.Payotpp, name="payotp2"),

    


    # path("verify/",views.verify,name="verify"),
    # path("verify/",views.verify,name="verify"),
    # path("error/",views.error_page,name="error"),


    path("insert/",views.InsertData,name="insert"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),
    path("delete2/<int:pk>",views.DeleteData2,name="delete2"),
    path("delete3/<int:pk>",views.DeleteData3,name="delete3"),
    path("delete4/<int:pk>",views.DeleteData4,name="delete4"),
    path("delete5/<int:pk>",views.DeleteData5,name="delete5"),
    path("delete6/<int:pk>",views.DeleteData6,name="delete6"),
    # path("delete7/<int:pk>",views.DeleteData7,name="delete7"),







    # path("u_login/user_panel/",views.User_panel,name="User_panel"),

    # path('delete/<int:Id>', views.delete, name='delete'),
    # path("user_panel/",views.InsertData,name="user_panel"),



    # path("",views.DoctorLogin,name="doctorlogin"),
]
