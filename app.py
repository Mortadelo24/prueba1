# python -m venv env //crear un entorno
# inclopeto la activacion del entorno


import os
from sqlalchemy import create_engine, text
from sqlalchemy.org import sessionmaker, scoped_session
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("")