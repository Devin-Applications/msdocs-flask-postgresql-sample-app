import os

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DATABASE_USER'],
    dbpass=os.environ['DATABASE_PASSWORD'],
    dbhost=os.environ['DATABASE_HOST'],
    dbname=os.environ['DATABASE_NAME']
)
