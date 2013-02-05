from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('staticsite/index.html',{})

def contact(request):
    return render_to_response('staticsite/contact.html',{},
                               context_instance=RequestContext(request))

def contactSubmit(request):
    header = request.POST['msgHeader']
    message = request.POST['msgBody']
    return render_to_response('staticsite/contactSubmitted.html', {'header':header,'message':message,})
