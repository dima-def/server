from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Конфигурация MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello world!'}), 201

# Создание машины (Create)
@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    brand = data['brand']
    model = data['model']
    color = data['color']
    license_plate = data['license_plate']
    
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO cars (brand, model, color, license_plate) VALUES (%s, %s, %s, %s)",
        (brand, model, color, license_plate)
    )
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Car added successfully!'}), 201


if __name__ == "__main__":
  app.run(debug=True)
