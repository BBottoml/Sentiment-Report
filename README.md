# Sentiment Report

Twitter & Stocktwits report generator using Chartify. Works by taking a ticker symbol input and parsing social media sites to determine the sentiment of a security. The program then generates a report using the Spotify developed data science library, Chartify. 

## Getting Started

To view the report, you will need to either have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) installed and in a directory within your PATH or run the program using Anaconda. See the [Chartify Repo](https://github.com/spotify/chartify) for more details 

### Installation

To start, clone this repo

```
git clone git@github.com:BBottoml/Sentiment-Report.git
```

After cloning, create a virtual environment 

```
virtualenv some-proj
source some-proj/bin/activate
```

Install reqs
```
pip3 install requirements.txt
```

## Running the program

Ensure correct installation of ChromeDriver or alternate option

```
python3 main.py
```

### Example 

See an example [Here](https://bradleybottomlee.com) (Coming Soon)

## Authors

**Bradley Bottomlee** - [BBottoml](https://github.com/BBottoml)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to Chartify devs 
* Sentiment analysis providers
