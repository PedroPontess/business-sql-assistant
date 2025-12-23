import pytest
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from src.database import get_db_connection


def test_database_is_read_only():
    db_wrapper = get_db_connection()

    engine = db_wrapper._engine

    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM EMPLOYEE")).scalar()
        assert isinstance(result, int)

    with pytest.raises(OperationalError):
        with engine.connect() as conn:
            conn.execute(text("CREATE TABLE hack (id INTEGER)"))
