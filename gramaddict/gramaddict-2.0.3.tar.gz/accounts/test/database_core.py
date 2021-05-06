import sqlite3

# from sqlite3 import Error


class SQLite:
    def __init__(self, file="GramAddict.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


class Tables:
    """tables definition for database"""

    def __init__(self):
        self.sql_create_accounts = """
        CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL);
        """

        self.sql_create_configuration = """
        CREATE TABLE IF NOT EXISTS configuration (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
        """

        self.sql_create_skip_reason = """
        CREATE TABLE IF NOT EXISTS skip_reason (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        reason TEXT NOT NULL);
        """

        self.sql_create_status = """
        CREATE TABLE IF NOT EXISTS status (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        datetime TEXT NOT NULL,
        n_posts INTEGER NOT NULL,
        n_followers INTEGER NOT NULL,
        n_following INTEGER NOT NULL);
        """

        self.sql_create_users_filtered = """
        CREATE TABLE IF NOT EXISTS users_filtered (
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
        CREATE TABLE IF NOT EXISTS bot_activity (
        id INTEGER NOT NULL,
        session_start TEXT NOT NULL,
        session_finish TEXT,
        session_length TEXT,
        total_interactions INTEGER,
        successful_interactions INTEGER,
        total_followed INTEGER,
        total_likes INTEGER,
        total_comments INTEGER,
        total_pm_sent INTEGER,
        total_watched INTEGER,
        total_unfollowed INTEGER,
        total_scraped INTEGER,
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
        CREATE TABLE IF NOT EXISTS followers (
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
        CREATE TABLE IF NOT EXISTS following (
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
        CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        liked INTEGER NOT NULL,
        watched INTEGER NOT NULL,
        followed INTEGER NOT NULL,
        commented INTEGER NOT NULL,
        pm_sent INTEGER NOT NULL,
        bot_activity_id INTEGER NOT NULL,
        users_filtered_id INTEGER NOT NULL,
        skip_reason_id INTEGER NOT NULL,        
        CONSTRAINT "skip_reason-actions"
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
        CREATE TABLE IF NOT EXISTS posts_insight (
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
        CREATE TABLE IF NOT EXISTS private_message (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        private_message TEXT NOT NULL,
        interactions_id INTEGER NOT NULL,CONSTRAINT "interactions-private_message"
        FOREIGN KEY (interactions_id)
        REFERENCES interactions(id));
        """

        self.sql_create_comments = """
        CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        comment TEXT,
        interactions_id INTEGER NOT NULL,CONSTRAINT "interactions-comments"
        FOREIGN KEY (interactions_id)
        REFERENCES interactions(id));
        """


def create_tables():
    TablesName = Tables()
    with SQLite() as cur:
        cur.execute(TablesName.sql_create_accounts)
        cur.execute(TablesName.sql_create_bot_activity)
        cur.execute(TablesName.sql_create_comments)
        cur.execute(TablesName.sql_create_configuration)
        cur.execute(TablesName.sql_create_followers)
        cur.execute(TablesName.sql_create_following)
        cur.execute(TablesName.sql_create_interactions)
        cur.execute(TablesName.sql_create_posts_insight)
        cur.execute(TablesName.sql_create_private_message)
        cur.execute(TablesName.sql_create_skip_reason)
        cur.execute(TablesName.sql_create_status)
        cur.execute(TablesName.sql_create_users_filtered)


def migrate_session():
    import json

    with open(r"la.samoana94/sessions.json", encoding="UTF-8") as json_data:
        d = json.load(json_data)
        for n in d:
            username = [
                "username",
            ]

            bot_activity = [
                "configuration_id",
                "my_account_id",
                "status_id",
                "session_start",
                "session_finish",
                "session_length",
                "total_interactions",
                "successful_interactions",
                "total_followed",
                "total_likes",
                "total_comments",
                "total_pm_sent",
                "total_watched",
                "total_unfollowed",
                "total_scraped",
            ]
            # someitem = n.get("id")
            query = "INSERT INTO bot_activity ({0}) values (?{1})"
            query = query.format(",".join(bot_activity), ",?" * (len(bot_activity) - 1))
            print(query)
            with SQLite() as cur:
                cur.execute(
                    query,
                    (
                        1,
                        1,
                        1,
                        n.get("start_time"),
                        n.get("finish_time"),
                        "0",
                        n.get("total_interactions"),
                        n.get("successful_interactions"),
                        n.get("total_followed"),
                        n.get("total_likes"),
                        n.get("total_comments"),
                        n.get("total_pm_sent"),
                        n.get("total_watched"),
                        n.get("total_unfollowed"),
                        "Null",
                    ),
                )

            # for data in columns():
            #     keys = tuple(data[c] for c in columns)
            #     with SQLite() as cur:
            #         cur.execute(query)


create_tables()
migrate_session()
