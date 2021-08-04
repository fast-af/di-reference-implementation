import pprint
import sys

separators = ["-", "-", "-", "-"]

def print_request_details(req, req_json):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    trace_id = ""
    for header in req.headers:
        if header[0] == 'X-Datadog-Trace-Id':
            trace_id = header[1]
    pprint.pprint((f"Trace ID:", trace_id), stream=sys.stderr)
    pprint.pprint((f"Headers:", req.headers), stream=sys.stderr)
    pprint.pprint((f"{req.method} Fast->Seller Request to {req.url}:", req_json), stream=sys.stderr)

def print_seller_to_fast_request_details(req_json, url):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    pprint.pprint((f"Seller->Fast Request to {url}:", req_json), stream=sys.stderr)

def print_fast_to_seller_response_details(resp):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    pprint.pprint(("Fast->Seller Response: ", resp.get_json()), sys.stderr)

def print_response_details(resp):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    pprint.pprint(("Seller->Fast Response: ", resp.get_json()), sys.stderr)

class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        def log_response(status, headers, *args):
            pprint.pprint((f"Response status and headers from {env['REQUEST_URI']}", status, headers), stream=errorlog)
            
            return resp(status, headers, *args)

        return self._app(env, log_response)