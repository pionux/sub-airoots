#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <https://github.com/calamares> ===
#
#   Copyright 2015, Teo Mrnjavac <teo@kde.org>
#   Copyright 2017. Alf Gaida <agaida@siduction.org>
#   Copyright 2019, Adriaan de Groot <groot@kde.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import subprocess
import libcalamares

import gettext
_ = gettext.translation("calamares-python",
                        localedir=libcalamares.utils.gettext_path(),
                        languages=libcalamares.utils.gettext_languages(),
                        fallback=True).gettext


def pretty_name():
    return _("Remove live user from target system")


def run():
    """
    Remove live user from target system
    """
    username = libcalamares.job.configuration["username"]

    try:
        libcalamares.utils.check_target_env_call(["userdel", "-f", "-r", username])
        libcalamares.utils.check_target_env_call([" sed", "-i", "'s/echo/#ech~o/g'", "/boot/grub/grub.cfg"])
    except subprocess.CalledProcessError as e:
        libcalamares.utils.debug("Cannot remove user. "
                                 "'userdel' terminated with exit code "
                                 "{}.".format(e.returncode))
    return None
