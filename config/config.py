class Config:
    SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'


class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/rent_api'
    DEBUG = True
    JWT_SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres://jdgctpmrllsaxg:e5485bb793e81a48acd25924ed4ccf3b1eaf9f6fe71a2e49d1cfe8e41b1bf096@ec2-18-232-143-90.compute-1.amazonaws.com:5432/dbtjilo4d8b0ir'
    JWT_SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'

    DEBUG = False