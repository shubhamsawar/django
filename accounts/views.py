from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
 
from . forms import SignUpForm

# Create your views here.


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
            
        
    else:
        form = SignUpForm()
    return render(request,'account/signup.html',{'form': form})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            un = request.POST['username']
            pw = request.POST['password']
            user = authenticate(request,username=un, password=pw)
            if user is not None:
                login(request, user )
                return HttpResponseRedirect('/home/')
            else:
                
                return HttpResponseRedirect('account/login/')
    return render(request,'account/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))