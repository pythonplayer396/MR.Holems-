# ORIGINAL CREATOR: darkwall
# AUTHOR: darkwall
# Copyright (C) 2025 darkwall
# License: GNU General Public License v3.0

from configparser import ConfigParser

class Check:

    @staticmethod 
    def WhoIs():
        api = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(api)
        Key = Parser["Settings"]["Api_Key"]
        return Key