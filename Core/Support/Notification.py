# ORIGINAL CREATOR: darkwall
# AUTHOR: darkwall
# Copyright (C) 2025 darkwall
# License: GNU General Public License v3.0

import os

class Notifier:

    @staticmethod
    def Start(Mode):
        if Mode == "Desktop":
            if os.name == "nt":
                pass
            else:
                os.system("java Core/Support/Notification/Notification.java")
        else:
            pass