from django.shortcuts import render
from products.models import * 
# Create your views here.
def main(request):
    return render(request,'index.html',{})  

def contact(request):
    return render(request,'c.html',{})  

def choose(request):
    return render(request,'choose.html',{})  

def auc(request):
    nu = auction.objects.all().count()
    img=[auction.objects.get(id=i).img for i in range(1,nu+1)] 
    desc = [auction.objects.get(id=i).descraption for i in range(1, nu+1)] 
    price=[auction.objects.get(id=i).price for i in range(1,nu+1)]
    context = zip(img,price,desc) 
    return render(request,'auction.html',{'all':context})  

def tuc(request):
    nu = truck_part.objects.all().count()
    img=[truck_part.objects.get(id=i).img for i in range(1,nu+1)] 
    desc = [truck_part.objects.get(id=i).descraption for i in range(1, nu+1)] 
    price=[truck_part.objects.get(id=i).price for i in range(1,nu+1)]
    context = zip(img,price,desc) 
    return render(request,'truck_parts.html',{'all':context})  