from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1>Hello</h1>")
    return render(request,"home.html", {})

#add contact view
def contact_view(request,*args, **kwargs):
    return render(request,"contact.html", {})
   



def about_view(request,*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")