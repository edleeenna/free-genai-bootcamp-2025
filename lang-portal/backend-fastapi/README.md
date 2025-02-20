# Backend FastAPI

This is the backend service for the Free GenAI Bootcamp 2025 project, built using FastAPI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation
Initialize a new FastAPI project.
Create a virtual environment and install dependencies:

```sh
python3 -m venv env
source env/bin/activate
pip install fastapi uvicorn sqlalchemy sqlite3
```

## Usage

1. Start the FastAPI server, running from the backend-fastapi folder:
    ```bash
    uvicorn app.main:app --reload
    ```
2. The API will be available at `http://127.0.0.1:8000`.
3. Run migration script
    ```sh
    python3 -m db.migrations.0001_create_tables
    ```
4. Seed the database
    ```sh
    python3 -m db.seeds.seed

    ```

## Testing
To run tests use the following command. This ensures that we are using the test.db and not the production words.db

```sh
TESTING=1 pytest    
```

If testing a route that includes pagination in browser use the following as an example of how to structure request

localhost:8000/groups/?page=2&items_per_page=10

## Issues
