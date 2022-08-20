import os
import sys

# sys.path.insert(0, os.path.dirname(__file__))

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'it works! hehehehe, lets gooooo.'
#     return [message.encode()]

from config.wsgi import application
