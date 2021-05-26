import psycopg2

import server.db as db

def get_order_by_external_id(r):
    order_id = r.get("order", {}).get("external_order_id", "")
    try:
        conn = db.db_connect()

        curr = conn.cursor()
        curr.execute("SELECT fast_order FROM orders WHERE id = %s", (order_id, ))
        order = curr.fetchone()[0]
        curr.close()
        return order
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return {}

def get_order_by_fast_order_id(r):
    order_id = r.get("order", {}).get("order_id", {}).get("value", "")
    try:
        conn = db.db_connect()

        curr = conn.cursor()
        curr.execute("SELECT fast_order FROM orders WHERE fast_order_id = %s", (order_id, ))
        order = curr.fetchone()[0]
        curr.close()
        return order
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return {}