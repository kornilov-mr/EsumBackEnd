from connect import Connector

def create_tables():
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            login VARCHAR(127) NOT NULL,
            password VARCHAR(127) NOT NULL,
            role VARCHAR(127) DEFAULT 'user'
        )
        """
        ,
        """
        CREATE TABLE problems (
            problem_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(1000) NOT NULL
        )
        """
        ,
        """
        CREATE TABLE user_problem_relation (
            user_id INTEGER NOT NULL,
            problem_id INTEGER NOT NULL,
            PRIMARY KEY (user_id, problem_id),
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (problem_id)
                REFERENCES problems (problem_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE tags(
            tag_id SERIAL PRIMARY KEY,
            name VARCHAR(127) NOT NULL
        )
        """,
        """
        CREATE TABLE problem_tag_relation(
            problem_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (problem_id, tag_id),
            FOREIGN KEY (problem_id)
                REFERENCES problems (problem_id)
                ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (tag_id)
                REFERENCES tags (tag_id)
                ON DELETE CASCADE ON UPDATE CASCADE
        )
        """
    )
    conn = Connector.get_connection()
    with conn.cursor() as cur:
        for command in commands:
            cur.execute(command)
    conn.commit()


if __name__ == '__main__':
    create_tables()