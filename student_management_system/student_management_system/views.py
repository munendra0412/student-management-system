from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from app.models import CustomUser
from django.contrib.auth.decorators import login_required

def BASE(request):
  return render(request, "base.html")

def LOGIN(request):
  return render(request, "login.html")


def DOLOGIN(request):
  if request.method == 'POST':
    user_name = request.POST.get('email')
    password = request.POST.get('password')
    print(user_name, password)
    user = EmailBackEnd.authenticate(request, username=user_name, password=password)
    print(user)
    if user != None:
      login(request, user)
      user_type = user.user_type
      if user_type == '1':
        return redirect('hod_home')
      elif user_type == '2':
        return HttpResponse("This is STAFF") 
      elif user_type == '3':
        return HttpResponse("This is STUDENT") 
      else:
        messages.error(request,'Email/Password Invalid')
        return redirect('login')
    else:
      messages.error(request,'Email/Password Invalid')
      return redirect('login')
    
def DOLOGOUT(request):
  logout(request)
  return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
  user = CustomUser.objects.get(id=request.user.id)
  context = {'user':user}

  return render(request,'profile.html', context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
  if request.method == "POST":
    profile_pic = request.FILES.get('profile_pic')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')

    try:
      customuser = CustomUser.objects.get(id=request.user.id)
      customuser.first_name = first_name
      customuser.last_name = last_name
      customuser.profile_pic = profile_pic
      
      if password != None and password != "":
        customuser.set_password(password)

      # if profile_pic != None and profile_pic != "":
      #   customuser.profile_pic = profile_pic

      customuser.save()
      messages.success(request,'Profile Updated Successfully')
      return redirect('profile')
    except:
      messages.error(request,'Profile not Updated')

  return render(request,'profile.html')
            


