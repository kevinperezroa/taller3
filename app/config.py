class Config:
    SECRET_KEY = 'clave secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/crud'
    SQLALCHEMY_TRACK_MODIFICATIONS = False