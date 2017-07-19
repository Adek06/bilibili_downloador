from os import system, chdir

class Download(object):

    def __init__(self,Ep_info_list,Ep_name):
        self.Ep_info_list = Ep_info_list
        self.Ep_name = Ep_name

    def down_load(self):
        print("请问要从第几集开始下载？")
        startEp_id = input(">>> ")
        print("要下载到第几集？")
        endEp_id = input(">>> ")
        down_list = self.Ep_info_list[int(startEp_id)-1:int(endEp_id)]
        print("马上开始下载，请稍后...")
        chdir('./EP/'+str(self.Ep_name))
        for i in down_list:
            print("""
                如果想要退出下载，请直接关闭程序即可
                下载好的文件会出现在该EP文件夹里
            """)
            system("you-get "+i)
