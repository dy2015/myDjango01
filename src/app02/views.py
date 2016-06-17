
#coding:utf-8
from django.shortcuts import render_to_response
from django import forms
from models import User
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField()    
    password=forms.CharField(widget=forms.PasswordInput)    

def regist(req):
    tag=True 
    if req.method == 'POST':
        form=UserForm(req.POST,req.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create(username=username,password=password)
            tag=False 
            return render_to_response('register.html', {'title':'表单','tag':tag})
        
    else:
        form=UserForm()
    return render_to_response('register.html', {'title':'表单','form':form,'tag':tag})



