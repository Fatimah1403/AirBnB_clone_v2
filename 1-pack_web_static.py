#!/usr/bin/python3
from fabric.api import local, run, put
from datetime import datetime
import os
from time import strftime
def do_pack():
    """ A Fabric script that generates a .tgz archive
    from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(path))
        return path
    except Exception as e:
        return None
