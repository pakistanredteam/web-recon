from flask import Flask, render_template, request, jsonify
from app import routes

app = Flask(__name__)
app.config.from_object('config')

# Set up the database
from app.models import db
db.init_app(app)

# Set up the routes
app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run()
