import Search_eps, Ep_infos, Downloads, Creat_folders


def creat_folder(animeName):
    creatEpFolder = Creat_folders.creat_folder(animeName)
    creatEpFolder.creat_ep_folder()

def download_ep(epInfo,animeName):
    downLoad = Downloads.Download(epInfo)
    downLoad.down_load()

def main():

    print("""
    ##################################################################
    ####                                                          ####
    ####                                                          ####
    ####                                                          ####
    ####                                                          ####
    ####                    视频下载器                            ####
    ####                                                          ####
    ####                                      v:1.0               ####
    ####                                                          ####
    ####                                 by：不愿透露姓名的游先生 ####
    ##################################################################
    """)

    print("""
    请问需要在哪里下载视频？
    """)

    print("""
    1.bilibili番剧
    2.bilibili视频合集
    """)

    try:
        notNum = True
        while(notNum):
            select = input(">>> ")
            if select == '1':
                notNum = False
           # try:
                animeDns,animeName = Search_eps.search_ep().bilibili_anime_search()
           # except:
                print("在搜索出了问题,请尝试查询该动漫是否属于b站番组计划")
                exit()

                getEpInfo = Ep_infos.Ep_info(animeDns)
                epInfo = getEpInfo.bilibili_Ep_info()

                creat_folder(animeName)

                download_ep(epInfo,animeName)
            elif select == '2':
                print('''
                在网页上打开需要下载的合集，复制地址栏上的地址
                下载结束后，打开该程序文件夹下的EP文件夹查找下载好的合集
                ''')
                notNum = False
                setPath = input("下载集合的地址:")
                setName = input("请给合集取个名字:")
                getSetInfo = Ep_infos.Ep_info(setPath)
            #setName = '合集下载'
            #getSetInfo = Ep_infos.Ep_info('https://www.bilibili.com/video/av1893599/?from=search&seid=3284471240480434664')
                setNums,setList = getSetInfo.bilibili_Set_info()
                creat_folder(setName)
                download_ep(setList,setName)
            else :
                print("请输入数字，否则按\"Ctrl+C\"退出")

    except KeyboardInterrupt:
        print("\n")
        print("成功退出程序")

if __name__ == "__main__":
    main()
