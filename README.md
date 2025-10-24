# Personal Stock Analyzer

This project is a personal stock analysis tool that provides a comprehensive overview of a company's financial health, valuation, growth prospects, and other relevant information. It features a FastAPI backend for data processing and a React frontend for an interactive user interface.

## Features

- **Valuation:** Price-to-Earnings (P/E), Price-to-Book (P/B), Price-to-Sales (P/S), Enterprise Value to EBITDA (EV/EBITDA) ratios.
- **Financial Health:** Debt-to-Equity (D/E), Current Ratio, Quick Ratio.
- **Past Performance:** Historical Revenue and Net Income charts.
- **Future Growth:** Analyst recommendations and earnings dates.
- **Dividends:** Dividend Yield, Dividend Rate, Payout Ratio, Ex-Dividend Date.
- **Management:** Basic company officer information.
- **Ownership:** (Currently commented out, but planned for detailed insider transaction data from OpenInsider).
- **News:** Recent news articles related to the stock.
- **Economy:** Macroeconomic indicators from FRED (GDP, CPI, Fed Funds Rate).
- **Other Information:** General company details like sector, industry, website, address, and employee count.

## Technologies Used

**Backend (Python):**
- FastAPI
- Uvicorn
- yfinance
- fredapi
- requests
- beautifulsoup4
- lxml

**Frontend (JavaScript/React):**
- React
- Vite
- Chart.js (with react-chartjs-2)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RatnaAnimesh/stock_tracking_interface.git
cd stock_tracking_interface
```

### 2. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Get a FRED API Key:**
    - Go to [https://fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) and create a free API key.
    - Open `backend/financial_analyzer.py` and replace `"api-key"` with your actual FRED API key.

### 3. Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```
2.  **Install JavaScript dependencies:**
    ```bash
    npm install
    ```

## How to Run the Application

1.  **Start the Backend Server:**
    Open a new terminal, navigate to the `backend` directory, and run:
    ```bash
    cd personal_stock_analyzer/backend
    uvicorn main:app --reload
    ```
    The backend will run on `http://localhost:8000`.

2.  **Start the Frontend Development Server:**
    Open another new terminal, navigate to the `frontend` directory, and run:
    ```bash
    cd personal_stock_analyzer/frontend
    npm run dev
    ```
    The frontend will typically open in your browser at `http://localhost:5173`.

## Future Enhancements

- Implement detailed insider trading and management information by robustly scraping SEC EDGAR filings.
- Add more advanced valuation models and financial metrics.
- Improve UI/UX with more interactive charts and a more polished design.
- Implement user authentication and portfolio tracking.
_- create a professional, state of the art app for personal use, and most importantly make it free__
