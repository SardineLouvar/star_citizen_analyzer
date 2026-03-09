# Star Citizen Analyzer

This is program which can be used to access the UEX API, which is a marketplace for the game "Star Citizen". The website monitors things like commodities, ships and planets.

The documentation for the API can be found here: https://uexcorp.space/api/documentation/

Python 3.13.5

To run : 
```
py -m venv venv
venv\scripts\activate
pip install -r requirements.txt

py -m src.main
py -m src.analysis.for_data.commodities_prices_all
```