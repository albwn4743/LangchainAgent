NOT_FOUND = "NOT_FOUND"

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
    'federal':{
        'fixed_deposit_interest': '6.50%',
        'savings_account_interest':'2.40%',
        'home_loan_interest':'9.50%'
    },
    'canara':{
        'fixed_deposit_interest': '5.80%',
        'savings_account_interest':'3.70%',
        'home_loan_interest':'6.50%'
    }
}

loan_details = {
    "loan": {
        "answer": "A loan is money borrowed from a bank that must be repaid with interest.",
        "keywords": ["loan", "borrow", "borrowing", "lend", "lending"],
    },
    "home loan": {
        "answer": "A home loan is borrowed money used to purchase or construct a house.",
        "keywords": ["home loan", "housing loan", "house loan", "property loan", "mortgage loan"],
    },
    "personal loan": {
        "answer": "A personal loan is an unsecured loan used for personal expenses.",
        "keywords": ["personal loan", "unsecured loan", "individual loan"],
    },
    "education loan": {
        "answer": "An education loan helps students finance their academic studies.",
        "keywords": ["education loan", "student loan", "study loan", "academic loan", "educational loan"],
    },
    "gold loan": {
        "answer": "A gold loan is secured by pledging gold ornaments as collateral.",
        "keywords": ["gold loan", "gold mortgage", "jewel loan", "ornament loan"],
    },
    "car loan": {
        "answer": "A car loan helps customers purchase a vehicle through borrowed funds.",
        "keywords": ["car loan", "vehicle loan", "auto loan", "automobile loan", "bike loan", "two wheeler loan"],
    },
    "emi": {
        "answer": "Equated Monthly Installment is the fixed amount paid every month towards loan repayment.",
        "keywords": ["emi", "equated monthly installment", "monthly installment", "monthly payment", "monthly repayment"],
    },
    "principal": {
        "answer": "The principal is the original amount of money borrowed or invested.",
        "keywords": ["principal", "principal amount", "loan amount", "original amount"],
    },
    "collateral": {
        "answer": "Collateral is an asset pledged to secure a loan.",
        "keywords": ["collateral", "security", "pledge", "asset pledge", "guarantee"],
    },
    "mortgage": {
        "answer": "A mortgage is a loan secured against real estate property.",
        "keywords": ["mortgage", "property mortgage", "real estate loan", "home mortgage"],
    },
    "overdraft": {
        "answer": "An overdraft allows customers to withdraw more money than is available in their account.",
        "keywords": ["overdraft", "od", "od limit", "overdraft facility"],
    },
    "credit score": {
        "answer": "A credit score reflects an individual's ability to repay borrowed money.",
        "keywords": ["credit score", "credit rating", "credit history", "creditworthiness"],
    },
    "cibil score": {
        "answer": "A CIBIL score is a credit score that indicates a person's creditworthiness.",
        "keywords": ["cibil", "cibil score", "cibil report", "credit bureau score"],
    },
    "npa": {
        "answer": "Non-Performing Asset is a loan on which the borrower has stopped making repayments.",
        "keywords": ["npa", "non performing asset", "bad loan", "defaulted loan", "bad debt"],
    },
}

card_types = {
    "debit card": {
        "answer": "A debit card allows customers to spend money directly from their bank account.",
        "keywords": ["debit card", "debit", "bank card", "atm card", "withdrawal card"],
    },
    "credit card": {
        "answer": "A credit card allows customers to borrow money from the bank up to a pre-approved limit.",
        "keywords": ["credit card", "credit", "charge card", "credit limit card"],
    },
    "rupay card": {
        "answer": "A RuPay card is an Indian domestic card payment network used for debit and credit cards.",
        "keywords": ["rupay", "rupay card", "ru pay", "india card network"],
    },
    "visa card": {
        "answer": "A Visa card is a globally accepted payment card issued by participating banks.",
        "keywords": ["visa", "visa card", "visa debit", "visa credit"],
    },
    "mastercard": {
        "answer": "A Mastercard is an international payment card accepted worldwide.",
        "keywords": ["mastercard", "master card", "mc", "mastercard debit", "mastercard credit"],
    },
    "prepaid card": {
        "answer": "A prepaid card can be loaded with money in advance and used for payments.",
        "keywords": ["prepaid card", "prepaid", "reloadable card", "gift card", "loaded card"],
    },
    "virtual card": {
        "answer": "A virtual card is a digital payment card used for secure online transactions.",
        "keywords": ["virtual card", "virtual", "digital card", "online card", "e-card"],
    },
    "contactless card": {
        "answer": "A contactless card enables tap-and-pay transactions using NFC technology.",
        "keywords": ["contactless card", "contactless", "tap card", "tap and pay", "nfc card", "nfc payment"],
    },
}

general_banking_facts = {
    "bank": {
        "answer": "A bank is a financial institution that accepts deposits, provides loans, and offers various financial services.",
        "keywords": ["bank", "banking", "financial institution", "bank definition"],
    },
    "atm": {
        "answer": "An Automated Teller Machine allows customers to withdraw cash, check balances, and perform basic banking transactions.",
        "keywords": ["atm", "automated teller machine", "cash machine", "cash point", "atm machine"],
    },
    "account": {
        "answer": "A bank account is a financial account maintained by a bank for a customer.",
        "keywords": ["account", "bank account", "savings account", "current account", "checking account"],
    },
    "deposit": {
        "answer": "A deposit is money placed into a bank account for safekeeping or investment.",
        "keywords": ["deposit", "fixed deposit", "fd", "recurring deposit", "rd", "term deposit"],
    },
    "withdrawal": {
        "answer": "A withdrawal is the process of taking money out of a bank account.",
        "keywords": ["withdrawal", "withdraw", "cash out", "take out money"],
    },
    "interest": {
        "answer": "Interest is the amount paid by a bank on deposits or charged on loans.",
        "keywords": ["interest", "interest rate", "rate of interest", "roi", "interest charge"],
    },
    "transaction": {
        "answer": "A transaction is any activity involving the movement of money into or out of an account.",
        "keywords": ["transaction", "transfer", "payment", "money movement", "banking transaction"],
    },
    "balance": {
        "answer": "Balance is the amount of money available in a bank account.",
        "keywords": ["balance", "account balance", "available balance", "bank balance", "current balance"],
    },
    "branch": {
        "answer": "A branch is a physical office of a bank where customers can access banking services.",
        "keywords": ["branch", "bank branch", "bank office", "banking center"],
    },
    "passbook": {
        "answer": "A passbook is a book issued by a bank that records account transactions.",
        "keywords": ["passbook", "pass book", "bank book", "account book", "statement book"],
    },
    "neft": {
        "answer": "National Electronic Funds Transfer is an electronic system to transfer money between bank accounts across India.",
        "keywords": ["neft", "national electronic funds transfer", "neft transfer", "neft payment"],
    },
    "rtgs": {
        "answer": "Real Time Gross Settlement is an instant large-value funds transfer system.",
        "keywords": ["rtgs", "real time gross settlement", "rtgs transfer", "high value transfer"],
    },
    "imps": {
        "answer": "Immediate Payment Service is a real-time interbank electronic fund transfer service available 24/7.",
        "keywords": ["imps", "immediate payment service", "instant transfer", "imps transfer"],
    },
    "upi": {
        "answer": "Unified Payments Interface is an instant real-time payment system developed by NPCI for mobile-based transfers.",
        "keywords": ["upi", "unified payments interface", "upi payment", "gpay", "phonepe", "bhim"],
    },
    "kyc": {
        "answer": "Know Your Customer is a mandatory bank process to verify a customer's identity before opening an account.",
        "keywords": ["kyc", "know your customer", "kyc verification", "kyc documents", "identity verification"],
    },
    "ifsc": {
        "answer": "Indian Financial System Code is an 11-character code that identifies every bank branch for electronic fund transfers.",
        "keywords": ["ifsc", "ifsc code", "indian financial system code", "branch code"],
    },
    "locker": {
        "answer": "A bank locker is a safe deposit box rented by a bank to customers for storing valuables.",
        "keywords": ["locker", "bank locker", "safe deposit box", "locker facility"],
    },
}
