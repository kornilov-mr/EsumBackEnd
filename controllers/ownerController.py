from configs.config import Config_holder
from database.connect import Connector


def set_admin(login: str):
    sql = "UPDATE users SET role = %s WHERE login = %s"
    conn = Connector.get_connection()
    print(login)
    with conn.cursor() as cur:
        data = ("admin", login)
        cur.execute(sql, data)
    conn.commit()