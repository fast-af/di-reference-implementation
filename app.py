from flask import Flask, make_response, jsonify, request

import server.log as log
import server.controller.create as create
import server.controller.read as read
import server.controller.update as update
import server.controller.delete as delete
import server.controller.refund as refund

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
SANDBOX_FAST_URL = "https://api.sandbox.fast.co"

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

    # Convert Cart to Order?
    convert_cart_to_order = r.get("order", {}).get("convert_cart_to_order", False)
    if convert_cart_to_order:
        order = update.convert_cart_to_order(order)

    # Update Shipment Details
    shipments = r.get("order", {}).get("shipments", [])
    if len(shipments) > 0:
        order = update.update_shipment_details(r, order, shipments)

    # Update Selected Shipping Option
    shipping_option = r.get("order", {}).get("shipping_option", {})
    if shipping_option != {}:
        order = update.update_shipping_option(r, order, shipping_option)

    # Update Coupon
    coupon = r.get("order", {}).get("coupon", {})
    if coupon != {}:
        order = update.update_coupon(r, order, coupon)

    # Update Bill To
    billing_details = r.get("order", {}).get("bill_to", {})
    if billing_details != {}:
        order = update.update_billing_details(r, order, billing_details)

    # Update Items
    items = r.get("order", {}).get("items", [])
    if items != []:
        order = update.update_line_items(r, order, items)

    update.update_order(order)

    # read object again to make sure we return the full Fast order
    order = read.get_order_by_fast_order_id(r)
    
    full_resp = make_response(jsonify(order), 200)
    log.print_response_details(full_resp)
    return full_resp

@app.route('/fast/v1/delete', methods=['POST'])
def delete_order():
    r = request.get_json()
    log.print_request_details(request, r)

    delete.delete_order(r)

    resp = {
        "type": r.get("type", None),
        "order": {}
    }
    
    full_resp = make_response(jsonify(resp), 200)
    log.print_response_details(full_resp)
    return full_resp

# This method is just used so we have an endpoint to trigger the call to Fast's refund endpoint
@app.route('/v1/external/orders/<id>/refund', methods=['POST'])
def refund_order(id):
    r = request.get_json()
    app_id = request.headers.get("x-fast-app", "")
    session_id = request.headers.get("cookie", "")
    order_id = request.url.split("/")[-2]
    

    url = SANDBOX_FAST_URL + f"/v1/external/orders/{order_id}/refund"

    log.print_seller_to_fast_request_details(r, url)
    resp = refund.refund_order(url, r, app_id, session_id)

    full_resp = make_response(resp.json(), resp.status_code)
    log.print_fast_to_seller_response_details(full_resp)
    return full_resp

 
if __name__ == '__main__':
    app.wsgi_app = log.LoggingMiddleware(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')
