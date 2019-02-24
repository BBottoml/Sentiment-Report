# Sentiment Report - security_info.py
import pytwits
from finviz.screener import Screener

# Create obj for given security (security is ticker input)
class Security:
    
    # Initalizer
    def __init__(self,ticker,name=None,price=None):
        
        self.ticker = ticker.upper()
    
        # Retrieve company name using Stocktwits api 
        try:
        
            stocktwits = pytwits.StockTwits(access_token=None) 
            info = stocktwits.search(path='search/symbols',
                                    q=self.ticker)
            self.name = info[0].title

            # Retrieve some data (price, etc.) using finviz
            # Price 
            stock_data = Screener(tickers=[self.ticker])
            self.price = stock_data[0]['Price']

            # Other data

        # Ticker doesn't exist
        except:

            print('Please enter a valid ticker symbol')
            exit()    
    
    # getTicker()
    def getTicker(self):
        return self.ticker
    
    # getTicker() 
    def getPrice(self):
        return self.price
        

        

