#!/usr/bin/python3

import os
import re

def get_anime_id(anime_path):
    try:
        get_id = ((re.search(r'\b#\d{2,}\b',anime_path)).group(0))[1:]
        anime_id = int(get_id)
        return anime_id

    except AttributeError:
        print('请确认这是B站番组计划的动漫')
        exit()

def get_down_anime_path(anime_path):
    down_anime_path = (re.match(r'\bhttp.{1,}#\b',anime_path)).group(0)
    return down_anime_path

def download_anime(char_get_anime_id,anime_path,char_get_down_anime_path,epsolde_num):
    for i in range(epsolde_num):
        try:
            download_path = char_get_down_anime_path + str(char_get_anime_id)
            os.system('you-get ' + download_path )
            char_get_anime_id += 1
            download_path = ''
            i += 1
        except IndentationError:
            print('下载完了！')
            break

def call_of_app():

    print("好的，不下了")
    exit()

os.chdir("/home/adek06/Videos")

try:
    print("请输入需要下载的番组计划动漫的名字")
    anime_name = input()
    file_path = os.getcwd()+'/'+anime_name
    os.mkdir(file_path)
    os.chdir(file_path)

except EOFError:
    call_of_app()

try:    
    print("请输入需要下载的网址")
    anime_path = input()

except EOFError:
    call_of_app()

try:
    print("请输入需要下载的集数")
    anime_epsolde = input()

char_get_anime_id = get_anime_id(anime_path)

char_get_down_anime_path = get_down_anime_path(anime_path)

download_anime(char_get_anime_id,anime_path,char_get_down_anime_path,anime_epsolde)
