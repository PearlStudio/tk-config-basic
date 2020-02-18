# -*- coding: utf-8 -*-

name = 'tk_config_basic'

version = "1.3.2"

description = 'Based on tk-config-basic'

authors = ['']

tools = []

requires = []

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.TK_CONFIG_BASIC_ROOT = "{root}"


format_version = 2
