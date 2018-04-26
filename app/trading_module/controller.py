# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
# Import Bittrex API
from app.exchanges_api_module.bittrex import bittrex
# Define the blueprint
trading_module = Blueprint('main', __name__)

@trading_module.route("/", methods=['GET', 'POST'])
def hello():
	return "Hello World!!"

@trading_module.route("/login", methods=['GET', 'POST'])
def login():
    return "login"