import configparser


class BotConfigParser:
    def __init__(self, ini_path):
        self.__parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.__parser.read(ini_path)

    def get_bot_name(self):
        return self.__parser.get('Default', 'name')

    def get_bot_icon_url(self):
        return self.__parser.get('Default', 'icon_url')

    def get_prefix(self):
        return self.__parser.get('Default', 'prefix')

    def get_bot_description(self):
        return self.__parser.get('Default', 'description')

    def get_help_description(self):
        return self.__parser.get('Help', 'description')

    def get_log_channel(self):
        return self.__parser.get('Logging', 'channel_name')

    def get_new_member_role_id(self):
        return self.__parser.getint('Roles', 'new_member_id')

    def get_default_role_id(self):
        return self.__parser.getint('Roles', 'default_id')
