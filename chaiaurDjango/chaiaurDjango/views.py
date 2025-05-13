from django.http import HttpResponse 




def home(request):
    return HttpResponse("hello, world. You are at home page")

def about(request):
    return HttpResponse("Hello world. You are at about page")

def contact(request):
    return HttpResponse("Hello world. You are at contact page")




