from flask import Flask, make_response, jsonify, request

import server.helpers as helpers
import server.log as log
import server.controller.create as create
import server.controller.read as read
import server.controller.update as update
import server.controller.delete as delete

app = Flask(__name__)

@app.route('/fast/v1/create', methods=['POST'])
def create_order():
    r = request.get_json()
    log.print_request_details(request, r)

    resp = create.create_order(r)
    update.update_order(resp)

    full_resp = make_response(jsonify(resp), 200)
    log.print_response_details(full_resp)
    return full_resp

@app.route('/fast/v1/read', methods=['POST'])
def read_order():
    r = request.get_json()
    log.print_request_details(request, r)

    order = read.get_order_by_external_id(r) # TODO: perform checks if order is empty

    full_resp = make_response(jsonify(order), 200)
    log.print_response_details(full_resp)
    return full_resp

@app.route('/fast/v1/update', methods=['POST'])
def update_order():
    r = request.get_json()
    log.print_request_details(request, r)

    order = read.get_order_by_fast_order_id(r) # TODO: perform checks if order is empty

    # Update Shipment Details
    order = update.update_shipment_details(r, order)

    # Update Selected Shipping Option
    order = update.update_shipping_option(r, order)

    update.update_order(order)

    full_resp = make_response(jsonify(order), 200)
    log.print_response_details(full_resp)
    return full_resp

@app.route('/fast/v1/delete', methods=['POST'])
def delete_order():
    r = request.get_json()
    log.print_request_details(request, r)

    delete.delete_order(r)

    resp = {
        "request_id": helpers.create_request_id(),
        "order": {}
    }
    
    full_resp = make_response(jsonify(resp), 200)
    log.print_response_details(full_resp)
    return full_resp

if __name__ == '__main__':
    app.wsgi_app = log.LoggingMiddleware(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')
