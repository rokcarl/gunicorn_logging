import logging
logger = logging.getLogger(__name__)

def app(environ, start_response):
    logger.info("start response")
    logger.error("something wrong")
    if environ["PATH_INFO"] == '/404':
        data = b'File is missing!\n'
        status = '404 Not Found'
        logger.error("MISSING")
    else:
        data = b'Hello, World!\n'
        status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
