import pytest


@pytest.mark.db_test
def test_database_connection(conn):
    assert conn is not None


@pytest.mark.db_test
def test_data_insertion(cursor_con):
    cursor, conn = cursor_con

    cursor.execute("INSERT INTO users (name) VALUES ('John') RETURNING id")
    user_id = cursor.fetchone()[0]

    cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'John'
