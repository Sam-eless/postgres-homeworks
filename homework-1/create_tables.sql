CREATE TABLE employees
(
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date varchar(100),
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)

);

CREATE TABLE orders
(
	order_id varchar(100) PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id) NOT NULL,
	employee_id varchar(100),
	order_date varchar(100),
	ship_city varchar(100)
);

SELECT * FROM employees;
SELECT * FROM customers;
SELECT * FROM orders;