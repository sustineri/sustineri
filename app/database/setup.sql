CREATE DATABASE sustineri;

CREATE TABLE users (
    user_id INT NOT NULL,
    username NVARCHAR(50) NOT NULL,
    password CHAR(64) NOT NULL, --SHA256

    PRIMARY KEY (user_id)
);

CREATE TABLE receipts (
    receipt_id INT NOT NULL,
    upload_date DATE NOT NULL
    user_id INT NOT NULL,

    PRIMARY KEY (receipt_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE items (
    item_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    amount DECIMAL(12,4) NOT NULL,
    gwp DECIMAL(12, 4) NOT NULL,
    receipt_id INT NOT NULL,

    PRIMARY KEY (item_id),
    FOREIGN KEY (receipt_id) REFERENCES receipts(receipt_id)
);
