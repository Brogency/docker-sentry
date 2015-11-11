# -*- coding: utf-8 -*-
from fabric.api import local

def build():
    local("docker build -t sentry-core .")
