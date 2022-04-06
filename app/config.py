import os

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]

DB = {
    'host': os.environ.get('POSTGRES_HOST', 'db'),
    'port': os.environ.get('POSTGRES_POST', '5432'),
    'db': os.environ.get('POSTGRES_DB', 'dfa'),
    'user': os.environ.get('POSTGRES_USER', 'dfa'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'password')
}