from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/wtsu/prefect-practice.git",
        entrypoint="rick_and_morty.py:run_rick_and_morty",
    ).deploy(
        name="rick_and_morty",
        work_pool_name="managed1",
    )
