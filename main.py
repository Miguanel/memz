from waitress import serve
import logging

from scripts.kolbapp import app

if __name__ == '__main__':
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    serve(app, host='127.0.0.1')