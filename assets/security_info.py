# Sentiment Report - security_info.py
import pytwits

# Create obj for given security (security is ticker input)
class Security:
    
    # Initalizer
    def __init__(self, ticker,name=None):
        
        self.ticker = ticker
    
        # Retrieve company name using Stocktwits api
        try:
        
            stocktwits = pytwits.StockTwits(access_token=None) 
            info = stocktwits.search(path='search/symbols',
                                    q=self.ticker)
            self.name = info[0].title

        # Ticker doesn't exist
        except:

            print('Please enter a valid ticker symbol')
            exit()    


        

