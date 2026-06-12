from langchain_core.tools import tool
from knowledge import (
    bank_data,
    banks,
    loan_details,
    card_types,
    general_banking_facts,
)


BANK_ALIASES = {
    "state bank of india": "sbi",
    "sbi": "sbi",
    "hdfc bank": "hdfc",
    "hdfc": "hdfc",
    "icici bank": "icici",
    "icici": "icici",
    "federal bank": "federal",
    "federal": "federal",
    "canara bank": "canara",
    "canara": "canara",
}



@tool
def bank_interest_rates(bank_name: str)->str:
    """
    Get all interest rates for a given bank.

    Examples:
    - sbi
    - state bank of india
    - hdfc
    - hdfc bank
    - icici
    - federal bank
    - canara bank
    """

    query = bank_name.lower().strip()

    matched_bank = None

    for alias, bank_code in BANK_ALIASES.items():
        if alias in query:
            matched_bank = bank_code
            break

    if not matched_bank:
        return {"error": "Bank not found"}

    data = bank_data.get(matched_bank)

    return (
    f"Bank: {matched_bank}\n"
    f"FD Interest: {data['fixed_deposit_interest']}\n"
    f"Savings Interest: {data['savings_account_interest']}\n"
    f"Home Loan Interest: {data['home_loan_interest']}"
)



@tool
def calculate_emi(principal: float, annual_rate: float, years: int):
    """
    Calculate EMI (Equated Monthly Installment).

    Arguments:
        principal: Loan amount
        annual_rate: Annual interest rate in %
        years: Loan tenure in years

    Example:
        calculate_emi(1000000, 8.5, 20)
    """

    rate = annual_rate / (12 * 100)
    nper = years * 12

    if rate == 0:
        emi = principal / nper
    else:
        emi = principal * rate * (1 + rate) ** nper / ((1 + rate) ** nper - 1)

    return (
    f"EMI Calculation:\n"
    f"Principal: {principal}\n"
    f"Annual Rate: {annual_rate}%\n"
    f"Years: {years}\n"
    f"Monthly EMI: {round(emi, 2)}"
)



@tool
def bank_names(query: str):
    """
    Search available bank names.

    Examples:
    - sbi
    - federal
    - kerala
    - indian
    """

    query = query.lower().strip()

    if not query:
        return banks

    matches = [
        bank
        for bank in banks
        if query in bank.lower()
    ]

    if matches:
        return matches

    return "No matching bank found."

@tool
def loan_details_faq(query: str):
    """
    Answers questions related to loans.

    Examples:
    - What is a home loan?
    - Explain EMI
    - What is collateral?
    - What is CIBIL score?
    """

    query = query.lower()

    for key in sorted(
        loan_details.keys(),
        key=len,
        reverse=True
    ):
        if key in query:
            return (
                f"topic: {key}\n"
                f"answer: {loan_details[key]}"
            )

    return 'Not Found'


@tool
def card_types_faq(query: str):
    """
    Answers questions related to debit cards,
    credit cards, RuPay, Visa, Mastercard, etc.
    """

    query = query.lower()

    for key in sorted(
        card_types.keys(),
        key=len,
        reverse=True
    ):
        if key in query:
            return (
                f"topic: {key}\n"
                f"answer: {card_types[key]}\n"
            )

    return 'Not Found'


@tool
def general_banking_faq(query: str):
    '''Use this tool for ALL banking definitions like ATM, withdrawal, deposit, interest, loans.'''

    query = query.lower()

    if "all" in query or "faq" in query:
        return general_banking_facts

    for key in sorted(
        general_banking_facts.keys(),
        key=len,
        reverse=True
    ):
        if key in query or query in key:
            return (
                f"topic: {key}\n"
                f"answer: {general_banking_facts[key]}"
            )

    return 'Not found'