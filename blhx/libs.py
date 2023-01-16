# -*- coding: utf-8 -*-

# 加载API
from mcdreforged.api.all import *
from blhx import *

# 直播间ID的取值,看直播间URL
# 例子：https://live.bilibili.com/13007212 ,其中13007212就是直播间ID
# 支持多个直播间轮询
INIT_ROOMS = []
ROOM_IDS = []

# 打印版本信息
def print_ver(src: CommandSource):
    src.reply('您已成功安装blhx')
    src.reply('该Blhx版本号为：2.7')
    src.reply('请使用!!help 获取相关帮助')
    return 0


# 添加房间 
def add_live_room(roomid, src: CommandSource):
    
    for item_id in ROOM_IDS:
        if item_id == roomid:
            src.reply("已存在")
            return 0
        else:
            ROOM_IDS.append(roomid)  ## 使用 append() 添加元素
            src.reply('已添加')
            return 0

    if ROOM_IDS == INIT_ROOMS:
        ROOM_IDS.append(roomid)  
        src.reply('已添加')
        return 0
    else:
        src.reply("未知错误")
        return 0

# 删除房间
def del_live_room(count, src: CommandSource):
    if ROOM_IDS == INIT_ROOMS:
        src.reply("无房间")
    else:
        if ROOM_IDS[count] in ROOM_IDS:
            del ROOM_IDS[count]  ## 使用del删除元素
            src.reply('已删除') 
        else:
            src.reply('未知房间')


# 遍历房间列表
def get_room_list(src: CommandSource):
    room_num = -1
    if ROOM_IDS == INIT_ROOMS:
        src.reply("无房间")
    else:
        for item_id in ROOM_IDS:
                room_num = room_num + 1
                src.reply(
                    "房间号：[" + str(room_num) + "]" + "  |  房间ID："+ str(item_id))  # 遍历List
                
def room_start_sync(src: CommandSource):
    src.reply("start debuger")

def room_stop_sync(src):
    src.reply("stop debuger")


def room_reload_sync(src):
    src.reply("reload debuger")

