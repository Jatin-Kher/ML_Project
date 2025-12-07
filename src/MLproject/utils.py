import os 
import sys 
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("Establishing connection to the database")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info(f"Connection established successfully: {mydb}")

        df=pd.read_sql_query("SELECT * FROM students",mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)