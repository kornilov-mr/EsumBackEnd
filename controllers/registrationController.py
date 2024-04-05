import sys
sys.path.append('../controllers')

from database.connect import Connector
from configs.config import Config_holder
from passlib.context import CryptContext

def insert_user(login: str, password: str):
    sql = """INSERT INTO users (login , password)
             VALUES(%s, %s) RETURNING user_id;"""
    config = Config_holder.get_config()

    conn = Connector.get_connection()
    with conn.cursor() as cur:
        data = (login, password)
        cur.execute(sql, data)
        conn.commit()


def check_if_name_already_exist(login: str):
    sql = "SELECT login from users WHERE login = (%s)"
    conn = Connector.get_connection()
    with conn.cursor() as cur:
        data = (login,)
        cur.execute(sql, data)
        name_found= cur.fetchone()
        if name_found is not None:
            return True
        else:
            return False

