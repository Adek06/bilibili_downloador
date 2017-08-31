import Search_eps, Ep_infos, Downloads, Creat_folders


def creat_folder(animeName):
    creatEpFolder = Creat_folders.creat_folder(animeName)
    creatEpFolder.creat_ep_folder()

def download_ep(epInfo,animeName):
    downLoad = Downloads.Download(epInfo,animeName)
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
    在开始下载前，请确保已经下载并安装了Chrome浏览器或者Firefox浏览器，
    并在指定的位置放置好对应浏览器的driver。
    """)

    print("""
    请问需要在哪里下载视频？
    """)

    print("""
    1.bilibili
    """)

    try:
        notNum = True
        while(notNum):
            select = input(">>> ")
            if select == '1':
                notNum = False
                try:
                    animeDns,animeName = Search_eps.search_ep().bilibili_anime_search()
                except:
                    print("在搜索出了问题,请尝试查询该动漫是否属于b站番组计划")
                    exit()

                getEpInfo = Ep_infos.Ep_info(animeDns)
                epInfo = getEpInfo.bilibili_Ep_info()

                creat_folder(animeName)

                download_ep(epInfo,animeName)
            else :
                print("请输入数字，否则按\"Ctrl+C\"退出")

    except KeyboardInterrupt:
        print("\n")
        print("成功退出程序")

if __name__ == "__main__":
    main()
