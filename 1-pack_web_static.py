#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    date = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(date))

        return "versions/web_static_{}.tgz".format(date)

    except Exception as e:
        return None
