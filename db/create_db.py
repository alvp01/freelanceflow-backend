import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from core.config import settings

# Example for PostgreSQL
def create_database_script():
    # Use the full database URL from settings
    dev_url = settings.DEV_DATABASE_URL

    # Create an SQLAlchemy engine
    engine = create_engine(dev_url)

    # Check if the database exists; if not, create it
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Database created: {engine.url}")
    else:
        print(f"Database already exists: {engine.url}")

if __name__ == "__main__":
    create_database_script()