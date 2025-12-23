CREATE TABLE delivery_list (
delivery_id SERIAL PRIMARY KEY,
order_id INT NOT NULL,
courier_id INT NOT NULL,
date_arrived TIMESTAMP,
taken BOOLEAN DEFAULT 'no',
payment_method CHARACTER VARYING (4) DEFAULT 'card',
FOREIGN KEY (order_id) REFERENCES orders (order_id),
FOREIGN KEY (courier_id) REFERENCES courier_info (courier_id)
);