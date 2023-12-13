from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import json

mysql = MySQL()
app = Flask(__name__)
CORS(app)

# MySQL Instance configurations
# Change these details to match your instance configurations
app.config['MYSQL_USER'] = 'A'
app.config['MYSQL_PASSWORD'] = 'B'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = 'db.mydomain.ie'
mysql.init_app(app)

@app.route("/add", methods=['POST'])  # Change to POST method for adding a student
def add():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO students(studentName, email) VALUES (%s, %s)', (name, email))
    mysql.connection.commit()
    return jsonify({"Result": "Success"})

@app.route("/", methods=['GET'])  # Changed route for better RESTful practices
def read():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM students')
    rv = cur.fetchall()
    results = []
    for row in rv:
        result = {
            'Name': row[1],
            'Email': row[2],
            'ID': row[0]
        }
        results.append(result)
    response = {'Results': results, 'count': len(results)}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


