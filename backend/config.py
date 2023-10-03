# config.py
import logging
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "testing":
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend/test.db")
    logging.info("Loaded testing environment configuration.")
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend/main.db")
    logging.info("Loaded development environment configuration.")
