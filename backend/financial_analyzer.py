
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

def calculate_interest_coverage_ratio(stock_data):
    """
    Calculates the Interest Coverage Ratio.
    """
    try:
        ebit = stock_data["financials"].loc["EBIT"]
        interest_expense = stock_data["financials"].loc["Interest Expense"]
        interest_coverage_ratio = ebit.iloc[0] / interest_expense.iloc[0]
        return interest_coverage_ratio
    except (KeyError, IndexError):
        return None

def calculate_debt_to_capital_ratio(stock_data):
    """
    Calculates the Debt to Capital Ratio.
    """
    try:
        total_debt = stock_data["balance_sheet"].loc["Total Debt"]
        total_equity = stock_data["balance_sheet"].loc["Total Equity Gross Minority Interest"]
        debt_to_capital_ratio = total_debt.iloc[0] / (total_debt.iloc[0] + total_equity.iloc[0])
        return debt_to_capital_ratio
    except (KeyError, IndexError):
        return None

def calculate_roic(stock_data):
    """
    Calculates the Return on Invested Capital (ROIC).
    """
    try:
        nopat = stock_data["financials"].loc["EBIT"].iloc[0] * (1 - stock_data["info"].get("taxRate", 0.25)) # Assuming 25% tax rate if not available
        total_debt = stock_data["balance_sheet"].loc["Total Debt"].iloc[0]
        total_equity = stock_data["balance_sheet"].loc["Total Equity Gross Minority Interest"].iloc[0]
        invested_capital = total_debt + total_equity
        roic = nopat / invested_capital
        return roic
    except (KeyError, IndexError):
        return None

def calculate_altman_z_score(stock_data):
    """
    Calculates the Altman Z-Score.
    """
    try:
        # A = Working Capital / Total Assets
        working_capital = stock_data["balance_sheet"].loc["Current Assets"].iloc[0] - stock_data["balance_sheet"].loc["Current Liabilities"].iloc[0]
        total_assets = stock_data["balance_sheet"].loc["Total Assets"].iloc[0]
        A = working_capital / total_assets

        # B = Retained Earnings / Total Assets
        retained_earnings = stock_data["balance_sheet"].loc["Retained Earnings"].iloc[0]
        B = retained_earnings / total_assets

        # C = EBIT / Total Assets
        ebit = stock_data["financials"].loc["EBIT"].iloc[0]
        C = ebit / total_assets

        # D = Market Value of Equity / Total Liabilities
        market_cap = stock_data["info"].get("marketCap")
        total_liabilities = stock_data["balance_sheet"].loc["Total Liabilities"].iloc[0]
        D = market_cap / total_liabilities

        # E = Sales / Total Assets
        sales = stock_data["financials"].loc["Total Revenue"].iloc[0]
        E = sales / total_assets

        z_score = 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E
        return z_score
    except (KeyError, IndexError, TypeError):
        return None

def calculate_peg_ratio(stock_data):
    """
    Calculates the Price/Earnings to Growth (PEG) ratio.
    """
    try:
        pe_ratio = stock_data["info"]["trailingPE"]
        # Use forwardAnnualEPSGrowth for growth rate if available, otherwise trailingAnnualEPSGrowth
        # yfinance often provides 'earningsGrowth' for trailing annual growth
        eps_growth = stock_data["info"].get("earningsGrowth", stock_data["info"].get("forwardEpsGrowth"))
        if pe_ratio and eps_growth and eps_growth > 0:
            peg_ratio = pe_ratio / (eps_growth * 100) # Convert growth to percentage
            return peg_ratio
        return None
    except KeyError:
        return None

def calculate_ev_to_sales(stock_data):
    """
    Calculates the Enterprise Value to Sales (EV/Sales) ratio.
    """
    try:
        enterprise_value = stock_data["info"].get("enterpriseValue")
        total_revenue = stock_data["financials"].loc["Total Revenue"].iloc[0]
        if enterprise_value and total_revenue:
            ev_to_sales = enterprise_value / total_revenue
            return ev_to_sales
        return None
    except (KeyError, IndexError):
        return None

def calculate_fcf_yield(stock_data):
    """
    Calculates the Free Cash Flow Yield.
    """
    try:
        free_cash_flow = stock_data["cashflow"].loc["Free Cash Flow"].iloc[0]
        market_cap = stock_data["info"].get("marketCap")
        if free_cash_flow and market_cap:
            fcf_yield = free_cash_flow / market_cap
            return fcf_yield
        return None
    except (KeyError, IndexError):
        return None

def calculate_gross_profit_margin(stock_data):
    """
    Calculates the Gross Profit Margin.
    """
    try:
        gross_profit = stock_data["financials"].loc["Gross Profit"]
        total_revenue = stock_data["financials"].loc["Total Revenue"]
        gross_profit_margin = gross_profit.iloc[0] / total_revenue.iloc[0]
        return gross_profit_margin
    except (KeyError, IndexError):
        return None

def calculate_operating_profit_margin(stock_data):
    """
    Calculates the Operating Profit Margin.
    """
    try:
        operating_income = stock_data["financials"].loc["Operating Income"]
        total_revenue = stock_data["financials"].loc["Total Revenue"]
        operating_profit_margin = operating_income.iloc[0] / total_revenue.iloc[0]
        return operating_profit_margin
    except (KeyError, IndexError):
        return None

def calculate_net_profit_margin(stock_data):
    """
    Calculates the Net Profit Margin.
    """
    try:
        net_income = stock_data["financials"].loc["Net Income"]
        total_revenue = stock_data["financials"].loc["Total Revenue"]
        net_profit_margin = net_income.iloc[0] / total_revenue.iloc[0]
        return net_profit_margin
    except (KeyError, IndexError):
        return None

def calculate_roe(stock_data):
    """
    Calculates the Return on Equity (ROE).
    """
    try:
        net_income = stock_data["financials"].loc["Net Income"]
        total_equity = stock_data["balance_sheet"].loc["Total Equity Gross Minority Interest"]
        roe = net_income.iloc[0] / total_equity.iloc[0]
        return roe
    except (KeyError, IndexError):
        return None

def calculate_roa(stock_data):
    """
    Calculates the Return on Assets (ROA).
    """
    try:
        net_income = stock_data["financials"].loc["Net Income"]
        total_assets = stock_data["balance_sheet"].loc["Total Assets"]
        roa = net_income.iloc[0] / total_assets.iloc[0]
        return roa
    except (KeyError, IndexError):
        return None

def calculate_asset_turnover(stock_data):
    """
    Calculates the Asset Turnover.
    """
    try:
        total_revenue = stock_data["financials"].loc["Total Revenue"]
        total_assets = stock_data["balance_sheet"].loc["Total Assets"]
        asset_turnover = total_revenue.iloc[0] / total_assets.iloc[0]
        return asset_turnover
    except (KeyError, IndexError):
        return None

def calculate_revenue_growth_rate(stock_data):
    """
    Calculates the Year-over-Year Revenue Growth Rate.
    """
    try:
        total_revenue = stock_data["financials"].loc["Total Revenue"]
        if len(total_revenue) >= 2:
            current_year_revenue = total_revenue.iloc[0]
            previous_year_revenue = total_revenue.iloc[1]
            if previous_year_revenue != 0:
                growth_rate = (current_year_revenue - previous_year_revenue) / previous_year_revenue
                return growth_rate
        return None
    except (KeyError, IndexError):
        return None

def calculate_eps_growth_rate(stock_data):
    """
    Calculates the Year-over-Year EPS Growth Rate.
    """
    try:
        eps = stock_data["financials"].loc["Diluted EPS"]
        if len(eps) >= 2:
            current_year_eps = eps.iloc[0]
            previous_year_eps = eps.iloc[1]
            if previous_year_eps != 0:
                growth_rate = (current_year_eps - previous_year_eps) / previous_year_eps
                return growth_rate
        return None
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
        "interest_coverage_ratio": calculate_interest_coverage_ratio(stock_data),
        "debt_to_capital_ratio": calculate_debt_to_capital_ratio(stock_data),
        "roic": calculate_roic(stock_data),
        "altman_z_score": calculate_altman_z_score(stock_data),
        "peg_ratio": calculate_peg_ratio(stock_data),
        "ev_to_sales": calculate_ev_to_sales(stock_data),
        "fcf_yield": calculate_fcf_yield(stock_data),
        "gross_profit_margin": calculate_gross_profit_margin(stock_data),
        "operating_profit_margin": calculate_operating_profit_margin(stock_data),
        "net_profit_margin": calculate_net_profit_margin(stock_data),
        "roe": calculate_roe(stock_data),
        "roa": calculate_roa(stock_data),
        "asset_turnover": calculate_asset_turnover(stock_data),
        "revenue_growth_rate": calculate_revenue_growth_rate(stock_data),
        "eps_growth_rate": calculate_eps_growth_rate(stock_data),
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
