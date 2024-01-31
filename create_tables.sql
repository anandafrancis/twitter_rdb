-- Create TWEET table
CREATE TABLE TWEET (
    tweet_id INT PRIMARY KEY,
    user_id INT,
    tweet_ts DATETIME,
    tweet_text VARCHAR(140),
    FOREIGN KEY (user_id) REFERENCES FOLLOWS(user_id)
);

-- Create FOLLOWS table
CREATE TABLE FOLLOWS (
    user_id INT,
    follows_id INT,
    PRIMARY KEY (user_id, follows_id),
    FOREIGN KEY (user_id) REFERENCES TWEET(user_id),
    FOREIGN KEY (follows_id) REFERENCES TWEET(user_id)
);

-- Show the tables created
SHOW TABLES STATUS;
