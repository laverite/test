# -*- coding: utf-8 -*-
from flask import url_for


def test_testAPp_index(client):
    res = client.get(url_for('testAPp_app.index'))
    assert res.data == b'Hello World!'
