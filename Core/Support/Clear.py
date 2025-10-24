# ORIGINAL CREATOR: darkwall
# AUTHOR: darkwall
# Copyright (C) 2025 darkwall
# License: GNU General Public License v3.0

import os

Windows = "nt"


class Screen:

    def Clear():
        os.system("cls" if os.name == Windows else "clear")
