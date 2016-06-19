#coding:utf-8
from django.shortcuts import render_to_response
from django import forms
from django.http.response import HttpResponseRedirect

class User(forms.Form):
    username=forms.CharField()

def login(req):
    if req.method == 'POST':
        uf = User(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            req.session['username']=username
            print username
            return HttpResponseRedirect('../index/')
    else:
        uf =User()
    return render_to_response('sessionlogin.html',{'title':'session登录','uf':uf})   

def index(req):
    username = req.session.get('username','othername')
    return render_to_response('sessionindex.html',{'title':'session内容','username':username})

def logout(req):
    username = req.session.get('username','othername')
    if username!='othername':
        del req.session['username']
        print('LOGOUT OK!')
    return HttpResponseRedirect('../login/')
    

