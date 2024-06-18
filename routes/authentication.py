import os
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
import jwt
import datetime
from dotenv import load_dotenv

load_dotenv()

def authentication(app, client):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db = client.flask_db
    users = db.users

    @app.route('/signup', methods=['POST'])
    def signup():
        data=request.form

        if "name" in data:
            name=data['name']
        else:
            return "Please Specify the Name", 400

        if "email" in data:
            email=data['email']
        else:
            return "Please Specify the Email", 400

        if "password" in data:
            password=data['password']
        else:
            return "Please Write the Password", 400

        if "organization" in data:
            organization=data['organization']
        else:
            return "Please Specify the Organization Name", 400

        users.insert_one({'name':name, 'email':email, 'password':password, 'organization':organization})

        return "Data Posted", 200

    @app.route('/forgotPassword', methods=['POST'])
    def forgotPassword():
        data = request.form

        if "email" in data:
            email = data['email']
        else:
            return "Please Specify the Email", 400

        user = users.find_one({"email": email})
        if not user:
            return "Email isn't Registered", 401
        else:
            password = data['password']
            user['password'] = password

            return "Password Updated", 200

    @app.route('/login', methods=['POST'])
    def login():
        data = request.form

        if "email" in data:
            email = data['email']
        else:
            return "Please Specify the Email", 400

        if "password" in data:
            password = data['password']
        else:
            return "Please Write the Password", 400

        user = users.find_one({"email": email})
        if not user:
            return "Email isn't Registered", 401
        else:
            if user['password'] == password:
                return "Login Successful", 200
            else:
                return "Invalid Password", 401