import { useState } from 'react';
import './App.css';
import PastPerformanceChart from './PastPerformanceChart';
import EconomyChart from './EconomyChart';

function App() {
  const [ticker, setTicker] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('Valuation');

  const handleAnalyze = async () => {
    if (!ticker) {
      alert('Please enter a stock ticker.');
      return;
    }
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/analyze/${ticker}`);
      if (!response.ok) {
        throw new Error('Stock not found or API error');
      }
      const data = await response.json();
      setAnalysis(data);
    } catch (error) {
      console.error('Error fetching analysis:', error);
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Personal Stock Analyzer</h1>
        <div className="input-container">
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            placeholder="Enter stock ticker (e.g., AAPL)"
          />
          <button onClick={handleAnalyze} disabled={loading}>
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>
      </header>
      {analysis && (
        <>
          <div className="analysis-container">
            <h2>{analysis.info.longName} ({analysis.ticker})</h2>

            <div className="tabs">
              <button className={activeTab === 'Valuation' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Valuation')}>Valuation</button>
              <button className={activeTab === 'Financial Health' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Financial Health')}>Financial Health</button>
              <button className={activeTab === 'Past Performance' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Past Performance')}>Past Performance</button>
              <button className={activeTab === 'Future Growth' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Future Growth')}>Future Growth</button>
              <button className={activeTab === 'Dividends' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Dividends')}>Dividends</button>
              <button className={activeTab === 'Management' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Management')}>Management</button>
              <button className={activeTab === 'Ownership' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Ownership')}>Ownership</button>
              <button className={activeTab === 'News' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('News')}>News</button>
              <button className={activeTab === 'Economy' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Economy')}>Economy</button>
              <button className={activeTab === 'Other Information' ? 'tab-button active' : 'tab-button'} onClick={() => setActiveTab('Other Information')}>Other Information</button>
            </div>

            <div className="tab-content">
              {activeTab === 'Valuation' && (
                <div>
                  <p><i>Note: High P/E and P/B ratios can sometimes be justified for companies with strong growth prospects and competitive advantages. Consider the Future Growth section for more context.</i></p>
                <div className="metrics-grid">
                  <div className="metric">
                    <h3>P/E Ratio</h3>
                    <p>{analysis.pe_ratio ? analysis.pe_ratio.toFixed(2) : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>P/B Ratio</h3>
                    <p>{analysis.pb_ratio ? analysis.pb_ratio.toFixed(2) : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>P/S Ratio</h3>
                    <p>{analysis.ps_ratio ? analysis.ps_ratio.toFixed(2) : 'N/A'}</p>
                  </div>
                  <div className="metric">
                                      <h3>EV/EBITDA</h3>
                                      <p>{analysis.ev_to_ebitda ? analysis.ev_to_ebitda.toFixed(2) : 'N/A'}</p>
                                    </div>
                                    <div className="metric">
                                      <h3>PEG Ratio</h3>
                                      <p>{analysis.peg_ratio ? analysis.peg_ratio.toFixed(2) : 'N/A'}</p>
                                    </div>
                                    <div className="metric">
                                      <h3>EV/Sales</h3>
                                      <p>{analysis.ev_to_sales ? analysis.ev_to_sales.toFixed(2) : 'N/A'}</p>
                                    </div>
                                    <div className="metric">
                                      <h3>FCF Yield</h3>
                                      <p>{analysis.fcf_yield ? (analysis.fcf_yield * 100).toFixed(2) + '%' : 'N/A'}</p>
                                    </div>
                                  </div>              )}
              {activeTab === 'Financial Health' && (
                <div className="metrics-grid">
                  <div className="metric">
                    <h3>D/E Ratio</h3>
                    <p>{analysis.de_ratio ? analysis.de_ratio.toFixed(2) : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>Current Ratio</h3>
                    <p>{analysis.current_ratio ? analysis.current_ratio.toFixed(2) : 'N/A'}</p>
                  </div>
                                  <div className="metric">
                                    <h3>Quick Ratio</h3>
                                    <p>{analysis.quick_ratio ? analysis.quick_ratio.toFixed(2) : 'N/A'}</p>
                                  </div>
                                  <div className="metric">
                                    <h3>Interest Coverage Ratio</h3>
                                    <p>{analysis.interest_coverage_ratio ? analysis.interest_coverage_ratio.toFixed(2) : 'N/A'}</p>
                                  </div>
                                  <div className="metric">
                                    <h3>Debt to Capital Ratio</h3>
                                    <p>{analysis.debt_to_capital_ratio ? analysis.debt_to_capital_ratio.toFixed(2) : 'N/A'}</p>
                                  </div>
                                  <div className="metric">
                                    <h3>ROIC</h3>
                                    <p>{analysis.roic ? (analysis.roic * 100).toFixed(2) + '%' : 'N/A'}</p>
                                  </div>
                                  <div className="metric">
                                    <h3>Altman Z-Score</h3>
                                    <p>{analysis.altman_z_score ? analysis.altman_z_score.toFixed(2) : 'N/A'}</p>
                                  </div>
                                </div>              )}
              {activeTab === 'Past Performance' && (
                <div>
                  <h3>Profitability & Efficiency</h3>
                  <div className="metrics-grid">
                    <div className="metric">
                      <h3>Gross Profit Margin</h3>
                      <p>{analysis.gross_profit_margin ? (analysis.gross_profit_margin * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>Operating Profit Margin</h3>
                      <p>{analysis.operating_profit_margin ? (analysis.operating_profit_margin * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>Net Profit Margin</h3>
                      <p>{analysis.net_profit_margin ? (analysis.net_profit_margin * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>ROE</h3>
                      <p>{analysis.roe ? (analysis.roe * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>ROA</h3>
                      <p>{analysis.roa ? (analysis.roa * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>Asset Turnover</h3>
                      <p>{analysis.asset_turnover ? analysis.asset_turnover.toFixed(2) : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>Revenue Growth (YoY)</h3>
                      <p>{analysis.revenue_growth_rate ? (analysis.revenue_growth_rate * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                    <div className="metric">
                      <h3>EPS Growth (YoY)</h3>
                      <p>{analysis.eps_growth_rate ? (analysis.eps_growth_rate * 100).toFixed(2) + '%' : 'N/A'}</p>
                    </div>
                  </div>
                  <h3 style={{ marginTop: '2rem' }}>Historical Trends</h3>
                  {analysis.historical_revenue && analysis.historical_net_income && (
                    <PastPerformanceChart 
                      revenueData={analysis.historical_revenue} 
                      netIncomeData={analysis.historical_net_income} 
                    />
                  )}
                </div>
              )}
              {activeTab === 'Dividends' && (
                <div className="metrics-grid">
                  <div className="metric">
                    <h3>Dividend Yield</h3>
                    <p>{analysis.dividend_yield ? (analysis.dividend_yield * 100).toFixed(2) + '%' : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>Dividend Rate</h3>
                    <p>{analysis.dividend_rate ? analysis.dividend_rate : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>Payout Ratio</h3>
                    <p>{analysis.payout_ratio ? (analysis.payout_ratio * 100).toFixed(2) + '%' : 'N/A'}</p>
                  </div>
                  <div className="metric">
                    <h3>Ex-Dividend Date</h3>
                    <p>{analysis.ex_dividend_date ? new Date(analysis.ex_dividend_date * 1000).toLocaleDateString() : 'N/A'}</p>
                  </div>
                </div>
              )}

              {activeTab === 'Future Growth' && (
                <div>
                  <h3>Growth Outlook</h3>
                  {analysis.recommendations && analysis.recommendations.length > 0 ? (
                    <p>Based on recent analyst recommendations, the sentiment for {analysis.ticker} is generally {analysis.recommendations[0]['To Grade']}.</p>
                  ) : (
                    <p>No recent analyst recommendations available.</p>
                  )}
                  {analysis.earnings_dates && analysis.earnings_dates.length > 0 ? (
                    <p>The company has upcoming earnings announcements, which are key indicators for future performance.</p>
                  ) : (
                    <p>No upcoming earnings announcements available.</p>
                  )}
                  <h3>Analyst Recommendations</h3>
                  <h3 style={{ marginTop: '2rem' }}>Earnings Dates</h3>
                  {analysis.earnings_dates && (
                    <table>
                      <thead>
                        <tr>
                          <th>Date</th>
                          <th>EPS Estimate</th>
                          <th>Reported EPS</th>
                          <th>Surprise</th>
                        </tr>
                      </thead>
                      <tbody>
                        {Object.entries(analysis.earnings_dates).map(([date, earnings]) => (
                          <tr key={date}>
                            <td>{date}</td>
                            <td>{earnings['EPS Estimate']}</td>
                            <td>{earnings['Reported EPS']}</td>
                            <td>{earnings['Surprise']}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  )}
                </div>
              )}
              {activeTab === 'Management' && (
                <div>
                  <h3>Company Officers</h3>
                  {analysis.company_officers && analysis.company_officers.length > 0 ? (
                    <table>
                      <thead>
                        <tr>
                          <th>Name</th>
                          <th>Title</th>
                          <th>Age</th>
                          <th>Year Born</th>
                        </tr>
                      </thead>
                      <tbody>
                        {analysis.company_officers.map((officer, index) => (
                          <tr key={index}>
                            <td>{officer.name}</td>
                            <td>{officer.title}</td>
                            <td>{officer.age || 'N/A'}</td>
                            <td>{officer.yearBorn || 'N/A'}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  ) : (
                    <p>No company officer information available from yfinance.</p>
                  )}
                </div>
              )}
              {activeTab === 'News' && (
                <div className="news-container">
                  <h3>Recent News</h3>
                  {analysis.news && analysis.news.map((article, index) => (
                    <div key={index} className="news-article">
                      <h4><a href={article.link} target="_blank" rel="noopener noreferrer">{article.title}</a></h4>
                      <p>{article.publisher}</p>
                    </div>
                  ))}
                </div>
              )}
              {activeTab === 'Economy' && (
                <div>
                  {analysis.fred_data && (
                    <EconomyChart fredData={analysis.fred_data} />
                  )}
                </div>
              )}
              {activeTab === 'Other Information' && (
                <div className="other-info-container">
                  <h3>Company Profile</h3>
                  <p><strong>Sector:</strong> {analysis.info.sector || 'N/A'}</p>
                  <p><strong>Industry:</strong> {analysis.info.industry || 'N/A'}</p>
                  <p><strong>Website:</strong> <a href={analysis.info.website} target="_blank" rel="noopener noreferrer">{analysis.info.website || 'N/A'}</a></p>
                  <p><strong>Address:</strong> {analysis.info.address1 || 'N/A'}, {analysis.info.city || 'N/A'}, {analysis.info.state || 'N/A'} {analysis.info.zip || 'N/A'}, {analysis.info.country || 'N/A'}</p>
                  <p><strong>Full Time Employees:</strong> {analysis.info.fullTimeEmployees || 'N/A'}</p>
                  <h4>Company Description</h4>
                  <p>{analysis.info.longBusinessSummary || 'N/A'}</p>
                </div>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
