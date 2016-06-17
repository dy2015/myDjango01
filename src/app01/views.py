#coding:utf-8
from django.shortcuts import render_to_response
from django import forms

# Create your views here.

class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say(self):
        return "I'm " +self.name
    
class User(forms.Form):
    name=forms.CharField()    
    Img=forms.FileField()
    
def regist(req):
    tag=True 
    if req.method == 'POST':
        form=User(req.POST,req.FILES)
        if form.is_valid():
            user=form.cleaned_data
            print form.cleaned_data['name']
            print form.cleaned_data['Img']
            print form.cleaned_data['Img'].name
            print form.cleaned_data['Img'].size
            print user
            fp= file('G:/'+form.cleaned_data['Img'].name,'wb')
            s=form.cleaned_data['Img'].read()
            fp.write(s)
            fp.close()
            
            tag=False 
            return render_to_response('register.html', {'title':'表单','user':user,'tag':tag})
        
    else:
        form=User()
    return render_to_response('register.html', {'title':'表单','form':form,'tag':tag})
      
def index(req, uid, name):
    user=Person('张三',40,'male')
    student={'id':12,'number':12345}
    book_list=['java','python','c++']
    person_list=[]
    return render_to_response('index.html', {'title':'my page', 'uid':uid, 'name':name,'student':student,'user':user,'book_list':book_list,'person_list':person_list})


