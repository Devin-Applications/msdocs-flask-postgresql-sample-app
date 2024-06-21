import os
from urllib.parse import urlparse, parse_qs

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
if not conn_str:
    raise KeyError('AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is not set')

# Log the connection string for debugging purposes
print(f"Connection string: {conn_str}")

# Parse the connection string as a DSN (Data Source Name)
conn_str_params = parse_qs(conn_str.replace(';', '&'))

# Log the parsed connection string parameters for debugging purposes
print(f"Parsed connection string parameters: {conn_str_params}")

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['User Id'][0],
    dbpass=conn_str_params['Password'][0],
    dbhost=conn_str_params['Server'][0],
    dbname=conn_str_params['Database'][0]
)
