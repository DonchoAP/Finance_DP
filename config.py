<<<<<<< HEAD
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/financeapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/financeapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 69ae552e20184609c2863a8576937c506af29c90
