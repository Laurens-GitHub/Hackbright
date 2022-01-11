"""Demonstration backend for AJAX."""

import random
from time import sleep
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

MELONS = ["Cantaloupe", "Honeydew", "Watermelon", "Musk"]

CITY_DELIVERY_INFO = {
    "SF": {
        "days": 1,
        "cost": 3.00,
    },
    "Oak": {
        "days": 2,
        "cost": 5.00,
    },
    "other": {
        "days": 5,
        "cost": 10.00,
    },
}

ADJECTIVES = ["Delicious","Aromatic","Ripe", "Flavorful","Reasonably-Priced"]


@app.route("/")
def index():
    """Homepage."""

    return render_template("index.html", melons=MELONS)


@app.route("/adjective")
def get_random_adjective():
    """Return a simple adjective."""

    sleep(2) # simulate a slow server
    return random.choice(ADJECTIVES)


@app.route("/status")
def get_order_status():
    """Get order status."""

    order_number = request.args.get("order")
    # For simplicity, we are just returning
    # a hard coded string but our data could
    # come from an external API or a database
    # and may take a while to be retrieved
    # we simulate this by adding the 2 seconds delay below
    sleep(2)
    if order_number == "123":
        return random.choice(["LATE", "SUPER-LATE"])
    else:
        return "ON-TIME"


@app.route("/new-order", methods=["POST"])
def add_order():
    """Add a melon order to our database."""
    sleep(2) # simulates the time actually adding the melon to the DB would take
    melon_type = request.json.get("type")
    amount = request.json.get("amount")

    return { "success": True, "status": "Your order has been confirmed"}


@app.route("/delivery-info.json")
def get_delivery_info():
    """Get delivery info."""

    address = request.args.get("address")
    city = request.args.get("city")

    if city in CITY_DELIVERY_INFO:
        return jsonify(CITY_DELIVERY_INFO[city])
    else:
        return jsonify(CITY_DELIVERY_INFO["other"])


@app.route("/melon-info_error.json")
def melon_info_py():
    """This route will fail!"""

    melon_1 = {
        "id": "watermelon",
        "price": 5.00,
        "available": True,
        "countries": ["US", "CA", "MX"],
    }
    return melon_1


@app.route("/melon-info.json")
def melon_info():
    """Return info about a melon as JSON."""

    # In real life, we would probably get this info
    # from our database
    melon_1 = {
        "id": "watermelon",
        "price": 5.00,
        "available": True,
        "countries": ["US", "CA", "MX"],
    }

    return jsonify(melon_1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)