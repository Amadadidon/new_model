# list_users.py
import os
from models import db, User
from flask import Flask

# Initialize Flask app context
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/social.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def list_all_users():
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found in the database.")
            return
        print("Users in the database:")
        print("-" * 40)
        for user in users:
            admin_flag = " (Admin)" if user.is_admin else ""
            print(f"ID: {user.id} | Username: {user.username} | Email: {user.email}{admin_flag}")
        print("-" * 40)
        print(f"Total users: {len(users)}")

if __name__ == "__main__":
    list_all_users()

