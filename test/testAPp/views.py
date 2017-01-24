# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['testAPp_app']

testAPp_app = Blueprint('testAPp_app', __name__)


@testAPp_app.route('/')
def index():
    return "Hello World!"
