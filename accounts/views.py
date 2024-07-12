from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . forms import SignUpForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            #Login user
            user = authenticate(request,username=username,password=password)
            login(request,user)
            # messages.success(request,'You have successfully registered...')
            return redirect('home')
    return render(request,'accounts/register.html',{'form':form})