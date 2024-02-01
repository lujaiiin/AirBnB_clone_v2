#!/usr/bin/python3
# archive
from datetime import datetime
from fabric.api import local
import os.path as oo


def do_pack():
    """Create a tar archive"""

    date = datetime.utcnow()
    filee = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)
    if oo.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(filee)).failed is True:
        return None

    return filee
