
use qr_secure_db;

-- Create the clients table
CREATE TABLE IF NOT EXISTS clients (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_name VARCHAR(100) NOT NULL,
    plot_no VARCHAR(50) NOT NULL,
    block VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    total_price INT NOT NULL,
    paid_amount INT NOT NULL,
    last_payment_date VARCHAR(20) NOT NULL,
    pin VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS admins (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE users (
    username VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100)
);

select * From users; 

-- Optional: insert sample admin
INSERT INTO admins (username, password)
VALUES ('admin', 'admin123');


SELECT * FROM clients;


