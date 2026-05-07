# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rotc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ATTENDANCE DATABASE TABLE
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rank = db.Column(db.String(50))
    platoon = db.Column(db.String(50))
    status = db.Column(db.String(50))
    date = db.Column(db.String(50))

# EQUIPMENT DATABASE TABLE
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100))
    equipment = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    date = db.Column(db.String(50))

# HOME
@app.route('/')
def home():
    return "ROTC Database System Running"

# ADD ATTENDANCE
@app.route('/attendance', methods=['POST'])
def attendance():

    data = request.json

    new_record = Attendance(
        name=data['name'],
        rank=data['rank'],
        platoon=data['platoon'],
        status=data['status'],
        date=data['date']
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({"message":"Attendance Saved"})

# ADD EQUIPMENT
@app.route('/equipment', methods=['POST'])
def equipment():

    data = request.json

    new_equipment = Equipment(
        borrower=data['borrower'],
        equipment=data['equipment'],
        quantity=data['quantity'],
        date=data['date']
    )

    db.session.add(new_equipment)
    db.session.commit()

    return jsonify({"message":"Equipment Saved"})

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)