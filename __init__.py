from flask import Flask, jsonify
#from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

app = Flask(__name__)

# Конфигурация MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

#mysql = MySQL(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello world!'}), 201

if __name__ == "__main__":
  app.run(debug=True)
