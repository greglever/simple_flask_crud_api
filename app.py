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

from flask_restplus import Api
from flask_restplus import Resource

api = Api()
app = Flask(__name__)
api.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


@api.route("/v1/products")
class Products(Resource):

    def get(self):
        """
        Endpoint to return all products
        """
        product_list = get_all_products()
        return Response(json.dumps(product_list), status="200")


@api.route("/v1/product")
class NewProduct(Resource):

    def post(self):
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


@api.route('/v1/product/<product_id>')
class Product(Resource):
    def get(self, product_id):
        """
        Endpoint to get a product by ID
        """
        try:
            result = get_product_by_id(product_id=product_id)
            return Response(json.dumps(result), status="200")
        except ValueError as e:
            return Response("Error with data: {e}".format(e=e), status="404")

    def put(self, product_id):
        """
        Endpoint to update a product by ID (please provide name, price or both)
        """
        try:
            name = request.form.get("name")
            price = request.form.get("price")
            update_product_by_id(product_id=product_id, name_to_update=name, price_to_update=price)
            return Response("Product correctly updated", status="200")
        except ValueError as e:
            return Response("Error with data: {e}".format(e=e), status="404")

    def delete(self, product_id):
        """
        Endpoint to delete a product by ID
        """
        try:
            delete_product_by_id(product_id=product_id)
            return Response("Product correctly deleted", status="200")
        except ValueError as e:
            return Response("Error with data: {e}".format(e=e), status="404")


if __name__ == "__main__":
    create_default_database_table()
    app.run(host='0.0.0.0', debug=True)
