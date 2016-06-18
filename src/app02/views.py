
#coding:utf-8
from django.shortcuts import render_to_response
from django import forms
from models import User
from django.http.response import HttpResponseRedirect
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
            response=HttpResponseRedirect('../login/')
            response.delete_cookie('flag')
            response.set_cookie('flag', False, 3600)
            return response        
    else:
        form=UserForm()
    return render_to_response('register.html', {'title':'注册','form':form,'tag':tag})

def login(req):
    flag= req.COOKIES.get('flag','')
    if req.method == 'POST':
        form=UserForm(req.POST,req.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = User.objects.filter(username=username,password=password)
            if users:
                response=HttpResponseRedirect('../index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                response=HttpResponseRedirect('../login/')
                response.delete_cookie('flag')
                response.set_cookie('flag', True, 3600)
                return response
    else:
        form=UserForm()
    print 'flag='+flag
    if flag=='True':
        print 'here if'
        response=render_to_response('login.html', {'title':'登录','form':form,'flag':flag})
        response.delete_cookie('flag')
        response.set_cookie('flag', False, 3600)
        return response
    else:
        print 'here else'
        return render_to_response('login.html', {'title':'登录','form':form})
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('content.html', {'title':'主页','username':username})

