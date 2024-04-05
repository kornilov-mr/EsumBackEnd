import sys

sys.path.append('../controllers')

import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database.connect import Connector
from configs.config import Config_holder


def get_user_by_name(login: str):
    sql = "SELECT login, password, role from users WHERE login = (%s)"
    conn = Connector.get_connection()
    with conn.cursor() as cur:
        data = (login,)
        cur.execute(sql, data)
        user_found = cur.fetchone()
        return user_found


def get_hashed_password(password: str):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.hash(password)


def verify_password(password_from_database: str, password_from_token: str):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.verify(password_from_database, password_from_token)


def create_new_access_JWToken(login: str, password: str, role: str):
    config = Config_holder.get_config()
    algorithm = Config_holder.get_config()["hash_algorythm"]["algorythm"]
    expires_delta = datetime.now() + timedelta(minutes=int(config["JWToken"]["access_token_expire_minutes"]))

    to_encode = {"exp": expires_delta, "login": login, "password": get_hashed_password(password), "role": role}
    encoded_jwt = jwt.encode(to_encode, config["secret_keys"]["jwt_key"], algorithm=algorithm)
    return encoded_jwt


def read_pay_load(token: str):
    config = Config_holder.get_config()
    algorithm = config["hash_algorythm"]["algorythm"]
    return jwt.decode(token, config["secret_keys"]["jwt_key"], algorithms=algorithm)


def check_JTWToken(token: str):
    try:
        pay_load = read_pay_load(token)
    except:
        return False

    user = get_user_by_name(pay_load["login"])
    if user is None:
        return False
    if verify_password(user[1], pay_load["password"]) is False:
        return False

    return create_new_access_JWToken(pay_load["login"], user[1], pay_load["role"])
