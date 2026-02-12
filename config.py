import os

class Config:
    SECRET_KEY = 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flowtasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False