# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.trading_module.controller import trading_module

# Register blueprint(s)
app.register_blueprint(trading_module)