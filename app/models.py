from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     email_token = models.CharField(max_length=200)
#     is_verified = models.BooleanField(default=False)

class Admin_log1(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=10)

class Doctor_log1(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=10)
    
class Announcement_md1(models.Model):
    Firstname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)   
    Announce = models.CharField(max_length=50)
    Date = models.DateField() 

    def __str__(self) -> str:
        return self.Firstname

class Pateintlogin1(models.Model):
    Email = models.EmailField(max_length=50)
    Otp = models.CharField(max_length=30)
    is_varified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.Email


class Patientdata1(models.Model):
    Firstname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=10)
    Date = models.DateField()

    def __str__(self) -> str:
        return self.Firstname

class Bookdata1(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    visit = models.CharField(max_length=50)
    adate = models.DateField()
    atime = models.TimeField()

    def __str__(self) -> str:
        return self.name

class Paymentdata1(models.Model):
    Name = models.CharField(max_length=50)
    Cvv = models.IntegerField(max_length=3)
    Card = models.IntegerField(max_length=10)
    Email = models.EmailField(max_length=50)
    Otp = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.Name
    
class Prescriptiondata1(models.Model):
    Name = models.CharField(max_length=50)
    Medicine = models.CharField(max_length=50)
    Date = models.DateField()

    def __str__(self) -> str:
        return self.Name