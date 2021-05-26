import uuid

def create_uuid():
    return str(uuid.uuid4())

def create_order_id():
    return create_uuid()

def create_line_id():
    return create_uuid()

def create_request_id():
    return create_uuid()