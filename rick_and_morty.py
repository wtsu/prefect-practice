import httpx 
import pandas as pd
from prefect import flow, task

@task()
def get_all_rick_and_morty_characters():
    #Get All Rick and Morty Characters from the Rick and Morty Character API
    dataframes = []
    url = 'https://rickandmortyapi.com/api/character'
    
    #paging thru the api endpoint and then combining all json payloads into one tabular dataframe
    response = httpx.get(url)
    data = response.json()
    
    while url:
        response = httpx.get(url)
        data = response.json()
        for character in data['results']:
            df = pd.DataFrame([character])
            dataframes.append(df)
        url = data['info']['next']
    df = pd.concat(dataframes)

    return df


@task()
def count_by_species(df):
    #Count the number of characters by species
    result = df.groupby('species').size()
    return result

@task(log_prints=True)
def log_results(df):
    #Print the results in logs
    print(df)

@flow()
def run_rick_and_morty():
    characters = get_all_rick_and_morty_characters()
    result = count_by_species(characters)
    log_results(result)
