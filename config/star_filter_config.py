try:
    import json
    import psycopg2
    from flask import Flask, request
    from flask_restful import Api
    from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.pool import NullPool
    from flask import jsonify
    from datetime import date
    from datetime import timedelta
    import os
    import logging as log
    log.basicConfig(level = log.DEBUG)
except Exception as er:
    log.info("Install Missing Libraries", er)
app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
