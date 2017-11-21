from os import system, chdir, remove, getcwd
import sys
from you_get import common as you_get
import multiprocessing as mp
from glob import glob

class Download(object):

    def __init__(self,Ep_info_list):
        self.Ep_info_list = Ep_info_list
        #self.Ep_name = Ep_name

    def use_youget(self,down_url_list):
        redown=[]
        for i in range(len(down_url_list)):
            try:
                sys.argv=['you-get',down_url_list[i]]
                you_get.main()
                system('cls')
            except:
                print("""


                """)
                print("下载{}的过程出了点问题，稍后会重新下载".format(down_url_list[i]))
                print("""


                """)
                redown.append(down_url_list[i])
        return redown


    def down_load(self):
        print("请问要从第几集开始下载？")
        startEp_id = input(">>> ")
        print("要下载到第几集？")
        endEp_id = input(">>> ")
        down_list = self.Ep_info_list[int(startEp_id)-1:int(endEp_id)]
        print("马上开始下载，请稍后...")
        #chdir('.\EP')
        #chdir(str(self.Ep_name))

        redown = self.use_youget(down_list)
        tryNum = 0
        while len(redown) != 0 and tryNum < 5:
            redown = self.use_youget(redown)
            tryNum += 1
        
        
        '''
        down_list1=[]
        down_list2=[]

        for i in range(len(down_list)):
            if i%2==0:
                down_list1.append(down_list[i])
            else:
                down_list2.append(down_list[i])

        pr1 = mp.Process(target=self.use_youget,args=(down_list1,))
        pr1.start()
        if (len(down_list2) !=0):
            pr2 = mp.Process(target=self.use_youget,args=(down_list2,))
            pr2.start()
            pr2.join()
        pr1.join()
        '''
        system('cls')
        if len(redown)>1:
            print("对不起，下载无能为力，请等以后的版本")
            print("没能下载的有一下几集：")
            print(redown)
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
