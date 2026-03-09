# Star Citizen Analyzer

This program can be used to access the UEX API, which is a marketplace for the game "Star Citizen". The website monitors things like commodities, ships and planets.

The data from the API is saved as a JSON and uploaded to a database, of which either can be viewed. The database can be found under 'data/databases/' if you would like to use SQL queries directly for simple checks.

After downloading the data, a python file is created under 'src/analysis/for_data/' corresponding to either the name of the resource used or the commodity. These are made for customisable analysis for each resource or commodity, such as by using the build in plotting functions inside of 'src/analysis/plotting'. 

The documentation for the API can be found here: https://uexcorp.space/api/documentation/

This program was designed for Windows 11 and Python 3.13.5.


## How to use

1. First it is required to make an account in order to generate an API key. The key can be found under account -> apps. Running the program without an API key will result in nothing happening. If you want to test the code without signing up, **skip step 3** and run the following code in place of step 4:
`python -m cmd.test_program` 

2. Open a terminal, ensuring that you are in the root directory of the project.
```
cd {path_to_program}
```

The program can then be set up by using the following commands in the terminal:
```
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

This sets up a virtual environment and downloads all of the required dependencies.

3. Set up the config.yaml file for your needs. The important aspects are as follows:
```
api_token : "paste your API key in here!"
```

Add the name of the resources to be found in the list below. An example is included.
```
# Resources specified in the UEX API 2.0 documentation
resources:
  - commodities_prices_all 
  - cities
```

To get the history of a specific commodity, add them into the "id_searches" field like follows. This example gets data for aluminium and gasping weavil eggs.
```
# [commodity_id, terminal_id] pairs to fetch history for
id_searches:
  - [5, 12]
  - [32, 16]
```

4. Run the main file using the following command. This downloads the desired data from the API, adds the data to the database, sets up any required folders and generates a python file under 'src/analysis/for_data' which can be used for plotting.
`python -m src.main`

5. The produced analysis files can then be run using an example similar to the following. I have kept an example file called `commodities_prices_all.py` that you can run to view a bar chart comparing every commodity's price.
`python -m src.analysis.for_data.commodities_prices_all`