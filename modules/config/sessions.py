#!/usr/bin/env python3

import os
import io
import sys

from modules.utils.dicts import DotNotation as DotNotation
import modules.utils.yaml as yaml

class SessionManager(object):
    """ Fermentation Session Manager Class

    Read Session Yaml file in 
    - ~/include-beer-sessions.yml
    or
    - ENV INCLUDE_BEER_SESSION_FILE (takes precedents)


    """

    def __init__(self, session_file=None):
        self.sessions = {}
        

        # If env INCLUDE_BEER_CONFIG_SESSION_FILE is set, always use that
        # elif try ~/include-beer.cfg
        # else return empty dict
        _expanded_user_file = os.path.expanduser('~/include-beer-sessions.yml')
        if os.getenv('INCLUDE_BEER_CONFIG_SESSION_FILE', 0):
            _env_file = os.environ['INCLUDE_BEER_CONFIG_SESSION_FILE']
            if os.path.exists(_env_file):
                self._session_file = _env_file
                self._use_session_file = True
        elif os.path.exists(_expanded_user_file):
            self._session_file = _expanded_user_file
            self._use_session_file = True
        else:
            self._use_session_file = False

        if self._use_session_file:

            # Load in our session yaml file
            self.sessions = yaml.yaml_loader(self._session_file)

    def _build_base_config(self, d):
        """Returns dictionaries of sections based on ini value

        Keyword arguments:
        - d(dict): dictionary of default defintions

        [ section1: { key: default, key: default }, section2: { key: default, key: default }]

        """
        _section_dicts = {}
        # loop on each default definition
        for _key in list(d):
            for _s in d[_key]['ini']:
                _section = _s['section']
                _option = _s['key']
                _default = d[_key]['default']
                _type = d[_key]['type']
                _section_dict = {_option: self._cast_value(_default, _type)}
                if _section in _section_dicts:
                    _section_dicts[_section].update(_section_dict)
                else:
                    _section_dicts[_section] = _section_dict
        return _section_dicts

    def _cast_value(self, value, value_type):
        """Return value cast as value_type

        Keyword arguments:
        - value: value to be cast
        - value_type: type to cast
        """
        if value is not None:
            if value_type == 'string':
                cast_value = str(value)

            elif value_type == "int":
                cast_value = int(value)

            elif value_type == "boolean":
                if value in ['True','False']:
                    cast_value = eval(value)
                else:
                    cast_value = value

            else:
                cast_value = value

        return cast_value

    def _ini_to_dict(self, ini_file):
        """Return INI file as dictionary object

        Keyword arguments:
        - ini_file(str): INI file to read and parse
        """
        cp = configparser.ConfigParser()
        cp.read(ini_file)
        _dict = {section: dict(cp.items(section)) for section in cp.sections()}
        return _dict

    def _build_option_type_def(self):
        """Return a dictionary of each option and its associated type

        Keyword arguments
        """
        _option_dict = {}
        _d = self._default_def
        for _key in list(_d):
            for _s in _d[_key]['ini']:
                _option = _s['key']
                _type = _d[_key]['type']
                _option_dict.update({_option: _type})
        self._option_type_def = _option_dict

    def _cast_dict_values(self, d):
        """Return dictionary with properly casted values

        Keyword arguments:
        - d(dict): dictionary to cast values in
        """
        _temp = {}
        for _section, _options in d.items():
            for _option, _value in d[_section].items():
                _type = self._option_type_def[_option]
                _option_dict = {_option: self._cast_value(_value, _type)}
                if _section in _temp:
                    _temp[_section].update(_option_dict)
                else:
                    _temp[_section] = _option_dict
        return _temp

    def _build_env_config(self, d):
        """Return dictionary of set ENV variables

        Keyword arguments:
        - d(dict): dictionary of default defintions
        """
        _env_dicts = {}
        for _s in list(d):
            _env_vars = d[_s]['env']
            _key = d[_s]['ini'][0]['key']
            _section = d[_s]['ini'][0]['section']
            _type = d[_s]['type']
            for _env_var in _env_vars:
                if os.getenv(_env_var['name'], 0):
                    _value = os.environ[_env_var['name']]
                    _entry = ({_key: self._cast_value(_value, _type)})
                    if _section in _env_dicts:
                        _env_dicts[_section].update(_entry)
                    else:
                        _env_dicts[_section] = _entry
        return _env_dicts

