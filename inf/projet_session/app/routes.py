from flask import Blueprint, request, jsonify, redirect, url_for
from app.models import Product, Order
from app.utils import calculate_shipping, calculate_tax

bp = Blueprint('routes', __name__)

@bp.route("/", methods=["GET"])
def get_products():
    products = list(Product.select().dicts())
    return jsonify({"products": products})

@bp.route("/order", methods=["POST"])
def create_order():
    data = request.json.get("product")
    if not data or "id" not in data or "quantity" not in data or data["quantity"] < 1:
        return jsonify({"errors": {"product": {"code": "missing-fields", "name": "Commande invalide"}}}), 422
    product = Product.get_or_none(Product.id == data["id"])
    if not product:
        return jsonify({"errors": {"product": {"code": "out-of-inventory", "name": "Produit non disponible"}}}), 422
    shipping_price = calculate_shipping(product.weight)
    order = Order.create(product_id=product.id, quantity=data["quantity"], total_price=product.price * data["quantity"], shipping_price=shipping_price)
    return redirect(url_for("routes.get_order", order_id=order.id), code=302)

@bp.route("/order/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.get_or_none(Order.id == order_id)
    if not order:
        return jsonify({"error": "Commande non trouvée"}), 404
    return jsonify({"order": order.__data__})
