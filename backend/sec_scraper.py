import requests
from bs4 import BeautifulSoup

def get_openinsider_data(ticker):
    """
    Scrapes the OpenInsider page for a given stock ticker.
    """
    url = f"http://openinsider.com/search?q={ticker}"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Find the insider trading table
        table = soup.find('table', {'class': 'tinytable'})
        if not table:
            return []
            
        # Extract the table headers
        headers = [th.text.strip() for th in table.find_all('th')]
        
        # Extract the table rows
        rows = []
        for tr in table.find_all('tr')[1:]: # Skip the header row
            cells = [td.text.strip() for td in tr.find_all('td')]
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
                
        return rows
        
    except requests.exceptions.RequestException as e:
        print(f"Error scraping OpenInsider: {e}")
        return None

if __name__ == '__main__':
    # Example usage
    ticker = "AAPL"
    data = get_openinsider_data(ticker)
    if data:
        print(f"Successfully scraped OpenInsider for {ticker}")
        print(data[:5]) # Print the first 5 transactions