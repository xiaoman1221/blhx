# -*- coding: utf-8 -*-

# Loading API
from mcdreforged.api.all import *
# Loading Class And Function
from blhx import *
from blhx.command import *
from blhx.libs import *


# Loading (on_load)
def on_load(server: PluginServerInterface, prev_module):
    # 判断是否重载
    if prev_module is None:
        server.logger.info(server.tr('main_msg.load_message'))
        add_help_command(server)
        # Build Command
        add_command(server)
    else:
        server.logger.info(server.tr('main_msg.reload_message'))
        server.say(server.tr('main_msg.reload_message'))
        add_help_command(server)
        # Build Command
        add_command(server)
