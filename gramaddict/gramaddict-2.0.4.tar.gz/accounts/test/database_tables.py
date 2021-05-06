class Tables:
    """tables definition for database"""

    def __init__(self):
        self.sql_create_accounts = """
        CREATE TABLE accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL);
        """

        self.sql_create_configuration = """
        CREATE TABLE configuration (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
        """

        self.sql_create_skip_reason = """
        CREATE TABLE skip_reason (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        reason TEXT NOT NULL);
        """

        self.sql_create_status = """
        CREATE TABLE status (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        datetime TEXT NOT NULL,
        n_posts INTEGER NOT NULL,
        n_followers INTEGER NOT NULL,
        n_following INTEGER NOT NULL);
        """

        self.sql_create_users_filtered = """
        CREATE TABLE users_filtered (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nickname TEXT NOT NULL,
        full_name TEXT,
        biography TEXT,
        n_following INTEGER NOT NULL,
        n_followers INTEGER NOT NULL,
        n_posts INTEGER NOT NULL,
        ratio REAL NOT NULL);
        """

        self.sql_create_bot_activity = """
        CREATE TABLE bot_activity (
        id INTEGER NOT NULL,
        session_start TEXT NOT NULL,
        session_finish TEXT,
        session_length TEXT,
        configuration_id INTEGER NOT NULL,
        my_account_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,CONSTRAINT "configuration-bot_activity"
        FOREIGN KEY (configuration_id)
        REFERENCES configuration(id)
        ,CONSTRAINT "my_account-bot_activity"
        FOREIGN KEY (my_account_id)
        REFERENCES accounts(id)
        ,CONSTRAINT "status-bot_activity"
        FOREIGN KEY (status_id)
        REFERENCES status(id),
        PRIMARY KEY(id));
        """

        self.sql_create_followers = """
        CREATE TABLE followers (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        status_id INTEGER NOT NULL,
        nickname TEXT NOT NULL,
        n_posts INTEGER NOT NULL,
        n_followers INTEGER NOT NULL,
        n_following INTEGER NOT NULL,
        ratio REAL NOT NULL,CONSTRAINT "status-followers"
        FOREIGN KEY (status_id)
        REFERENCES status(id));
        """

        self.sql_create_following = """
        CREATE TABLE following (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        status_id INTEGER NOT NULL,
        nickname TEXT NOT NULL,
        n_posts INTEGER NOT NULL,
        n_followers INTEGER NOT NULL,
        n_following INTEGER NOT NULL,
        ratio REAL NOT NULL,
        is_following_you INTEGER NOT NULL,CONSTRAINT "status-following"
        FOREIGN KEY (status_id)
        REFERENCES status(id));
        """

        self.sql_create_interactions = """
        CREATE TABLE interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        datetime TEXT NOT NULL,
        bot_activity_id INTEGER NOT NULL,
        users_filtered_id INTEGER NOT NULL,
        skip_reason_id INTEGER NOT NULL,
        liked INTEGER NOT NULL,
        watched INTEGER NOT NULL,
        followed INTEGER NOT NULL,
        commented INTEGER NOT NULL,CONSTRAINT "skip_reason-actions"
        FOREIGN KEY (skip_reason_id)
        REFERENCES skip_reason(id)
        ,CONSTRAINT "bot_activity-interactions"
        FOREIGN KEY (bot_activity_id)
        REFERENCES bot_activity(id)
        ,CONSTRAINT "users_filtered-interactions"
        FOREIGN KEY (users_filtered_id)
        REFERENCES users_filtered(id));
        """

        self.sql_create_posts_insight = """
        CREATE TABLE posts_insight (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        status_id INTEGER NOT NULL,
        likes INTEGER NOT NULL,
        comments INTEGER NOT NULL,
        sent INTEGER NOT NULL,
        bookmark INTEGER NOT NULL,
        profile_visits INTEGER NOT NULL,
        follows INTEGER NOT NULL,
        reach INTEGER NOT NULL,
        impressions INTEGER NOT NULL,
        from_home INTEGER NOT NULL,
        from_profile INTEGER NOT NULL,
        from_hashtags INTEGER NOT NULL,
        from_other INTEGER NOT NULL,CONSTRAINT "status-post_insight"
        FOREIGN KEY (status_id)
        REFERENCES status(id));
        """

        self.sql_create_private_message = """
        CREATE TABLE private_message (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        private_message TEXT NOT NULL,
        interactions_id INTEGER NOT NULL,CONSTRAINT "interactions-private_message"
        FOREIGN KEY (interactions_id)
        REFERENCES interactions(id));
        """

        self.sql_create_comments = """
        CREATE TABLE comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        comment TEXT,
        interactions_id INTEGER NOT NULL,CONSTRAINT "interactions-comments"
        FOREIGN KEY (interactions_id)
        REFERENCES interactions(id));
        """
