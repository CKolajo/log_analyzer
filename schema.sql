-- schema.sql
-- Creates a simple user login table for SQL Injection lab

DROP TABLE IF EXISTS login_users;

CREATE TABLE login_users (
	id SERIAL PRIMARY KEY,
	username TEXT NOT NULL,
	password TEXT NOT NULL);

-- Optional: insert test users
INSERT INTO login_users (username, password)
VALUES
('alice', 'wonderland'),
('bob', 'builder'),
('admin', 'admin');
