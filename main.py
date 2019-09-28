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

while True:
    music_name = random.choice(music_list)
    print("正在播放 %s" % music_name)
    ctypes.windll.winmm.mciSendStringW(r"open %s alias s" % os.path.join(music_path, music_name), None, 0, None)
    ctypes.windll.winmm.mciSendStringW(r"play s repeat", None, 0, None) # 循环播放
    # ctypes.windll.winmm.mciSendStringW(r"stop %s alias s" % os.path.join(music_path, music_name), None, 0, None)

    input("\n按回车键播放下一首......")
    ctypes.windll.winmm.mciSendStringW(r"stop s", None, 0, None)
    ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None)
    os.system("cls")
    # if input("\n按回车键播放下一首......"):
    # ctypes.windll.winmm.mciSendStringW(r"stop %s alias s" % os.path.join(music_path, music_name), None, 0, None)
    #     continue
    
