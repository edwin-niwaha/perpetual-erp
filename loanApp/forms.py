from django import forms
from .models import loanRequest, loanTransaction


class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = loanRequest
        fields = (
            "category",
            "reason",
            "amount",
            "year",
            "annual_interest_rate",
            "monthly_prepayment",
        )
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control", "min": 100000}),
            "year": forms.NumberInput(
                attrs={"class": "form-control", "min": 1, "max": 2}
            ),
        }


# https://hugsformybugs.medium.com/saving-data-using-django-model-form-7ec9d8471ccf


class LoanTransactionForm(forms.ModelForm):
    class Meta:
        model = loanTransaction
        fields = ("payment",)
