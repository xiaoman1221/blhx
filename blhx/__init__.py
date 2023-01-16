# -*- coding: utf-8 -*-

from mcdreforged.api.all import PluginServerInterface
from blhx.command import add_command, add_help_command


def on_load(server: PluginServerInterface, prev_module):

    if prev_module is None:
        server.logger.info(server.tr('main_msg.load_message'))
        add_help_command(server)
        add_command(server)
    else:
        server.say(server.tr('main_msg.reload_message'))
        add_help_command(server)
        add_command(server)

