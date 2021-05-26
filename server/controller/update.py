import pprint
import json
import psycopg2
import sys

import server.db as db
import server.helpers as helpers

def update_order(order):
    try:
        conn = db.db_connect()
        curr = conn.cursor()
        data = {
            "id": order["order"]["order"]["external_id"],
            "fast_order_id": order["order"]["order"]["id"]["value"],
            "fast_order": json.dumps(order)
        }
        
        curr.execute("""
        INSERT INTO orders (id, fast_order_id, fast_order)
        VALUES (%(id)s,%(fast_order_id)s,%(fast_order)s)
        ON CONFLICT (id) DO UPDATE SET fast_order = %(fast_order)s
        """, data)
        
        conn.commit()
        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        pprint.pprint(error, stream=sys.stderr)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def update_shipping_option(r, order):
    shipping_option = r.get("order", {}).get("shipping_option", {})
    if shipping_option != {}:
        shipment_plans = order.get("order", {}).get("order", {}).get("shipment_plans", {})
        shipment_plan_id = shipping_option.get("plan_id", {}).get("value", "")

        for i, shipment_plan in enumerate(shipment_plans):
            if shipment_plan.get("external_id", "") == shipment_plan_id:
                order["order"]["order"]["shipment_plans"][i]["selected_option"]["external_id"] = shipping_option["option_id"]["value"]

    return order

def update_shipment_details(r, order):
    selected_option_external_uuid = helpers.create_uuid()

    shipments = r.get("order", {}).get("shipments", [])
    shipment_plans = []
    if len(shipments) > 0:
        for shipment in shipments:
            shipment_plan = {
                # Get id, ship_to, and lines from request
                "id": shipment.get("plan_id", {"value": helpers.create_uuid()}),
                "ship_to": shipment.get("ship_to"),
                # add external_id, selected_option, available_option from internal server (using ship_to address)
                "external_id": helpers.create_uuid(),
                "selected_option": { # TODO: load shipping options from service instead of hardcoding
                    "shipment_type": 99,
                    "cost": "0.00",
                    "tax": "0.00",
                    "total": "0.00"
                },
                "available_options": [
                    {
                    "external_id": selected_option_external_uuid,
                    "name": "Free Shipping",
                    "shipment_type": 99,
                    "cost": "0.00",
                    "tax": "0.00",
                    "total": "0.00"
                    }
                ]
            }
            shipment_plans.append(shipment_plan)
        order["order"]["order"]["bill_to"] = shipments[0].get("ship_to")
        order["order"]["order"]["shipment_plans"] = shipment_plans
    
    return order