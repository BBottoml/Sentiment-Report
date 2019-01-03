# Sentiment Report - security_info.py
import pytwits

# Create class security (security is ticker)
class Security:
    
    # Initalizer
    def __init__(self, ticker,name=None):
        
        self.ticker = ticker
    
        # Retrieve company name using Stocktwit api
        try:
        
            stocktwits = pytwits.StockTwits(access_token=None) 
            symbols = stocktwits.search(path='search/symbols',
                                    q=self.ticker)
            info = symbols[0]
            self.name = info.title

        # Ticker doesn't exist
        except:

            print('Please enter a valid ticker symbol')
            exit()    


        

