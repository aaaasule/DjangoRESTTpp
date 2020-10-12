# -*- encoding: utf-8 -*-
from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        print("request_url", request.url)

    @app.after_request
    def after(response):
        return response
