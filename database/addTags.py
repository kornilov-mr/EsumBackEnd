from connect import Connector
from TagEnum import Tags
def add_tags():
    sql = """INSERT INTO tags (name)
                VALUES(%s) """
    conn = Connector.get_connection()
    with conn.cursor() as cur:
        tags=[]
        for data in Tags:
            tags.append((data.name,))
            print(data.name)
        cur.executemany(sql,tags)
    conn.commit()


if __name__ == '__main__':
    add_tags()