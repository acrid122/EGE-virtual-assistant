import pytest
from sqlalchemy import create_engine, text

def test_db_connection():
    engine = create_engine("postgresql://ege:1357913579QqPp@db:5432/ege_assistant")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).fetchone()
        assert result[0] == 1