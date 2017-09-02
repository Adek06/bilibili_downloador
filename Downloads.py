from os import system, chdir
import sys
from you_get import common as you_get
import multiprocessing as mp

class Download(object):

    def __init__(self,Ep_info_list,Ep_name):
        self.Ep_info_list = Ep_info_list
        self.Ep_name = Ep_name

    def use_youget(self,down_url_list):
        for i in range(len(down_url_list)):
            sys.argv=['you-get',down_url_list[i]]
            you_get.main()
            system('cls')

    def down_load(self):
        print("请问要从第几集开始下载？")
        startEp_id = input(">>> ")
        print("要下载到第几集？")
        endEp_id = input(">>> ")
        down_list = self.Ep_info_list[int(startEp_id)-1:int(endEp_id)]
        print("马上开始下载，请稍后...")
        #chdir('.\EP')
        #chdir(str(self.Ep_name))

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
        print("下载结束")
