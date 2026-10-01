SELECT
    users.username,
    posts.post_content,
    posts.post_location,
    posts.created_at
FROM users
JOIN posts ON users.user_id = posts.user_id
WHERE users.username = 'funny_dog';