#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py)
# that distributes an archive to your web servers

from fabric.api import *
from datetime import datetime
import os

env.hosts = []
env.user = 'ubuntu'
env.key_filename - '~/.ssh/school'


def do_deploy(archive_path):
    """Upload the archive to the /tmp/ directory of the web server """
    try:
        if not (path.exits(archive_path)):
            return False
        put(archive_path, '/tmp/')

        time_stamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/\
web_static_{}'.format(time_stamp))
        # Uncompress the archive to the folder /data/web_static/releases/
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'.format(time_stamp, time_stamp))
        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(time_stamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(time_stamp, time_stamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'.format(time_stamp))
        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-create symbolic link
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(time_stamp))
    except Exception as e:
        return false
    return True
