#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0')
