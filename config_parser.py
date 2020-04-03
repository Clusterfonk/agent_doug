import configparser


class BotConfigParser:
    def __init__(self, ini_path):
        self.__parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.__parser.read(ini_path)

    def get_bot_name(self):
        return self.__parser['Default']['name']

    def get_bot_icon_url(self):
        return self.__parser['Default']['icon_url']

    def get_prefix(self):
        return self.__parser['Default']['prefix']

    def get_bot_description(self):
        return self.__parser['Default']['description']

    def get_help_description(self):
        return self.__parser['Help']['description']

    def get_log_channel(self):
        return self.__parser['Logging']['channel_name']

    def get_default_role(self):
        return self.__parser['Roles']['default_role']

