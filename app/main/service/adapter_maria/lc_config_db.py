import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
sys.path.insert(1, root_dir)
print(root_dir)

from config_maria import user_name_mariadb_lc_db, password_mariadb_lc_db, \
    database_mariadb_lc_db, host_mariadb_lc_db

url_database = 'mysql+mysqldb://{username}:{password}@{host}/{database}?charset=utf8'.format(
    username=user_name_mariadb_lc_db, password=password_mariadb_lc_db, host=host_mariadb_lc_db,
    database=database_mariadb_lc_db)



if not database_exists(url_database):
    create_database(url_database)
engine_lc_config = create_engine(url_database, pool_size=20, max_overflow=0,echo=True)
Session_lc_config = sessionmaker(bind=engine_lc_config)
Base_lc_config = declarative_base()

