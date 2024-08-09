from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        #Url to the github repo
        source="https://github.com/wtsu/prefect-practice.git",

        #name of the python file and the function to run
        entrypoint="rick_and_morty.py:run_rick_and_morty",
    ).deploy(
        #name of the deployment
        name="rick_and_morty",

        #name of the workpool to use
        work_pool_name="managed1",
    )
