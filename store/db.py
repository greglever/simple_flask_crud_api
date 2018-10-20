from sqlalchemy import create_engine


# TODO: Make this a context manager to deal with sessions
def get_db():
    db_string = "postgresql+psycopg2://crudproducts:crudproducts@db/postgres"
    return create_engine(db_string)

def create_default_database_table():
    """
    Create the following table, called products:
    | Product code  | Name                       |  Price |
    |---            |---                         |---     |
    |  001          |  Lavender heart            | £9.25  |
    |  002          |  Personalised cufflinks    | £45.00 |
    |  003          |  Kids T-shirt              | £19.95 |
    """
    db = get_db()
    db.execute("DROP TABLE IF EXISTS products")
    db.execute("CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(100), price FLOAT )")
    db.execute("INSERT INTO products (name, price) VALUES (%s, %s)", "Lavender heart", 9.25)
    db.execute("INSERT INTO products (name, price) VALUES (%s, %s)", "Personalised cufflinks", 45.00)
    db.execute("INSERT INTO products (name, price) VALUES (%s, %s)", "Kids T-shirt", 19.95)
