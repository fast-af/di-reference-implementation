CREATE TABLE products (
   id VARCHAR(50),
   variant_id VARCHAR(50),
   price FLOAT,
   discount FLOAT,
   name VARCHAR(50),
   PRIMARY KEY (id, variant_id)
);

CREATE TABLE orders (
    id VARCHAR(50) PRIMARY KEY,
    fast_order_id VARCHAR(50) UNIQUE,
    fast_order JSONB
);