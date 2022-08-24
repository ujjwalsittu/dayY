from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sql_address= 'mysql+pymysql://root:@localhost:3306/mydb'
sql_address= 'sqflite:///./user.db'
engine = create_engine(sql_address)

Session = sessionmaker(bind=engine)


Base = declarative_base()