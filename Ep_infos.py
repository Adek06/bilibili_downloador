from selenium import webdriver
from re import findall, sub
from time import sleep
import requests

class Ep_info(object):

    def __init__(self,html):

        self.html = html

    def bilibili_Ep_info(self):
        text = self.open_Web()
        Ep_info_rep = findall(r"bangumi.bilibili.com/anime/\d{2,}/play#\d{2,}",text)
        Ep_info_list = []
        print("浏览器正常关闭...")
        for i in Ep_info_rep:
            if i not in Ep_info_list:
                Ep_info_list.append(i)
        print("目前一共有"+str(len(Ep_info_list))+"集")
        return Ep_info_list
    '''
    def bilibili_Set_info(self):
        text = self.open_Web()
        Set_nums_str = findall(r"totalpage = '\d{,3}'",text)
        Set_nums = sub("\D", "", Set_nums_str[0])
        Set_list = []
        for i in range(int(Set_nums)):
            Set_list.append(self.html+"#page="+str(i+1))
        print("这个合集一共有{}个视频".format(len(Set_list)))
        return Set_nums,Set_list
    '''
    def bilibili_Set_info(self):
        response = requests.get(self.html)
        Set_list_str = findall(r"/video/av\d{,10}/index_\d{1,3}.html",response.text)
        #print(Set_list_str)
        Set_list = []
        for i in range(len(Set_list_str)):
            url = "https://www.bilibili.com"+Set_list_str[i]
            Set_list.append(url)
        print("这个合集一共有{}个视频".format(len(Set_list_str)))
        return len(Set_list),Set_list

    def open_Web(self):
        print('正在打开浏览器寻找下载地址，请稍等...')
        driver = webdriver.Firefox()
        try:
            driver.get(self.html)
        except:
            print("打开浏览器这里出了问题")
            exit()
        sleep(5)
        text = driver.page_source
        driver.close
        return text
