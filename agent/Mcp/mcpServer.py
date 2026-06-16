from mcp.server.fastmcp import FastMCP

mcp = FastMCP('first MCP server')


@mcp.tool()
def greet(name:str)->str:
    '''Greet a user'''
    return f"Hello, {name}"

@mcp.tool()
def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:
    """
    Calculate Equated Monthly Installment (EMI), total interest, and total payable amount.
    
    Args:
        principal: The loan principal amount (e.g. 500000)
        annual_rate: The annual interest rate in percent (e.g. 8.5)
        years: The tenure of the loan in years (e.g. 15)
    """
    rate = annual_rate / (12 * 100)
    months = years * 12
    if rate == 0:
        emi = principal / months
    else:
        emi = principal * rate * ((1 + rate) ** months) / (((1 + rate) ** months) - 1)
    
    total_payable = emi * months
    total_interest = total_payable - principal
    
    return {
        "monthly_emi": round(emi, 2),
        "principal": principal,
        "total_interest_payable": round(total_interest, 2),
        "total_amount_payable": round(total_payable, 2),
        "tenure_months": months
    }

@mcp.tool()
def calculate_compound_interest(principal: float, annual_rate: float, years: float, compounding_frequency: int = 1) -> dict:
    """
    Calculate compound interest and the final maturity amount.
    
    Args:
        principal: The initial principal amount (e.g. 10000)
        annual_rate: The annual interest rate in percent (e.g. 6.5)
        years: The time period in years (can be fractional, e.g. 2.5)
        compounding_frequency: Times interest is compounded per year (1=annually, 4=quarterly, 12=monthly, 365=daily). Default is 1.
    """
    rate_decimal = annual_rate / 100
    amount = principal * ((1 + rate_decimal / compounding_frequency) ** (compounding_frequency * years))
    interest = amount - principal
    
    return {
        "initial_principal": principal,
        "interest_rate_percent": annual_rate,
        "years": years,
        "compounding_frequency_per_year": compounding_frequency,
        "interest_earned": round(interest, 2),
        "total_maturity_amount":round(amount,2)
    }

@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Convert money from one currency to another using fixed exchange rates.
    Supported currencies: USD, EUR, GBP, INR, JPY, CAD, AUD.
    
    Args:
        amount: The amount of money to convert.
        from_currency: 3-letter currency code of the source currency (e.g. USD).
        to_currency: 3-letter currency code of the target currency (e.g. INR).
    """
    # Standard rates relative to USD (1 USD = target currency amount)
    rates_to_usd = {
        "USD": 1.0,
        "EUR": 0.92,
        "INR": 83.50,
        "CAD": 1.37,
        "AUD": 1.51
    }
    
    from_curr = from_currency.strip().upper()
    to_curr = to_currency.strip().upper()

    if from_curr not in rates_to_usd or to_curr not in rates_to_usd:
        supported = ", ".join(rates_to_usd.keys())
        return {
            "error": f"Unsupported currency code. Supported currencies: {supported}"
        }
    
    # Convert to USD first, then to target currency
    amount_in_usd = amount / rates_to_usd[from_curr]
    converted_amount = amount_in_usd * rates_to_usd[to_curr]
    
    return {
        "original_amount": amount,
        "from_currency": from_curr,
        "to_currency": to_curr,
        "converted_amount": round(converted_amount, 2)
    }
    
if __name__ == '__main__':
    mcp.run()

# print(greet('Albin'))