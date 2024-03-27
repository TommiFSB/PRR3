from django.shortcuts import render, HttpResponse

# Create your views here.
def first_page(request):
    return render(request,'1.html')