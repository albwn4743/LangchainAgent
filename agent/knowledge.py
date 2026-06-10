bank_data = {
    'sbi':{
        'fixed_deposit_interest': '6.80%',
        'savings_account_interest':'2.70%',
        'home_loan_interest':'8.50%'
    },
    'hdfc':{
        'fixed_deposit_interest': '7.00%',
        'savings_account_interest':'3.00%',
        'home_loan_interest':'8.73%'
    },
    'icici':{
        'fixed_deposit_interest': '6.90%',
        'savings_account_interest':'3.00%',
        'home_loan_interest':'8.80%'
    },
    'federal bank':{
        'fixed_deposit_interest': '6.50%',
        'savings_account_interest':'2.40%',
        'home_loan_interest':'9.50%'
    },
    'canara bank':{
        'fixed_deposit_interest': '5.80%',
        'savings_account_interest':'3.70%',
        'home_loan_interest':'6.50%'
    }
}
def bank_details(question):
    question = question.lower()
    
    for name,data in bank_data.items():
        if name in question:
            if 'fd' in question or 'fixed deposit' in question:
                return f"{name} FD intrest rate is:{data['fixed_deposit_interest']}"
            if 'savings' in question:
                return f"{name} Savings interest rate is:{data['savings_account_interest']}"
            if 'home loan' in question:
                return f"{name} Home loan interest is:{data['home_loan_interest']}"
    return None