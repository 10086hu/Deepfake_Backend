class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/deepfake'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret key"
