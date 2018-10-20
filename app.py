import json

from flask import (
    Flask,
    request,
    Response,
)

from store import (
    get_all_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id,
    create_default_database_table,
    add_product_by_name_and_price,
)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/products", methods=['GET'])
def get_products():
    """
    Endpoint to return all products
    """
    product_list = get_all_products()
    return Response(json.dumps(product_list), status="200")


@app.route("/v1/product", methods=['POST'])
def add_product():
    """
    Endpoint to create a new product
    """
    name = request.form.get("name")
    price = request.form.get("price")
    try:
        add_product_by_name_and_price(name=name, price=price)
        return Response("Data created", status="200")
    except ValueError as e:
        return Response("Error with data: {e}".format(e=e), status="406")


# TODO(Greg): Figure out how to check the request method for each of these
# TODO(Greg): then have them in the same function
@app.route('/v1/product/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        result = get_product_by_id(product_id=product_id)
        return Response(json.dumps(result), status="200")
    except ValueError as e:
        return Response("Error with data: {e}".format(e=e), status="404")


@app.route('/v1/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        name = request.form.get("name")
        price = request.form.get("price")
        update_product_by_id(product_id=product_id, name_to_update=name, price_to_update=price)
        return Response("Product correctly updated", status="200")
    except ValueError as e:
        return Response("Error with data: {e}".format(e=e), status="404")


@app.route('/v1/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        delete_product_by_id(product_id=product_id)
        return Response("Product correctly deleted", status="200")
    except ValueError as e:
        return Response("Error with data: {e}".format(e=e), status="404")


if __name__ == "__main__":
    create_default_database_table()
    app.run(host='0.0.0.0', debug=True)
