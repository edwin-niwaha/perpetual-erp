from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from managerApp.forms import AdminLoginForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from loanApp.models import loanCategory, loanRequest, CustomerLoan, loanTransaction
from .forms import LoanCategoryForm
from loanApp.forms import LoanRequestForm
from loginApp.models import CustomerSignUp
from django.contrib.auth.models import User
from datetime import date

from django.db.models import Sum
from .amortize import MortgageAmortizationSchedule
import pandas as pd

# Create your views here.
# Create your views here.


def superuser_login_view(request):
    form = AdminLoginForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    else:
        if request.method == "POST":
            form = AdminLoginForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    if user.is_superuser:
                        login(request, user)
                        return HttpResponseRedirect(reverse("managerApp:dashboard"))
                    else:
                        return render(
                            request,
                            "admin/adminLogin.html",
                            context={"form": form, "error": "You are not Super User"},
                        )

            else:
                return render(
                    request,
                    "admin/adminLogin.html",
                    context={"form": form, "error": "Invalid Username or Password "},
                )
    return render(
        request, "admin/adminLogin.html", context={"form": form, "user": "Admin Login"}
    )


# @staff_member_required(login_url='/manager/admin-login')
def dashboard(request):
    totalCategories = (loanCategory.objects.all().count(),)
    totalCustomer = (CustomerSignUp.objects.all().count(),)
    requestLoan = (loanRequest.objects.all().filter(status="pending").count(),)
    approved = (loanRequest.objects.all().filter(status="approved").count(),)
    rejected = (loanRequest.objects.all().filter(status="rejected").count(),)
    totalLoan = (CustomerLoan.objects.aggregate(Sum("total_loan"))["total_loan__sum"],)
    totalPayable = (
        CustomerLoan.objects.aggregate(Sum("payable_loan"))["payable_loan__sum"],
    )
    totalPaid = (loanTransaction.objects.aggregate(Sum("payment"))["payment__sum"],)

    dict = {
        "totalCategories": totalCategories[0],
        "totalCustomer": totalCustomer[0],
        "request": requestLoan[0],
        "approved": approved[0],
        "rejected": rejected[0],
        "totalLoan": totalLoan[0],
        "totalPayable": totalPayable[0],
        "totalPaid": totalPaid[0],
    }
    print(dict)

    return render(request, "admin/dashboard.html", context=dict)


# @staff_member_required(login_url='/manager/admin-login')
def add_category(request):
    form = LoanCategoryForm()
    if request.method == "POST":
        form = LoanCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("managerApp:dashboard")
    return render(request, "admin/admin_add_category.html", {"form": form})


# @staff_member_required(login_url='/manager/admin-login')
def total_users(request):
    users = CustomerSignUp.objects.all()

    return render(request, "admin/customer.html", context={"users": users})


# @staff_member_required(login_url='/manager/admin-login')
def user_remove(request, pk):
    CustomerSignUp.objects.get(id=pk).delete()
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect("/manager/users")
    # return redirect('managerApp:users')


# @staff_member_required(login_url='/manager/admin-login')
def loan_request(request):
    loanrequest = loanRequest.objects.filter(status="pending")
    return render(
        request, "admin/request_user.html", context={"loanrequest": loanrequest}
    )


# @staff_member_required(login_url='/manager/admin-login')
def approved_request(request, id):
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    year = loan_obj.year

    approved_customer = loanRequest.objects.get(id=id).customer
    if CustomerLoan.objects.filter(customer=approved_customer).exists():
        # find previous amount of customer
        PreviousAmount = CustomerLoan.objects.get(customer=approved_customer).total_loan
        PreviousPayable = CustomerLoan.objects.get(
            customer=approved_customer
        ).payable_loan

        # update balance
        CustomerLoan.objects.filter(customer=approved_customer).update(
            total_loan=int(PreviousAmount) + int(loan_obj.amount)
        )
        CustomerLoan.objects.filter(customer=approved_customer).update(
            payable_loan=int(PreviousPayable)
            + int(loan_obj.amount)
            + int(loan_obj.amount) * 0.12 * int(year)
        )

    else:
        # request customer

        # CustomerLoan object create
        save_loan = CustomerLoan()

        save_loan.customer = approved_customer
        save_loan.total_loan = int(loan_obj.amount)
        save_loan.payable_loan = int(loan_obj.amount) + int(
            loan_obj.amount
        ) * 0.12 * int(year)
        save_loan.save()

    loanRequest.objects.filter(id=id).update(status="approved")
    loanrequest = loanRequest.objects.filter(status="pending")
    return render(
        request, "admin/request_user.html", context={"loanrequest": loanrequest}
    )


# @staff_member_required(login_url='/manager/admin-login')
def rejected_request(request, id):
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    # rejected_customer = loanRequest.objects.get(id=id).customer
    # print(rejected_customer)
    loanRequest.objects.filter(id=id).update(status="rejected")
    loanrequest = loanRequest.objects.filter(status="pending")
    return render(
        request, "admin/request_user.html", context={"loanrequest": loanrequest}
    )


# @staff_member_required(login_url='/manager/admin-login')
def approved_loan(request):
    # print(datetime.now())
    approvedLoan = loanRequest.objects.filter(status="approved")
    return render(
        request, "admin/approved_loan.html", context={"approvedLoan": approvedLoan}
    )


# @staff_member_required(login_url='/manager/admin-login')
def rejected_loan(request):
    rejectedLoan = loanRequest.objects.filter(status="rejected")
    return render(
        request, "admin/rejected_loan.html", context={"rejectedLoan": rejectedLoan}
    )


# @staff_member_required(login_url="/manager/admin-login")
def update_loan(request, id, template_name="admin/loan_update.html"):
    loan = get_object_or_404(loanRequest, id=id)
    form = LoanRequestForm(request.POST or None, instance=loan)
    if form.is_valid():
        form.save()
        return redirect("managerApp:loan_request")
    return render(request, template_name, {"form": form})


# @staff_member_required(login_url="/manager/admin-login")
def delete_loan(request, id):
    loans = loanRequest.objects.get(id=id)
    loans.delete()
    return HttpResponseRedirect(reverse("managerApp:loan_request"))


# @staff_member_required(login_url="/manager/admin-login")
def loan_schedule(request, id, template_name="admin/loan_schedule.html"):
    loan = get_object_or_404(loanRequest, id=id)
    form = LoanRequestForm(request.POST or None, instance=loan)
    return render(request, template_name, {"form": form})


# @staff_member_required(login_url="/manager/admin-login")
def amortization_schedule(request):
    form = LoanRequestForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            loan_amount = form.cleaned_data["amount"]
            annual_interest_rate = form.cleaned_data["annual_interest_rate"]
            monthly_prepayment = form.cleaned_data["monthly_prepayment"]
            loan_term_years = form.cleaned_data["year"]
            loan_term_months = int(loan_term_years) * 12

            schedule, summary = MortgageAmortizationSchedule(
                loan_amount, annual_interest_rate, loan_term_months, monthly_prepayment
            )

            df = pd.DataFrame(schedule)
            df = df.round(0)
            df = df.astype(int)
            df = df.style.set_table_attributes(
                'class="table table-striped table-bordered border-info text-center align-items-center bg-light"'
            ).format("{:,}")

            print(f"Loan schedule has been generated!")
            print("Summary:")
            print(summary)

            html_table = df.to_html()
            return render(
                request,
                "admin/schedule_display.html",
                {
                    "html_table": html_table,
                },
            )
    context = {"form": form, "schedule": ""}
    return render(request, "admin/loan_schedule.html", context)


# @staff_member_required(login_url='/manager/admin-login')
def transaction_loan(request):
    transactions = loanTransaction.objects.all()
    return render(
        request, "admin/transaction.html", context={"transactions": transactions}
    )


# @login_required()
def logout(request):
    return HttpResponseRedirect(reverse("home"))
