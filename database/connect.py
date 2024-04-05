import psycopg2
from configs.config import Config_holder


class Connector():
    connection = None

    @staticmethod
    def get_connection():
        if Connector.connection == None:
            Connector.connection = Connector.connect()
        return Connector.connection

    @staticmethod
    def connect():
        config = Config_holder.get_config()["database"]
        try:
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)


