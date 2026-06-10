from langchain.tools import tool
from knowledge import bank_data, banks,loan_details,card_types,general_banking_facts
@tool
def get_interest(bank_name:str):
    '''
    returns FD interest rate for a bank
    '''
    bank_name = bank_name.lower()
    context = []
    for bank,data in bank_data.items():
        if bank in bank_name:
            context.append(f"bank:{bank}")

            for key,value in bank_data.items():
                context.append(f'{key}:{value}')
        return ','.join(context)

@tool
def calculate_emi(principal:float,annual_rate:float,years:int):
    '''
    calculate EMI.
    '''
    rate = annual_rate/ (12*100)
    nper = years*12

    emi = (principal*rate*(1+rate)**nper)/((1+rate)**nper-1)

    return round(emi,2)


@tool
def bank_names(query:str):
    '''
    about the bank names
    '''
    return banks

@tool
def loan_details_faq(query: str):
    """
    Answers questions related to loans.
    """
    query = query.lower()

    for key, value in loan_details.items():
        if key in query:
            return value

    return "Loan information not available."

@tool
def card_types_faq(query: str):
    """
    Answers questions related to debit cards, credit cards and card networks.
    """
    query = query.lower()

    for key, value in card_types.items():
        if key in query:
            return value

    return "Card information not available."

@tool
def general_banking_faq(query: str):
    """
    Answers general banking questions such as bank, ATM, account, deposit, withdrawal, etc.
    """
    query = query.lower()

    if "all" in query or "faq" in query:
        return general_banking_facts

    for key, value in general_banking_facts.items():
        if key in query:
            return value

    return "General banking information not available."