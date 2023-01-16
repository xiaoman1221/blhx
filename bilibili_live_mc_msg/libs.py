# -*- coding: utf-8 -*-

# 加载API
from mcdreforged.api.all import *
# from bilibili_live_mc_msg import blivedm
from bilibili_live_mc_msg import *

# 加载依赖
import asyncio
import random
import time
# 直播间ID的取值,看直播间URL
# 例子：https://live.bilibili.com/13007212 ,其中13007212就是直播间ID
# 支持多个直播间轮询
INIT_ROOMS = []
ROOM_IDS = []

# 指令树相关
def print_help_message(src: CommandSource):
    src.reply('帮助占位符')
    return True


def print_unknown_argument_message(src: CommandSource):
    src.reply('未知帮助信息')


# 添加房间 
def add_live_room(roomid, src: CommandSource):
    
    for item_id in ROOM_IDS:
        # src.reply(item_id)
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
    run_sync_main(src)
    src.reply("开始了")

def room_stop_sync(src, live_status):
    if live_status == True:
        live_status == False
        src.reply("结束了")
    else:
        src.reply("未运行")


def room_reload_sync(src, live_status):
    if live_status == True:
        src.reply("正在重新加载")
        live_status == False
        live_status == True
        src.reply("重新加载成功")
    else:
        src.reply("未运行")


# 主程序 
@new_thread("Sync Start!")
def run_sync_main(src):
    while True:
        src.reply("Sync Ses")
        time.sleep(1)
        