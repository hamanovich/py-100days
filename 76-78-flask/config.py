import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any-secret-key-code'