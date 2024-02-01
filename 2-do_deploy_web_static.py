#!/usr/bin/python3
# waaw.
import os.path
from fabric.api import put, env, run


env.hosts = ["54.236.53.177", "52.201.211.59"]

def do_deploy(archive_path):
    """dep"""
    
    if os.path.isfile(archive_path) is False:
        return False
    
    malaf = archive_path.split("/")[-1]
    asm = malaf.split(".")[0]

    if put(archive_path, "/tmp/{}".format(malaf)).failed is True:
        return False
    
    if run("rm -rf /data/web_static/releases/{}/".
           format(asm)).failed is True:
        return False
    
    if run("mkdir -p /data/web_static/releases/{}/".
           format(asm)).failed is True:
        return False
    
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(malaf, asm)).failed is True:
        return False
    
    if run("rm /tmp/{}".format(malaf)).failed is True:
        return False
    
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(asm, asm)).failed is True:
        return False
    
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(asm)).failed is True:
        return False
    
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(asm)).failed is True:
        return False
    
    return True
