from langchain_core.tools import tool
import re
from knowledge import (
    NOT_FOUND,
    bank_data,
    loan_details,
    card_types,
    general_banking_facts,
)
def _resolve_bank(query: str) -> str | None:
    """Return the canonical bank key for *query*, or None if not found."""
    q = query.lower().strip()
    for key, data in bank_data.items():
        for alias in data.get("aliases", []):
            if alias in q or q in alias:
                return key
    # Fallback: direct key match
    if q in bank_data:
        return q
    return None

def _match_keyword_entry(query: str, knowledge: dict) -> tuple[str, dict] | None:
    """
    Return the (topic, entry) whose keywords best match *query*.
    Tries longest-key match first to avoid false positives on short keys.
    """
    q = query.lower().strip()
    # Sort by length of key descending so more specific keys match first
    for topic in sorted(knowledge.keys(), key=len, reverse=True):
        entry = knowledge[topic]
        keywords = entry.get("keywords", [topic])
        for kw in sorted(keywords, key=len, reverse=True):
            if kw in q:
                return topic, entry
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
def loan_details_faq(query: str) -> str:
    """
    Answer questions about loan types and banking loan terminology.

    Handles: home loan, personal loan, education loan, gold loan, car loan,
    EMI, principal, collateral, mortgage, overdraft, credit score, CIBIL, NPA.

    Example inputs:
    - "What is a home loan?"
    - "Explain EMI"
    - "What is CIBIL score?"
    - "What does NPA mean?"
    """
    result = _match_keyword_entry(query, loan_details)
    if not result:
        return NOT_FOUND
    topic, entry = result
    return f"Topic : {topic.title()}\nAnswer: {entry['answer']}"


@tool
def card_types_faq(query: str) -> str:
    """
    Answer questions about card types: debit card, credit card, RuPay,
    Visa, Mastercard, prepaid card, virtual card, contactless card.

    Example inputs:
    - "What is a credit card?"
    - "Tell me about RuPay"
    - "What is a contactless card?"
    """
    result = _match_keyword_entry(query, card_types)
    if not result:
        return NOT_FOUND
    topic, entry = result
    return f"Topic : {topic.title()}\nAnswer: {entry['answer']}"


@tool
def general_banking_faq(query: str) -> str:
    """
    Answer general banking definitions, concepts, terminology, and FAQs.

    Use this tool whenever the user asks:

    - What is a bank?
    - What is banks?
    - Tell me about banks
    - What is banking?
    - Explain ATM
    - What is deposit?
    - What is withdrawal?
    - What is interest?
    - What is transaction?
    - What is account?
    - What is passbook?
    - What is NEFT?
    - What is RTGS?
    - What is IMPS?
    - What is UPI?
    - What is KYC?
    - What is IFSC?

    ALWAYS use this tool for banking definitions,
    banking terminology, and FAQ-style questions.

    Also accepts:
    - "faq"
    - "all"
    """
    print('Faqs are called')
    q = query.lower().strip()

    if q in ("all", "faq"):
        lines = []
        for topic, entry in general_banking_facts.items():
            lines.append(f"{topic.upper()}: {entry['answer']}")
        return "\n\n".join(lines)

    result = _match_keyword_entry(query, general_banking_facts)
    if not result:
        return NOT_FOUND
    topic, entry = result
    return f"Topic : {topic.upper()}\nAnswer: {entry['answer']}"
