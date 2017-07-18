from selenium import webdriver
from re import findall
from time import sleep

class Ep_info(object):

    def __init__(self,html):
        self.html = html

    def bilibili_Ep_info(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.html)
        except:
            print("打开浏览器这里出了问题")
        print('在全力打开中，请稍等...')
        sleep(5)
        Ep_info_rep = findall(r"bangumi.bilibili.com/anime/\d{2,}/play#\d{2,}",driver.page_source)
        Ep_info_list = []
        for i in Ep_info_rep:
            if i not in Ep_info_list:
                Ep_info_list.append(i)
        print("目前一共有"+str(len(Ep_info_list))+"集")
        return Ep_info_list