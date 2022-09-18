import pandas as pd


def load_pop(location="datasets/world_population.csv"):
    """
    Load the data into a pandas dataframe
    """
    return pd.read_csv(location)


def pandas_country_pop(location="datasets/world_population.csv", country = 'United States'):
    """
    Display the population of country selected

    print and returns a single email record from the enron dataset
    """

    data = pd.read_csv(location)
    country_pops = data.loc[data['Country'] == country]
    pop_cols = ['1970 Population',
        '1980 Population', '1990 Population', '2000 Population',
        '2010 Population', '2015 Population', '2020 Population',
        '2022 Population']

    return country_pops[pop_cols]
