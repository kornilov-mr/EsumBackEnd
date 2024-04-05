from configparser import ConfigParser
import os


class Config_holder():
    config: dict | None = None

    @staticmethod
    def get_config():
        if Config_holder.config is None:
            Config_holder.config = dict()
            Config_holder.load_config()
        return Config_holder.config

    @staticmethod
    def load_config():
        Config_holder.config["database"] = load_config(filename='database.ini', section='postgresql')
        Config_holder.config["secret_keys"] = load_config(filename='hash.ini', section='secret_keys')
        Config_holder.config["hash_algorythm"] = load_config(filename='hash.ini', section='hash_algorythm')
        Config_holder.config["JWToken"] = load_config(filename='hash.ini', section='JWToken')


def load_config(filename, section):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'configs', filename)
    parser = ConfigParser()
    parser.read(file_path)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config
