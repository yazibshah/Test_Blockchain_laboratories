import os

class Config:
    SECRET_KEY = 'ssmK4zPXRNaHfZr4cMLjXcgCMg84U'
    MONGODB_SETTINGS = {
        'db': 'payment_processor',
        'host': 'mongodb://localhost/payment_processor'
    }
