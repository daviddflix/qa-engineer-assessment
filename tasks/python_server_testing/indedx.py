from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto.db'
db = SQLAlchemy(app)

class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/fetch', methods=['GET'])
def fetch_crypto_data():
    name = request.args.get('name')
    symbol = request.args.get('symbol')
    
    if not name or not symbol:
        return jsonify({"error": "Both name and symbol are required"}), 400

    # Simulating Binance API call
    binance_data = {"name": name, "symbol": symbol, "price": 100.0}
    
    return jsonify(binance_data)

@app.route('/save', methods=['POST'])
def save_crypto_data():
    data = request.json
    
    if not data or 'name' not in data or 'symbol' not in data or 'price' not in data:
        return jsonify({"error": "Invalid data"}), 400

    crypto = Cryptocurrency(name=data['name'], symbol=data['symbol'], price=data['price'])
    db.session.add(crypto)
    db.session.commit()
    
    return jsonify({"message": "Data saved successfully"}), 201

@app.route('/retrieve', methods=['GET'])
def retrieve_crypto_data():
    cryptos = Cryptocurrency.query.all()
    result = [{"name": c.name, "symbol": c.symbol, "price": c.price} for c in cryptos]
    return jsonify(result)

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)