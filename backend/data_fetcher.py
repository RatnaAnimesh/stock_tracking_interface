
import yfinance as yf

def get_stock_data(ticker):
    """
    Fetches stock data for a given ticker using yfinance.
    """
    stock = yf.Ticker(ticker)
    
    # Get stock info
    info = stock.info
    
    # Get historical market data
    hist = stock.history(period="10y")
    
    # Get financial statements
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow
    
    # Get ownership data
    major_holders = stock.major_holders
    institutional_holders = stock.institutional_holders
    # insider_transactions = stock.insider_transactions
    # Get news
    news = stock.news
    # Get future growth data
    recommendations = stock.recommendations
    earnings_dates = stock.earnings_dates
    
    return {
        "info": info,
        "history": hist,
        "financials": financials,
        "balance_sheet": balance_sheet,
        "cashflow": cashflow,
        "major_holders": major_holders,
        "institutional_holders": institutional_holders,
#        "insider_transactions": insider_transactions,
        "news": news,
        "recommendations": recommendations,
        "earnings_dates": earnings_dates,
    }

if __name__ == '__main__':
    # Example usage
    ticker = "MSFT"
    data = get_stock_data(ticker)
    
    # Print some data to verify
    print(f"Successfully fetched data for {ticker}")
    print("Info:", data["info"]["longName"])
    print("History data points:", len(data["history"]))
    print("Financials columns:", data["financials"].shape)
    print("Balance Sheet columns:", data["balance_sheet"].shape)
    print("Cashflow columns:", data["cashflow"].shape)
