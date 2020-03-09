from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def main(request):
    contact_list = Employee.objects.all()
    context = {'nodes':contact_list}
    return render(request,'main.html',context)

def table_view(request):
    context = {'employees':Employee.objects.all()}

    return render(request,'table.html',context)


    
    


    

