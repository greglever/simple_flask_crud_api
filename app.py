import json

from flask import Flask

from store import (
    get_all_products,
    create_default_database_table,
)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/products")
def products():
    product_list = get_all_products()
    return json.dumps(product_list)


if __name__ == "__main__":
    create_default_database_table()
    app.run(host='0.0.0.0', debug=True)
