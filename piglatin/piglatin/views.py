from django.http import HttpResponse
from django.shortcuts import render


# def hello(request):
#     return HttpResponse("Hello World!")

def home(request):
    return render(request,'home.html')

def translate(request):
    original = request.GET['originaltext'].lower()

    # Pig latin translator code
    translation = ''
    for word in original.split():
        if word[0] in ["a","e","i","o","u"]:
            translation += word + 'yay '
        else:
            translation += word[1:]+word[0]+"ay "
    # Return translation
    return render(request,'translate.html',{"original":original, "translation":translation})


def about(request):
    return render(request,"about.html")
