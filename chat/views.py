from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/account/login-customer")
def chatPage(request, *args, **kwargs):
    #  if not request.user.is_authenticated:
    #      return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)
