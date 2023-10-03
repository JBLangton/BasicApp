#tests / conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.database import Base
import sys
sys.path.append(r"/")

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./backend/test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def clear_data():
    for table in reversed(Base.metadata.sorted_tables):
        engine.execute(table.delete())
    yield