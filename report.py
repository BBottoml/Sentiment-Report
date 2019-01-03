# Sentiment Report - report.py 
from assets import security_info as se
import chartify

# Main func 
def main():

    # Prompt for ticker
    ticker = input('Enter a ticket symbol (e.g: AMZN): ')

    # Create obj for ticker
    security_obj = se.Security(ticker)

    # Create chartify graph one
    ch1 = chartify.Chart()
    ch1.set_title(security_obj.name)
    ch1.set_subtitle('Chart for '+security_obj.ticker)

    # Display charts
    # Chromedriver installation
    try:
        ch1.show('png')
    
    # Check if being run in Anaconda
    except:
        
        # Anaconda
        try:
            ch1.show()
        
        # None of above
        except:
            print('You do not have Chromedriver installed correctly. Please reference README.md.\nAlternatively, run program using Anaconda')
            exit()

if __name__ == "__main__":
    main()