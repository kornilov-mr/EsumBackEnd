from configs.config import Config_holder
from database.connect import Connector


def set_problem_as_solved(problem_id: int, login: str):
    sql_get_user_id = """SELECT user_id FROM users WHERE login = %s"""
    sql_insert_in_relation = """INSERT INTO user_problem_relation (user_id, problem_id)
            VALUES(%s,%s)"""
    conn = Connector.get_connection()
    print(login)
    with conn.cursor() as cur:
        cur.execute(sql_get_user_id, (login,))
        user_id = cur.fetchone()
        print(user_id)
        cur.execute(sql_insert_in_relation, (user_id, problem_id))
        conn.commit()
