import os

DBHOST = os.getenv('DBHOST')
DBUSERNAME = os.getenv('DBUSERNAME')
DBPASSWORD = os.getenv('DBPASSWORD')
DB = os.getenv('DB')

DB_SETUP = {
    "local": {
        "username": DBUSERNAME,
        "password": DBPASSWORD,
        "host": DBHOST,
        'database': DB
    }
}
