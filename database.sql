CREATE DATABASE IF NOT EXISTS fastapi;
USE fastapi;

CREATE TABLE IF NOT EXISTS User (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(50) NOT NULL,
gender ENUM('male', 'female') NOT NULL,
roles ENUM('admin', 'user') NOT NULL
); 

INSERT INTO User (first_name, last_name, gender, roles) values ('Linus', 'Torvalds', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Bill', 'Gates', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Steve', 'Jobs', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('James', 'Gosling', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Nikola', 'Tesla', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Martin', 'Cooper', 'male', 'user');
INSERT INTO User (first_name, last_name, gender, roles) values ('Alan', 'Turing', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Ada', 'Lovelace', 'female', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Tim', 'Berners-Lee', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Sam', 'Altman', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Larry', 'Page', 'male', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Grace', 'Hopper', 'female', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Jean', 'Sammet', 'female', 'admin');
INSERT INTO User (first_name, last_name, gender, roles) values ('Konrad', 'Suze', 'male', 'admin');