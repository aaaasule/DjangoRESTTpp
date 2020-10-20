# -*- encoding: utf-8 -*-
from App.models.movie_user import MovieUserModel


def get_user(user_ident):
    if not user_ident:
        return None

    user = MovieUserModel.query.get(user_ident)

    if user:
        return user

    user = MovieUserModel.query.filter(MovieUserModel.phone.__eq__(user_ident)).first()
    if user:
        return user

    user = MovieUserModel.query.filter(MovieUserModel.username.__eq__(user_ident)).first()

    if user:
        return user

    return None
