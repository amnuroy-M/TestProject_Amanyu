from pydantic import BaseSettings


class settings(BaseSettings):
    DB_HOST=localhost
    DB_PORT=5432
    DB_DATABASE=testdb
    DB_USERNAME=postgres
    DB_PASSWORD=postgres
    DB_URL= postgresql+psycopg2://postgres:postgres@localhost:5432/devbud-be