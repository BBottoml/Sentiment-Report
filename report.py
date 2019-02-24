'''
This program accepts a stock "ticker" symbol as a user input
and generates a sentiment report for the given security 
using the Spotify-developed Python data science library, Chartify. 
Various code sources have been used to enhance and enable
certain functionality. See Github repo for full acknowledgements.
This program will only run using Python 3. 
-BBottoml
'''
# Sentiment Report -- report.py

from assets import security_info as security
import chartify

# Main func
def main():

    # Prompt for ticker
    ticker = input('\nEnter a ticker symbol (e.g: AMZN): ')

    # Create obj for ticker & generate data
    securityObj = security.Security(ticker)
    securityObj.dataGen()
    print('\nGenerating Report...')

    # Create chartify graph one
    ch1 = chartify.Chart()
    ch1.set_title(securityObj.getName())
    ch1.set_subtitle('Report for '+securityObj.getTicker() +
                     ' | Price: '+securityObj.getPrice())

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