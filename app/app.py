from flask import Flask, make_response, jsonify, request
import pprint
import sys
import json

separators = ["-", "-", "-", "-"]

def print_request_details(req, req_json):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    pprint.pprint((f"Request headers to {req.url}:", req.headers), stream=sys.stderr)
    pprint.pprint((f"{req.method} Request to {req.url}:", req_json), stream=sys.stderr)

def print_response_details(resp):
    pprint.pprint(separators, stream=sys.stderr, width=3)
    pprint.pprint(("Response: ", resp.get_json()), sys.stderr)

class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        def log_response(status, headers, *args):
            pprint.pprint((f"Response status and headers from {env['REQUEST_URI']}", status, headers), stream=errorlog)
            
            return resp(status, headers, *args)

        return self._app(env, log_response)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/fast/v1/create', methods=['POST'])
def create():
    r = request.get_json()
    print_request_details(request, r)

    resp = {
        "type": "ENTITY_TYPE_ORDER",
        "order": {
            "order": {
            "id": {
                "value": r["order"]["order"]["id"]["value"]
            },
            "external_id": "f3098ae6-4dfc-4f1b-8721-432c7b04f777",
            "user_id": "09876",
            "order_type": "ORDER_TYPE_CART",
            "currency_code": "USD",
            "status": "ORDER_STATUS_PENDING",
            "lines": [
                {
                "id": {
                    "value": r["order"]["order"]["lines"][0]["id"]["value"]
                },
                "external_id": "87654321",
                "external_product_id": "1",
                "external_variant_id": "3",
                "quantity": 1,
                "total_amount": "29.99",
                "subtotal_amount": "29.99"
                }
            ],
            "total_amount": "29.99",
            "sub_total": "29.99",
            "total_discounts": "0.00",
            }
        },
        "request_id": {
            "value": "f3098ae6-4dfc-4f1b-8721-432c7b04f555"
        }
    }

    full_resp = make_response(jsonify(resp), 200)
    print_response_details(full_resp)
    return full_resp

@app.route('/fast/v1/update', methods=['POST'])
def update():
    r = request.get_json()
    print_request_details(request, r)


    full_resp = make_response(jsonify("{}"), 200)
    print_response_details(full_resp)
    return full_resp

if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')
