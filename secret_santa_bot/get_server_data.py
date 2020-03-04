import ConfigParser
import os
import io


def parse_config_file():
    with open(os.path.join(os.path.dirname(__file__), 'config.ini'), 'r') as config_file:
        config = config_file.read()
    config_parser = ConfigParser.RawConfigParser(allow_no_value=True)
    config_parser.readfp(io.BytesIO(config))
    config_params = {}
    for param in config_parser.sections():
        if param == 'guild':
            for option in config_parser.options(param):
                if option == 'id':
                    config_params['id'] = config_parser.get(param, option)
                elif option == 'token':
                    config_params['token'] = config_parser.get(param, option)
                elif option == 'role':
                    config_params['role'] = config_parser.get(param, option)
                elif option == 'retired_role':
                    config_params['retired_role'] = config_parser.get(param, option)
        elif param == 'messages':
            for option in config_parser.options(param):
                if option == 'santa_message':
                    config_params['santa_message'] = config_parser.get(param, option)
                elif option == 'add_santa':
                    config_params['add_santa'] = config_parser.get(param, option)
                elif option == 'retired_santa':
                    config_params['retired_santa'] = config_parser.get(param, option)
                elif option == 'already_retired':
                    config_params['already_retired'] = config_parser.get(param, option)
                elif option == 'list_of_retirees':
                    config_params['list_of_retirees'] = config_parser.get(param, option)
    return config_params
