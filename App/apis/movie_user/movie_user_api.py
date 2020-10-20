# -*- encoding: utf-8 -*-
import uuid

from flask import request
from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_LOGIN, USER_ACTION_REGISTER, HTTP_OK
from App.apis.movie_user.model_utils import get_user
from App.ext import cache
from App.models.movie_user.movie_user_model import MovieUserModel

parse_base = reqparse.RequestParser()
parse_base.add_argument("password", type=str, required=True, help="plz input password")
parse_base.add_argument("action", type=str, required=True, help="plz input request args")

parse_register = parse_base.copy()
parse_register.add_argument("username", type=str, required=True, help="plz input username")
parse_register.add_argument("phone", type=str, required=True, help="plz input phone number")

parse_login = parse_base.copy()
parse_login.add_argument("username", type=str, help="plz input username")
parse_login.add_argument("phone", type=str, help="plz input phone number")

movie_user_fields = {
    "username": fields.String,
    "password": fields.String(attribute="_password"),
    "phone": fields.Integer
}
single_movie_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(movie_user_fields)
}


class MovieUsersResource(Resource):
    # @marshal_with(movie_user_fields)
    def post(self):
        args = parse_base.parse_args()
        password = args.get("password")
        action = args.get("action")
        if action == USER_ACTION_REGISTER:
            register = parse_register.parse_args()
            username = register.get("username")
            phone = register.get("phone")

            movie_user = MovieUserModel()
            movie_user.username = username
            movie_user.password = password
            movie_user.phone = phone
            print("--->", username, password, phone)
            if not movie_user.save():
                abort(400, message="create fail")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "success",
                "data": movie_user
            }

            return marshal(data, single_movie_user_fields)
        elif action == USER_ACTION_LOGIN:
            login = parse_login.parse_args()
            username = login.get("username")
            phone = login.get("phone")
            print("username--phone", login, username, phone)
            user = get_user(username) or get_user(phone)
            if not user:
                abort(400, message="the user isn't exists!")

            if not user.check_password(password):
                abort(400, message="password is error!")

            if user.is_delete:
                abort(400, msg="the user isn't exists!")

            token = uuid.uuid4().hex
            cache.set(token, user.id, timeout=60 * 60 * 24 * 7)
            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token
            }
            return data
        else:
            abort(400, message="plz input correct args")
