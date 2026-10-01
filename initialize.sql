
USE vdv9yr_media;
CREATE TABLE users(
   user_id INT PRIMARY KEY AUTO_INCREMENT,
   username VARCHAR(255) NOT NULL,
   account_number VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL
);
CREATE TABLE posts(
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    post_location VARCHAR(255) NOT NULL,
    post_content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users(username, account_number, email)
VALUES ('funny_dog', '01', 'funny_dog@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('funny_cat', '02', 'funny_cat@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('mad_dog', '03', 'mad_dog@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('mad_cat', '04', 'mad_cat@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('cute_dog', '05', 'cute_dog@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('cute_cat', '06', 'cute_cat@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('silly_dog', '07', 'silly_dog@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('silly_cat', '08', 'silly_cat@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('happy_dog', '09', 'happy_dog@gmail.com');

INSERT INTO users(username, account_number, email)
VALUES ('happy_cat', '10', 'happy_cat@gmail.com');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (1, 'Charlottesville, VA', 'Just saw the funniest dog on my walk.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (2, 'New York, NY', 'My cat has officially taken over my bed.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (3, 'Austin, TX', 'Anyone else having a ridiculously long day?');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (4, 'Seattle, WA', 'Finally got around to cleaning my apartment.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (5, 'Denver, CO', 'The weather is perfect for a hike today.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (6, 'Boston, MA', 'Found an amazing little coffee shop downtown.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (7, 'Chicago, IL', 'This sunset was absolutely incredible.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (8, 'San Diego, CA', 'Trying a new recipe tonight. Wish me luck!');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (9, 'Portland, OR', 'My dog refused to come inside because he was having too much fun.');

INSERT INTO posts(user_id, post_location, post_content)
VALUES (10, 'Miami, FL', 'Spent the afternoon at the beach and it was perfect.');