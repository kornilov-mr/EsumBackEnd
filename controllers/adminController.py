import sys

sys.path.append('../controllers')

from database.connect import Connector


def add_new_problem(name: str, description: str, tags: list[str]):
    sqlSELECT = """SELECT tag_id from tags WHERE name IN %s"""

    sqlInsert = """INSERT INTO problems (name , description)
            VALUES(%s, %s) RETURNING problem_id"""
    sqlManyToMany = """INSERT INTO problem_tag_relation (problem_id,tag_id)
            VALUES(%s,%s)"""
    conn = Connector.get_connection()
    with conn.cursor() as cur:
        cur.execute(sqlSELECT, (tuple(tags),))
        tags_id = cur.fetchall()

        data = (name, description)
        cur.execute(sqlInsert, data)
        problem_id = cur.fetchone()

        print(tags_id)
        for tag_id in tags_id:
            cur.execute(sqlManyToMany, (problem_id, tag_id,))
        conn.commit()
