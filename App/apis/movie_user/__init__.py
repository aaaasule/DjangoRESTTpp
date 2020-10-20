# -*- encoding: utf-8 -*-
from flask_restful import Api

from App.apis.movie_user.movie_order_api import MovieOrdersResource
from App.apis.movie_user.movie_user_api import MovieUsersResource

client_api = Api(prefix="/user")

client_api.add_resource(MovieUsersResource, "/movie_users/")

client_api.add_resource(MovieOrdersResource, "/movie_orders/")