#!/usr/bin/env python

from app import app as application
from app.routes import *


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001)