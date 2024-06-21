import os
from urllib.parse import urlparse

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
if not conn_str:
    raise KeyError('AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is not set')

# Parse the connection string as a URL
parsed_url = urlparse(conn_str)

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=parsed_url.username,
    dbpass=parsed_url.password,
    dbhost=parsed_url.hostname,
    dbname=parsed_url.path[1:]  # Remove leading '/' from path
)
