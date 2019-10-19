from django.shortcuts import render

# Create your views here.

def category(request):
    return render(request,'index.html')

def cat_ingredient(request,pk):
    data={
        'pk':pk
    }
    return render(request,'ingrediant.html',data)

def ingredient(request):
    return render(request,'detail.html')