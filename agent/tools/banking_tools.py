from langchain_core.tools import tool
import re
from knowledge import (
    bank_data,
    banks,
    loan_details,
    card_types,
    general_banking_facts,
)
def _normalize(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text.lower())).strip()

def _match_key(query_clean: str, keys) -> str | None:
    """Return the longest key whose words all appear in the query."""
    for key in sorted(keys, key=len, reverse=True):
        key_words = key.split()
        if all(w in query_clean.split() for w in key_words):
            return key
    return None




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
    f"Home Loan Interest: {data['home_loan_interest']}")


@tool
def bank_names(query: str):
    """
    Search available bank names.

    Examples:
    - sbi
    - federal
    - kerala
    - indian
    - list all banks
    """
    clean = _normalize(query)

    # Handle "list all" / "show all" intent
    if not clean or any(w in clean.split() for w in ["all", "list", "show"]):
        return banks

    matches = [b for b in banks if any(w in b for w in clean.split())]
    return matches if matches else "No matching bank found."

@tool
def loan_details_faq(query: str):
    """
    Answers questions related to loans.
    Trigger words: loan, emi,principal,collateral,mortgage,overdraft,npa,credit score,cibil.

    Examples:
    - What is a home loan?
    - Explain EMI
    - What is collateral?
    - What is CIBIL score?
    """
    clean = _normalize(query)
    key = _match_key(clean, loan_details.keys())
    if key:
        return f"topic: {key}\nanswer: {loan_details[key]}"
    return "Not Found"


@tool
def card_types_faq(query: str):
    """
    Answers questions related to debit cards,
    credit cards, RuPay, Visa, Mastercard, etc.
    examples:
        what is a debit card?
        explain credit card
        what is rupay?
        tell me about visa card
    """
    clean = _normalize(query)
    key = _match_key(clean, card_types.keys())
    if key:
        return f"topic: {key}\nanswer: {card_types[key]}"
    return "Not Found"


@tool
def general_banking_faq(query: str):
    """Use this tool for ALL banking definitions like ATM, withdrawal, deposit, interest, loans."""
    clean = _normalize(query)

    # Handle "all" / "faq" intent
    if "all" in clean.split() or "faq" in clean.split():
        return general_banking_facts

    key = _match_key(clean, general_banking_facts.keys())
    if key:
        return f"topic: {key}\nanswer: {general_banking_facts[key]}"
    return "Not found"

