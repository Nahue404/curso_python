CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users(username, password) VALUES ('user1', 'password1');
INSERT INTO users(username, password) VALUES ('user2', 'password2');
INSERT INTO users(username, password) VALUES ('user3', 'password3');

select * from users u;
