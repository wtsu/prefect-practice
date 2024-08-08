import httpx 
import pandas as pd
from prefect import flow, task

@flow(log_prints=True)
def get_all_rick_and_morty_characters() -> None:
    dataframes = []

    #paging thru the api endpoint and then combining all json payloads into one tabular dataframe
    response = httpx.get('https://rickandmortyapi.com/api/character')
    data = response.json()
    
    while url:
        response = httpx.get(url)
        data = response.json()
        for character in data['results']:
            df = pd.DataFrame([character])
            dataframes.append(df)
        url = data['info']['next']
    df = pd.concat(dataframes)

    #dont' have access to a database to write to, so just pretend this print does that
    print(df)
