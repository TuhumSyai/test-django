from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello")

# def contact(request):
#     return render(request, 'contact.html')