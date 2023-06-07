from django import forms
from .models import Pateintlogin

class NameForm(forms.Form):
    yourmail = forms.CharField(label='Email',max_length=100)
    def clean(self):
        cleaned_data = super(NameForm,self).clean()
        yourmail = cleaned_data.get("yourmail")
        otp = cleaned_data.get("otp")
        p=Pateintlogin.objects.all()
        if yourmail:
                    for i in p:
                        if i.Email not in yourmail:
                            raise forms.ValidationError("user not exist.")
                        # elif i.Otp not in otp:
                        #     raise forms.ValidationError("user not exist.")

