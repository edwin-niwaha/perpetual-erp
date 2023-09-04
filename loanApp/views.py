from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from .forms import LoanRequestForm, LoanTransactionForm
# from .models import loanRequest, loanTransaction, CustomerLoan
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.db.models import Sum

# Create your views here.


# @login_required(login_url='/account/login-customer')
def home(request):
    return render(request, "home.html", context={})


def error_404_view(request, exception):
    print("not found")
    return render(request, "notFound.html")
