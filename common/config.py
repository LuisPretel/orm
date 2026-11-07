from sqlalchemy.engine import URL


class Config:
    USER = 'root'
    PASSWORD = 'Root#23'  
    HOST = 'localhost'
    DATABASE = 'db_products'
    SQLALCHEMY_DATABASE_URI = URL.create(
        'mysql+pymysql',
        username=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False