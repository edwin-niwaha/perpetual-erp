import pandas as pd


def MortgageAmortizationSchedule(
    loan_amount, annual_interest_rate, loan_term_months, monthly_prepayment
):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months)
        / ((1 + monthly_interest_rate) ** loan_term_months - 1)
    )

    schedule = []
    remaining_balance = loan_amount
    original_loan_amount = loan_amount
    original_loan_term_months = loan_term_months

    for month in range(1, loan_term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment

        # Check if the current month is within the first 2 years of loan
        if month <= 2 * 12:
            remaining_balance -= monthly_payment + monthly_prepayment - interest_payment
        else:
            remaining_balance -= monthly_payment - interest_payment

        if remaining_balance <= 0:
            # Loan is fully paid, no need to continue calculating the schedule
            loan_term_months = month
            break

        schedule.append(
            {
                "Month": month,
                "Monthly Payment": monthly_payment,
                "Interest Payment": interest_payment,
                "Principal Payment": principal_payment,
                "Prepayment": monthly_prepayment if month <= 2 * 12 else 0,
                "Remaining Balance": max(
                    0, remaining_balance
                ),  # Ensure balance doesn't go negative
            }
        )

    # Calculate total interest savings and total tenure reduced
    original_interest = (
        monthly_payment * original_loan_term_months
    ) - original_loan_amount
    new_interest = (monthly_payment * loan_term_months) - loan_amount
    interest_savings = original_interest - new_interest
    tenure_reduced_months = original_loan_term_months - loan_term_months
    total_interest = (monthly_payment * loan_term_months) - loan_amount
    total_principal = loan_amount

    summary = {
        "Total Interest Savings": interest_savings,
        "Total Tenure Reduced (months)": tenure_reduced_months,
        "Total interest": total_interest,
        "Total principal": total_principal,
    }

    return schedule, summary
