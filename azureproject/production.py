import os
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
if not conn_str:
    raise KeyError('AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is not set')

logger.info('AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is set: %s', conn_str)

# Parse the connection string as a URL
parsed_url = urlparse(conn_str)
logger.info('Parsed connection string components: %s', parsed_url)

# Log individual components of the parsed connection string for debugging
logger.info('Username: %s', parsed_url.username)
logger.info('Password: %s', parsed_url.password)
logger.info('Hostname: %s', parsed_url.hostname)
logger.info('Database name: %s', parsed_url.path[1:])  # Remove leading '/' from path

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=parsed_url.username,
    dbpass=parsed_url.password,
    dbhost=parsed_url.hostname,
    dbname=parsed_url.path[1:]  # Remove leading '/' from path
)
logger.info('DATABASE_URI: %s', DATABASE_URI)
