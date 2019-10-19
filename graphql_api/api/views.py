from django.shortcuts import render

# Create your views here.

def category(request):
    return render(request,'index.html')

def cat_ingredient(request):
    return render(request,'ingrediant.html')

def ingredient(request):
    return render(request,'detail.html')