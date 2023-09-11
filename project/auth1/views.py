from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def sign_up(req):
    if req.method == "POST":
        # Explicitily Mention because this class is borrowed from UserCreationForm
        fm = SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
            messages.success(req, 'Successfully signed Up')
            fm = LogInForm()
            return render(req, 'auth1/login.html', {'fm': fm})
    else:
        fm = SignUpForm()
    return render(req, 'auth1/signup.html', {'fm': fm})


def log_in(req):
    status = req.session.get('status')
    # print(status)
    if req.method == "POST":
        fm = LogInForm(request=req, data=req.POST)
        if fm.is_valid():
            a = fm.cleaned_data['username']
            b = fm.cleaned_data['password']
            user = authenticate(username=a, password=b)
            if user is not None:
                login(req, user)
                # messages.success(req,"successfully logged in")
                # fm = LogInForm()

                req.session['cartcount'] = 0
                req.session['status'] = 1
                status = req.session['status']
                # print(status)
                return render(req, "app/index.html", {"status": status})

    else:
        fm = LogInForm()
        return render(req, "auth1/login.html", {"fm": fm, "status": status})


def log_out(req):
    status = req.session.get('status')
    logout(req)
    req.session['status'] = 0
    status = req.session['status']
    messages.success(req, "logged out successfully")
    fm = LogInForm()
    return render(req, 'auth1/login.html', {'fm': fm})
