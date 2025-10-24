
from fredapi import Fred

# The user's FRED API key is stored in memory
# I will retrieve it from memory when needed.

def get_fred_data(api_key):
    """
    Fetches key macroeconomic data from the FRED API.
    """
    fred = Fred(api_key=api_key)
    
    gdp = fred.get_series('GDP', observation_start='2020-01-01')
    cpi = fred.get_series('CPIAUCSL', observation_start='2020-01-01')
    fed_funds = fred.get_series('FEDFUNDS', observation_start='2020-01-01')
    
    return {
        "gdp": gdp.to_dict(),
        "cpi": cpi.to_dict(),
        "fed_funds": fed_funds.to_dict(),
    }

if __name__ == '__main__':
    # Example usage
    # I will need to get the API key from memory to run this
    # For now, I will just print a success message
    print("fred_data.py created successfully")
