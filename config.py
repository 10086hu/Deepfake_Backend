import secrets

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:HjH20040229@127.0.0.1:3306/deepfake'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = secrets.token_hex(32)
