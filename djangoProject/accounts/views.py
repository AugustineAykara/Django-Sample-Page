from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']        
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username already exist")
            elif User.objects.filter(email=email).exists():
                print("email id already exist")
            else:
                user = User.objects.create_user(username = username, password = password1, first_name = first_name, last_name = last_name, email = email)
                user.save();
                print("user created")
        else:
            print("Password not matching")

        return redirect('/')
        
    else: 
        return render(request, 'register.html')