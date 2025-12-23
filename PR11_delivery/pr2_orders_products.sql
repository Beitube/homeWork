CREATE TABLE orders_products (
order_id INT, 
product_id INT NOT NULL,
quantity INT,
PRIMARY KEY (order_id, product_id),
FOREIGN KEY (order_id) REFERENCES orders (order_id),
FOREIGN KEY (product_id) REFERENCES products (product_id)
);
