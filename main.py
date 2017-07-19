import Search_eps, Ep_infos, Downloads, Creat_folders

def main():

    print("""
    ##################################################################
    ####                                                          ####
    ####                                                          ####
    ####                                                          ####
    ####                                                          ####  
    ####                    视频下载器                              ####
    ####                                                          ####          
    ####                                      v:1.0               ####
    ####                                                          ####
    ####                                     by：不愿透露姓名的游先生 ####
    ##################################################################
    """)

    print('请问需要在哪里下载视频？')
    
    print("""
    1.bilibili
    """)

    select = input(">>> ")
    try:
        if select == '1':
            
            search = Search_eps.search_ep()
            try:
                animeDns,animeName = search.bilibili_anime_search()
            except:
                print("在搜索出了问题,请尝试查询该动漫是否属于b站番组计划")
                exit()
                
            getEpInfo = Ep_infos.Ep_info(animeDns)
            epInfo = getEpInfo.bilibili_Ep_info()

            try:
                creatEpFolder = Creat_folders.creat_folder(animeName)
                creatEpFolder.creat_ep_folder()
            except:
                print('在创建文件夹时出了点问题')
                exit()

            downLoad = Downloads.Download(epInfo,animeName)
            downLoad.down_load()
    except:
        pass

if __name__ == "__main__":
    main()
