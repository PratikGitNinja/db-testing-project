import pytest
from pytest_bdd import scenario,given,when,then
import mysql.connector

@pytest.fixture
def db_cursor():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="practice"
    )
    cursor = conn.cursor()
    yield cursor
    cursor.close()
    conn.close()

scenario('../features/transaction_validations.feature','Validate all transactions belong to existing customers')
@given('the transactions and customer tables are available')
def test_tables_available(db_cursor):
        
    db_cursor.execute("SHOW TABLES")
    TABLES = [table[0] for table in db_cursor.fetchall()]
    assert 'transactions' in TABLES
    assert 'customers' in TABLES

invalid_transaction = []
@when('we fetch transactions with invalid customer_id')
def test_transaction_with_invalid_transaction(db_cursor):
    
    global invalid_transaction
    db_cursor.execute("""
        SELECT t.txn_id FROM transactions t left join customers c on t.customer_id = c.customer_id
        Where c.customer_id is null
        """)
    invalid_transaction = db_cursor.fetchall()

@then('there should be no such transactions')
def test_validate_no_invalid_transaction():
        
    assert len(invalid_transaction) == 0, f"There are {len(invalid_transaction)} invalid transactions."

