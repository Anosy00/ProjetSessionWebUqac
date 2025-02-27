import requests
from app.models import Product

def fetch_products():
    url = "http://dimensweb.uqac.ca/~jgnault/shops/products/"
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json().get("products", [])
        for product in products:
            Product.get_or_create(id=product["id"], defaults=product)