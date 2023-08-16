# config.py
import logging
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
#logging.basicConfig(filename='app.log', level=logging.INFO)

if ENVIRONMENT == "testing":
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    logging.info("Loaded testing environment configuration.")
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./main.db")
    logging.info("Loaded development environment configuration.")
