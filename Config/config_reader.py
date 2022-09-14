import configparser
import os


class ConfigReader:
    def __init__(self, path=None):
        self.config = configparser.ConfigParser()
        if path is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.cfg")
        self.config.read(path)

    def get_base_url(self) -> str:
        return self.config.get("Mocked", "url")