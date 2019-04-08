import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or f'postgresql+psycopg2://KPI:bO36k73G@db:5432/kpi_test' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
