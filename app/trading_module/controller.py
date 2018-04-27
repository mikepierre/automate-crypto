# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,\
                  jsonify
# Import Bittrex API
from app.exchanges_api_module.bittrex import bittrex
# Define the blueprint
trading_module = Blueprint('main', __name__)

@trading_module.route("/", methods=['GET', 'POST'])
def index():
	return render_template("trading_module/layout.html")

@trading_module.route("/set-sell", methods=['GET', 'POST'])
def set_sell():
    return "set sell"

@trading_module.route("/set-sell", methods=['POST'])
def get_sell():
    return "get sell"

@trading_module.route("/get-currency", methods=['GET'])
def get_currency():
    ico = request.args.get('ico')
    return jsonify(bittrex.get_market_summery(ico).json())

@trading_module.route("/get-summaries", methods=['GET'])
def get_summaries():
    return jsonify(bittrex.get_summaries().json())