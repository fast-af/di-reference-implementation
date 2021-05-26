import pprint
import psycopg2
import psycopg2.extras
import sys

import server.db as db
import server.helpers as helpers

def calculate_totals(line_items):
    total = 0
    subtotal = 0
    discounts = 0
    tax_amount = 0

    for line in line_items:
        quantity = line["quantity"]
        total += (float(line["discounted_unit_price"]) + float(line["tax_amount"])) * float(quantity)
        subtotal += float(line["discounted_unit_price"]) * float(quantity)
        discounts += float(line["line_discount_amount"]) * float(quantity)
        tax_amount += float(line["tax_amount"]) * float(quantity)

    totals = {
        "total": str(total),
        "subtotal": str(subtotal),
        "discounts": str(discounts),
        "tax_amount": str(tax_amount)
    }
    return totals

def get_product_id(line):
    # returns {"product_id": 123, "variant_id": 123, "options": []}
    product_id_w_variants = {"product_id": "", "variant_id": "", "options": []}

    external_product_id = line.get("external_product_id", "")
    external_variant_id = line.get("external_variant_id", "")
    external_options = line.get("external_options", [])

    if external_product_id != "":
        product_id_w_variants["product_id"] = external_product_id

    if external_variant_id != "":
        product_id_w_variants["variant_id"] = external_variant_id

    if external_options != []:
        product_id_w_variants["options"] = external_options

    return product_id_w_variants

def get_product_info(product_id_w_variants):
    # query product info from db including price, discounts, etc.
    product_info = []
    try:
        conn = db.db_connect()

        curr = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        pprint.pprint("Getting product from database", stream=sys.stderr)
        query = "SELECT * FROM products WHERE id = %(product_id)s"
        curr.execute(query, product_id_w_variants)
        
        product_info = curr.fetchall()
        if len(product_info) == 1:
            pprint.pprint(("Found product: ", product_info[0]), stream=sys.stderr)
            return product_info[0]

        for product in product_info:
            if product["variant_id"] == product_id_w_variants["variant_id"]:
                pprint.pprint(("Found product with variant: ", product_info[0]), stream=sys.stderr)
                return product

        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        pprint.pprint(error, stream=sys.stderr)
    finally:
        if conn is not None:
            conn.close()
            pprint.pprint('Database connection closed.', stream=sys.stderr)

    return product_info[0] if len(product_info) > 0 else []


def map_fulfillment_mode(fulfillment_mode):
    #Default: "ITEM_FULFILLMENT_MODEL_UNSPECIFIED"
    #Enum: "ITEM_FULFILLMENT_MODEL_UNSPECIFIED" "ITEM_FULFILLMENT_MODEL_PHYSICAL" "ITEM_FULFILLMENT_MODEL_DIGITAL" "ITEM_FULFILLMENT_MODEL_SERVICE"
    return fulfillment_mode

def create_line_items(lines):
    platform_lines = []
    for line in lines:
        product_id_w_variants = get_product_id(line)
        product_info = get_product_info(product_id_w_variants)
        platform_line = {
            "id": {
                "value": line.get("id").get("value")
            },
            "external_id": helpers.create_line_id(),
            "external_product_id": product_id_w_variants.get("product_id", ""),
            "external_variant_id": product_id_w_variants.get("variant_id", ""),
            "external_options": product_id_w_variants.get("options", []),
            "customizations": product_id_w_variants.get("customizations", []),
            "quantity": line.get("quantity", 0),
            "quantity_fulfilled": line.get("quantity_fulfilled", 0),
            "unit_price": str(product_info.get("price", "0.00")),
            "discounted_unit_price": str(float(product_info.get("price", "0.00")) - float(product_info.get("discount", "0.00"))),
            "line_discount_amount": str(product_info.get("discount", "0.00")),
            "tax_amount": str(product_info.get("tax_amount", "0.00")),
            "discounts": product_info.get("discounts", []),
            "name": product_info.get("name", ""),
            "description": product_info.get("description", ""),
            "image_url": product_info.get("image_url", ""),
            "fulfillment_mode": map_fulfillment_mode(product_info.get("fulfillment_mode", 1))
        }
        platform_line["total_amount"] = str((float(platform_line["discounted_unit_price"]) + float(platform_line["tax_amount"])) * platform_line["quantity"])
        platform_line["subtotal_amount"] = str(float(platform_line["discounted_unit_price"]) * platform_line["quantity"])
        platform_lines.append(platform_line)

    return platform_lines

def create_order(r):
    line_items = create_line_items(r.get("order", {}).get("order", {}).get("lines", []))
    totals = calculate_totals(line_items)
    resp = {
        "type": "ENTITY_TYPE_ORDER",
        "order": {
            "order": {
                "id": {
                    "value": r["order"]["order"]["id"]["value"]
                },
                "external_id": helpers.create_order_id(),
                "order_type": r.get("order", {}).get("order", {}).get("order_type", ""),
                "currency_code": "USD",
                "status": r.get("order", {}).get("order", {}).get("status", ""),
                "lines": line_items,
                "total_amount": totals.get("total", ""),
                "sub_total": totals.get("subtotal", ""),
                "total_discounts": totals.get("discounts", ""),
                "total_tax": totals.get("tax_amount", "")
            }
        },
        "request_id": {
            "value": helpers.create_request_id()
        }
    }

    return resp