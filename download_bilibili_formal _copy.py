
import requests
import re
import os

def search_anime(name):
   
   anime_url = 'https://search.bilibili.com/all?keyword='+name
   anime_name_list_html = requests.get(anime_url)
   anime_name_list_html_match = re.findall(r"class=\"title\" href.{2,}title=\".{2,20}\"",anime_name_list_html.text)
   anime_name_list=[]
   for i in range(len(anime_name_list_html_match)):
       anime_name_list.append(re.search(r'title=\".{2,15}\"',anime_name_list_html_match[i]).group(0)[7:-1])

   print("你要找的是下面哪一个动漫呢？(输入名字前的序号选择)")
   for i in range(len(anime_name_list)):
       print(str(i)+"、"+anime_name_list[i])
   anime_select_num = input(">>> ")
   anime_address_match = re.search(r"//.{1,}\?",anime_name_list_html_match[int(anime_select_num)]) 
   anime_html = "https:"+anime_address_match.group(0)[:-1]
   return anime_html,anime_name_list[int(anime_select_num)]

def Ep_info(html):
    
    anime_homepage_html_requests = requests.get(html)
    newEp_first_match = re.findall("newestEp: \'\d{1,3}\'",anime_homepage_html_requests.text)
    newEp_num = int(re.search("\d{1,3}",newEp_first_match[0]).group(0))

    newEp_id = int(re.search("\d{1,10}" , re.findall("data-newest-ep-id=\"\d{2,10}\"" , anime_homepage_html_requests.text)[0] ).group(0))
    firstEp_id = newEp_id-newEp_num+1
    print("这个动漫现在为止，一共有"+str(newEp_num)+"集")
    return newEp_num,firstEp_id

def down_load(anime_homepage_html,Ep_num,firstEp_id):

    print("请问要从第几集开始下载？")
    startEp_id = input(">>> ")
    startEp_id = int(startEp_id)+firstEp_id-1
    print("下载到第几集？")
    downloadEp_num = input(">>> ")
    print("请稍后，马上开始下载...")
    for i in range(int(downloadEp_num)):
        print("""
        如果想要退出下载，直接关闭即可。
        下载好的文件将会在本软件的目录下出现
                """)
        print(anime_homepage_html+str(startEp_id))
        os.system("you-get "+anime_homepage_html+str(startEp_id))
        startEp_id = int(startEp_id)+1
        

print("""
##################################################################
####                                                          ####
####                                                          ####
####                                                          ####
####                                                          ####  
####                    b站下载器                              ####
####                                                          ####          
####                                      v:1.0               ####
####                                                          ####
####                                     by：不愿透露姓名的游先生 ####
##################################################################
""")

print("请输入需要查询的动漫")
#anime_name = input()
anime_name = "Re:CREATORS"

anime_homepage_html,anime_real_name=search_anime(anime_name)
Ep_sum_num,firstEp_id = Ep_info(anime_homepage_html)

if anime_name in (os.listdir(".")):
    pass
else:
    os.mkdir("./"+str(anime_real_name))

os.chdir("./"+str(anime_real_name))

anime_homepage_html += "/play#"
down_load(anime_homepage_html,Ep_sum_num,firstEp_id)