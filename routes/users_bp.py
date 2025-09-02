from flask import Blueprint, request
from models.user import User
from extensions import db


HTTP_NOT_FOUND = 404
HTTP_CREATED = 201
HTTP_ERROR = 500

users_bp = Blueprint("users_bp", __name__)

@users_bp.get("/users")
def get_all_users():
    users = [user.to_dict() for user in User.query.all()]
    return users

@users_bp.post("/signup")
def create_user():
    return {"mess":"signup"}   
    

@users_bp.post("/login")
def Login():
    return {"mess":"login"}   
    

