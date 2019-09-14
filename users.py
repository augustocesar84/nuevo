from flask import Blueprint

users = Blueprint('users',__name__)

@users.route("/users")
def accountList():
    return "<h1>lista de usuarios</h1>"