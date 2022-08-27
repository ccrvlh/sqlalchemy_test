A simple test to try to replicate a situation in which ocasionally inserts are not persisted.
This will use Poetry (I'm running on Python 3.10.3)

1. Setup venv `poetry shell`
2. Install deps `poetry install`
3. Run application `make run`
4. Drop / Create / Initialize data with `make all`

When running for the very first time, everything should work.
But when running `make all` at any give moment with the application running, the `Accounts` table and related won't be filled.
If the application is restarted and then run `make all` again, it works.
Maybe there something wrong with the code itself, couldn't really find what may be wrong.
If (big if) the code is sane, then there might be an issue with cache management or maybe with async/await logic?
