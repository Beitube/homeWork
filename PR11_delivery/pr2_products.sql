CREATE TABLE products (
product_id SERIAL PRIMARY KEY,
menu_name CHARACTER VARYING (25) NOT NULL, 
price DECIMAL (10,2),
weight SMALLINT
);
