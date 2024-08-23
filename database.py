import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus


load_dotenv()
database_url = os.getenv("database_url")
engine = create_engine(database_url)
# What is an sqlalchemy engine?
# The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend. An engine is a factory for connecting object. It encapsulate a connection pool that minimizes the cost of connecting to the database by reusing existing connection and provides a consistent API for working with transaction.

metadata = MetaData()
sessionloacl = sessionmaker(autocommit=False,autoflush=False,bind = engine)

base = declarative_base()
