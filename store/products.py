from store import get_db


def execute_query(query):
    db = get_db()
    return db.execute(query)


def get_all_products():
    result = execute_query(query="SELECT * FROM products;")
    result_list = [
        {"id": row[0], "name": row[1], "price": "%.2f" % row[2]} for row in result
    ]
    return result_list


def add_product_by_name_and_price(name=None, price=None):
    if name is None or price is None:
        raise ValueError("Name and price must be provided !")
    db = get_db()
    db.execute("INSERT INTO products (name, price) VALUES (%s, %s)", name, price)


def get_product_by_id(product_id):
    check_product_exists(product_id)
    db = get_db()
    query_result = db.execute("SELECT * FROM products WHERE id={product_id};".format(product_id=product_id))
    result = [{"id": row[0], "name": row[1], "price": "%.2f" % row[2]} for row in query_result][0]
    return result


def check_product_exists(product_id):
    db = get_db()
    query_result = db.execute("SELECT * FROM products WHERE id={product_id};".format(product_id=product_id))
    if len([row for row in query_result]) < 1:
        raise ValueError("Product with ID: {product_id} is not in the database !")


def update_product_by_id(product_id, name_to_update=None, price_to_update=None):
    check_product_exists(product_id=product_id)
    if name_to_update is None and price_to_update is None:
        raise ValueError("No values to update !")
    query = "UPDATE products SET "
    if name_to_update is not None:
        query += "name = '{name}' ".format(name=name_to_update)
    if price_to_update is not None:
        query += ", price = {price} ".format(price=price_to_update)
    query += "WHERE id = {product_id}".format(product_id=product_id)
    execute_query(query=query)


def delete_product_by_id(product_id):
    check_product_exists(product_id=product_id)
    execute_query(query="DELETE FROM products WHERE id = {product_id}".format(product_id=product_id))
