from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect , render_template, request, jsonify, url_for
from models import Products, User, setup_db, rollback, checkout, carts, order, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user
)
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os 


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    # db = SQLAlchemy(app). setup.sh



######################### Auth ###############################################
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)




    class ModeslView(ModelView):
        def is_accessible(self):
            if current_user.is_authenticated:
                if current_user.is_Admin:
                    return current_user.is_authenticated

    admin = Admin(app)
    admin.add_view(ModeslView(User, db.session))
    admin.add_view(ModeslView(checkout, db.session))
    admin.add_view(ModeslView(Products, db.session))
    admin.add_view(ModeslView(carts, db.session))
    admin.add_view(ModeslView(order, db.session))
    
    @app.route('/')
    def home():
        return "zaid"
    return app 




APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
