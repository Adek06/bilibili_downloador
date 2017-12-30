from os import system, chdir, remove, getcwd
from os import name as systemName
import sys
from you_get import common as you_get
import multiprocessing as mp
from glob import glob

class Download(object):

    def __init__(self,Ep_info_list):
        self.Ep_info_list = Ep_info_list

    def clearTerminal(self):
        if systemName =='nt':
            system('cls')
        elif systemName == 'posix':
            system('clear')

    def creatDict(self,listT,st,end):
        dictT = {}
        for i,j in zip(range(st,end+1),listT):
            dictT[i] = j

        return dictT

    def use_youget(self,down_url_dict):
        redownDict={}
        for i in list(down_url_dict.keys()):
            try:
                sys.argv=['you-get',down_url_dict[i]]
                you_get.main()
                self.clearTerminal()
            except:
                print("""


                """)
                print("下载{}的过程出了点问题，稍后会重新下载".format(down_url_dict[i]))
                print("""


                """)
                redownDict[i] = down_url_dict[i]
        return redownDict





    def down_load(self):
        print("请问要从第几集开始下载？")
        startEp_id = int(input(">>> "))
        print("要下载到第几集？")
        endEp_id = int(input(">>> "))
        down_list = self.Ep_info_list[startEp_id-1:endEp_id]
        down_dict = self.creatDict(down_list,startEp_id,endEp_id)
        print("马上开始下载，请稍后...")

        redown = self.use_youget(down_dict)
        tryNum = 0
        while len(redown) != 0 and tryNum < 5:
            redown = self.use_youget(redown)
            tryNum += 1
        
        self.clearTerminal()
        if len(redown)>1:
            print("对不起，下载无能为力，请等以后的版本")
            print("没能下载的有一下几集：")
            print(str(redown))
        removeList = glob(r"./*.xml")
        for x in removeList:
            remove(x)
        print("下载好的文件放在在这里了：{}".format(getcwd()))
        print("""
    ##################################################################
    ####                                                          ####
    ####                                                          ####
    ####                                                          ####
    ####                   下载已经完成                           ####
    ####                                                          ####
    ####                  按回车键退出程序                        ####
    ####                                                          ####
    ####                                                          ####
    ##################################################################
        """)
        input()
