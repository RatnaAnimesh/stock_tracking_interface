
from fastapi import FastAPI
from financial_analyzer import analyze_stock
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow cross-origin requests from the frontend
origins = [
    "http://localhost:3000",  # React default port
    "http://localhost:5173",  # Vite default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze/{ticker}")
async def get_analysis(ticker: str):
    """
    Returns a financial analysis of the given stock ticker.
    """
    analysis = analyze_stock(ticker)
    return analysis
