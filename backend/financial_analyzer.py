
from data_fetcher import get_stock_data

import pandas as pd
from fred_data import get_fred_data
# from sec_scraper import get_openinsider_data


def replace_nan(data):
    if isinstance(data, dict):
        return {k: replace_nan(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_nan(i) for i in data]
    elif isinstance(data, float) and pd.isna(data):
        return None
    return data

def calculate_pe_ratio(stock_data):
    """
    Calculates the Price-to-Earnings (P/E) ratio.
    """
    try:
        pe_ratio = stock_data["info"]["trailingPE"]
        return pe_ratio
    except KeyError:
        return None

def calculate_pb_ratio(stock_data):
    """
    Calculates the Price-to-Book (P/B) ratio.
    """
    try:
        pb_ratio = stock_data["info"]["priceToBook"]
        return pb_ratio
    except KeyError:
        return None

def calculate_de_ratio(stock_data):
    """
    Calculates the Debt-to-Equity (D/E) ratio.
    """
    try:
        total_debt = stock_data["balance_sheet"].loc["Total Debt"]
        total_equity = stock_data["balance_sheet"].loc["Total Equity Gross Minority Interest"]
        # Use the most recent year's data
        de_ratio = total_debt.iloc[0] / total_equity.iloc[0]
        return de_ratio
    except (KeyError, IndexError):
        return None

def calculate_current_ratio(stock_data):
    """
    Calculates the Current Ratio.
    """
    try:
        current_assets = stock_data["balance_sheet"].loc["Current Assets"]
        current_liabilities = stock_data["balance_sheet"].loc["Current Liabilities"]
        current_ratio = current_assets.iloc[0] / current_liabilities.iloc[0]
        return current_ratio
    except (KeyError, IndexError):
        return None

def calculate_quick_ratio(stock_data):
    """
    Calculates the Quick Ratio.
    """
    try:
        current_assets = stock_data["balance_sheet"].loc["Current Assets"]
        inventory = stock_data["balance_sheet"].loc["Inventory"]
        current_liabilities = stock_data["balance_sheet"].loc["Current Liabilities"]
        quick_ratio = (current_assets.iloc[0] - inventory.iloc[0]) / current_liabilities.iloc[0]
        return quick_ratio
    except (KeyError, IndexError):
        return None

def calculate_ps_ratio(stock_data):
    """
    Calculates the Price-to-Sales (P/S) ratio.
    """
    try:
        ps_ratio = stock_data["info"]["priceToSalesTrailing12Months"]
        return ps_ratio
    except KeyError:
        return None

def calculate_ev_to_ebitda(stock_data):
    """
    Calculates the Enterprise Value to EBITDA (EV/EBITDA) ratio.
    """
    try:
        ev_to_ebitda = stock_data["info"]["enterpriseToEbitda"]
        return ev_to_ebitda
    except KeyError:
        return None

def analyze_stock(ticker):
    """
    Performs a financial analysis of a given stock.
    """
    stock_data = get_stock_data(ticker)
    fred_data = get_fred_data(api_key="b04b0764e1181f9e8c8735068e0f03ce")
    
    analysis = {
        "ticker": ticker,
        "info": stock_data["info"],
        "pe_ratio": calculate_pe_ratio(stock_data),
        "pb_ratio": calculate_pb_ratio(stock_data),
        "de_ratio": calculate_de_ratio(stock_data),
        "current_ratio": calculate_current_ratio(stock_data),
        "quick_ratio": calculate_quick_ratio(stock_data),
        "ps_ratio": calculate_ps_ratio(stock_data),
        "ev_to_ebitda": calculate_ev_to_ebitda(stock_data),
        "historical_revenue": stock_data["financials"].loc["Total Revenue"].to_dict() if "Total Revenue" in stock_data["financials"].index else None,
        "historical_net_income": stock_data["financials"].loc["Net Income"].to_dict() if "Net Income" in stock_data["financials"].index else None,
        "dividend_yield": stock_data["info"].get("dividendYield"),
        "dividend_rate": stock_data["info"].get("dividendRate"),
        "payout_ratio": stock_data["info"].get("payoutRatio"),
        "ex_dividend_date": stock_data["info"].get("exDividendDate"),
        "major_holders": stock_data["major_holders"].to_dict() if stock_data["major_holders"] is not None else None,
        "institutional_holders": stock_data["institutional_holders"].to_dict() if stock_data["institutional_holders"] is not None else None,
#        "insider_transactions": get_openinsider_data(ticker),
        "company_officers": stock_data["info"].get("companyOfficers"),
    }
    
    analysis = replace_nan(analysis)
    return analysis

if __name__ == '__main__':
    # Example usage
    ticker = "MSFT"
    analysis = analyze_stock(ticker)
    
    print(f"Financial Analysis for {ticker}:")
    print(f"P/E Ratio: {analysis['pe_ratio']}")
    print(f"P/B Ratio: {analysis['pb_ratio']}")
    print(f"D/E Ratio: {analysis['de_ratio']}")
    print(f"Current Ratio: {analysis['current_ratio']}")
    print(f"Quick Ratio: {analysis['quick_ratio']}")
    print(f"P/S Ratio: {analysis['ps_ratio']}")
    print(f"EV/EBITDA: {analysis['ev_to_ebitda']}")
