from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def inscription(request):
  if request.method == "POST":
    # recuperation des valeurs
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # check if password much
    if password == password2:
      pass
      #check username
      if User.objects.filter(username=username).exists():
        messages.error(request, "That username is taken")
        return redirect('inscription')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, "That email is being used")
          return redirect('inscription')
        else:
          # looks good
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # auth.login(request, user)
          # messages.success(request, "You are logged in")
          # return redirect(request, "index")
          user.save()
          messages.success(request, "You are now registred and can log  in")
          return redirect("login")
    else:
      messages.error(request, "Password didn't match")
      return redirect('inscription')
    #Resgister user
    print("e")
  else:
    context = {}
    return render(request, "accounts/inscription.html", context)

def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, "You now log in")
      return redirect("/")
    else:
      messages.error(request, "Invalid creadentiel")
      return redirect("login")

  else:
    #context = {}
    return render(request, "accounts/login.html")

def logout(request):
  if request.method == "POST":
    auth.logout(request)
    messages.success(request, "You are log out")
    return redirect('/')

