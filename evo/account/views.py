from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import logForm,RegForm
# Create your views here.


class LandingView(TemplateView):
    template_name="landing.html"

class LoginView(FormView):
    template_name="login.html"
    form_class=logForm
    def post(self,request):
        form_data=logForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('uhome')
            else:
                return redirect('log')
        else:
            return render(request,"login.html",{"form",form_data})
        
class RegView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    success_url=reverse_lazy('log')


class ReviewView(TemplateView):
    template_name="review.html"


class CarView(TemplateView):
    template_name="car.html"

class BikeView(TemplateView):
    template_name="bike.html"

class BikerView(TemplateView):
    template_name="b1.html"

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')