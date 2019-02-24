# Sentiment Report - report.py 
from assets import security_info as security
import chartify

# Main func 
def main():

    # Prompt for ticker
    ticker = input('\nEnter a ticker symbol (e.g: AMZN): ')
    print('\nGenerating Report...')

    # Create obj for ticker
    securityObj = security.Security(ticker)

    # Create chartify graph one
    ch1 = chartify.Chart()
    ch1.set_title(securityObj.name)
    ch1.set_subtitle('Report for '+securityObj.getTicker()+' | Price: '+securityObj.getPrice())

    # Display charts
    # Chromedriver installation
    try:
        ch1.show('png')
        print('Success!')
    
    # Check if being run in Anaconda
    except:
        try:
            ch1.show()
            print('Success!')
        
        # None of above
        except:
            print('You do not have Chromedriver installed correctly. Please reference README.md.\nAlternatively, run program using Anaconda')
            exit()

if __name__ == "__main__":
    main()