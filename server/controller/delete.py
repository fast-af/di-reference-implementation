import psycopg2
import sys
import pprint

import server.db as db

def delete_order(r):
    order_id = r.get("order", {}).get("order_id", {}).get("value", "")
    try:
        conn = db.db_connect()
        curr = conn.cursor()
        
        curr.execute("""
            DELETE FROM orders
            WHERE id = %s;
        """, (order_id,))
        
        conn.commit()
        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        pprint.pprint(error, stream=sys.stderr)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')