CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT NOT NULL,
date_get TIMESTAMP,
FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
