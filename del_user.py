# del_user.py
from flask import Flask
from models import db, User
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'social.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def delete_user_by_email():
    email = input("Enter the email of the user to delete: ").strip()
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if not user:
            print("User not found.")
            return
        confirm = input(f"Are you sure you want to delete {user.username} ({user.email})? [y/n]: ").lower()
        if confirm == 'y':
            db.session.delete(user)
            db.session.commit()
            print(f"User {user.username} has been deleted successfully.")
        else:
            print("Deletion canceled.")

if __name__ == "__main__":
    delete_user_by_email()
