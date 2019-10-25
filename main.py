'''
Author: shuijing
Date: 2019-7
E-mail: 1134794665@qq.com
Last-Edit_Time: 2019-9-28
'''

import ctypes
import random
import os
import sys
import time


music_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "music")

try:
    os.mkdir(music_path)
except:
    pass

music_list = os.listdir(music_path)
music_list = list(filter(lambda x: x[-4:].lower() in (".mp3", ), music_list))

if len(music_list) == 0:
    print("音乐列表为空，请将音乐文件放在music文件夹中！")
    input("\n按回车键退出......")
    sys.exit(1)


# 顺序播放
def order_play():
    for i in music_list:
        print("正在播放 %s" % i) # 打印当前歌曲名
        ctypes.windll.winmm.mciSendStringW(r"open %s alias s" % os.path.join(music_path, i), None, 0, None) # 打开音乐文件并命名为 s
        ctypes.windll.winmm.mciSendStringW(r"play s", None, 0, None) # 播放
        input("\n按回车键播放下一首......")
        ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None) # 停止播放
        ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None) # 关闭当前音乐文件
        os.system("cls") # 清屏


# 随机播放
def random_play():
    music_name = random.choice(music_list) # 在音乐列表中随机选取一首歌曲
    music_url = os.path.join(music_path, music_name)
    print("正在播放 %s" % music_name) # 打印当前歌曲名
    ctypes.windll.winmm.mciSendStringW(r"open %s alias s" % music_url, None, 0, None) # 打开音乐文件并命名为 s
    ctypes.windll.winmm.mciSendStringW(r"play s", None, 0, None) # 循环播放
    input("\n按回车键播放下一首......")
    ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None) # 停止播放
    ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None) # 关闭当前音乐文件
    os.system("cls") # 清屏
    time.sleep(5)

def loop_playback():
    music_name = random.choice(music_list) # 在音乐列表中随机选取一首歌曲
    music_url = os.path.join(music_path, music_name)
    print("正在播放 %s" % music_name) # 打印当前歌曲名
    ctypes.windll.winmm.mciSendStringW(r"open %s alias s" % music_url, None, 0, None) # 打开音乐文件并命名为 s
    ctypes.windll.winmm.mciSendStringW(r"play s repeat", None, 0, None) # 循环播放
    input("\n按回车键播放下一首......")
    ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None) # 停止播放
    ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None) # 关闭当前音乐文件
    os.system("cls") # 清屏


while True:
    print("1.顺序播放\n2.随机播放\n3.循环播放")
    num = int(input("请选择播放方式(数字):\n"))
    if num == 1:
        order_play()
    elif num == 2:
        random_play()
    else:
        loop_playback()
    # music_name = random.choice(music_list) # 在音乐列表中随机选取一首歌曲
    # music_url = os.path.join(music_path, music_name)
    # l_old = 0
    # ctypes.windll.winmm.mciSendStringW(r"open %s alias s" % music_url, None, 0, None) # 打开音乐文件并命名为 s
    # # L = ctypes.windll.winmm.mciSendStringW(r"status s length", None, 0, None) # 获取当前音乐文件总长度
    # # print(L)
    # print("正在播放 %s" % music_name) # 打印当前歌曲名
    # ctypes.windll.winmm.mciSendStringW(r"play s", None, 0, None) # 循环播放
    
    # # l_new = ctypes.windll.winmm.mciSendStringW(r"status s position", music_url, len(music_url), 0) # 获取播放信息
    # # print(l_new)
    # # if left(music_url, 7) == "stopped": # 播放完毕
    # #     ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None) # 停止播放
    # # # if l_new > l_old:
    # #     print(l_new)
    # # l_old = l_new
    # input("\n按回车键播放下一首......")
    # ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None) # 停止播放
    # ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None) # 关闭当前音乐文件
    # os.system("cls") # 清屏
    # time.sleep(5)
    
