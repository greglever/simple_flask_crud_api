from store import get_db


def get_all_products():
    db = get_db()
    result = db.execute("SELECT * FROM products;")
    result_list = [
        {"id": row[0], "name": row[1], "price": "%.2f" % row[2]} for row in result
    ]
    return result_list
