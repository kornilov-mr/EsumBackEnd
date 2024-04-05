class AccessDenied(Exception):
    reason: str = "User doesn't have rights to do it"
    def __init__(self):
        pass


class AdminKeyIsNotProvided(Exception):
    def __init__(self):
        pass


class JWTTokenCheckException(Exception):
    reason: str = "JWToken is not valid"
    def __int__(self):
        pass


class NotValidNameException(Exception):
    def __init__(self, login: str):
        self.login = login


class NotValidPasswordException(Exception):
    def __init__(self, password: str):
        self.password = password


class AlreadyExistedNameException(Exception):
    def __init__(self, login: str):
        self.login = login


class WrongPasswordException(Exception):
    def __init__(self, password: str):
        self.password = password


class WrongNameException(Exception):
    def __init__(self, login: str):
        self.login = login


class TokenIsNotProvided(Exception):
    def __init__(self):
        pass

class LoginDoesNotExist(Exception):
    def __init__(self):
        pass
