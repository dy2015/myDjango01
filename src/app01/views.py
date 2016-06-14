from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# Create your views here.
def index(req, uid,name):
    return render_to_response('index.html', {'title':'my page', 'uid':uid, 'name':name})
#     str='<html><title></title><body>id:'+uid+'name:'+name+'</body></html>'
#     return HttpResponse(str)
