from django.shortcuts import render_to_response

# Create your views here.
def index(req, uid, name):
    return render_to_response('index.html', {'title':'my page', 'uid':uid, 'name':name})
