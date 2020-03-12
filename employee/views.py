from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.views import LoginView,LogoutView


class SignLoginView(LoginView):
    template_name = 'registration/login.html'

class OutLogoutView(LogoutView):
    next_page = 'main'

    





def main(request):
    contact_list = Employee.objects.all()
    context = {'nodes':contact_list}
    return render(request,'main.html',context)

def table_view(request):

    all_employee = Employee.objects.all()
    paginator = Paginator(all_employee,15)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)

    objects = posts.object_list
        
    return render(request,'table.html',{'page':posts,'employees':objects})

    


    
    


    

