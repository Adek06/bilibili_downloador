# anime_name_list_html --> anlh怕
# anime_name_list_html_match --> anlhm
# anime_name_list --> anl
# anime_select_num --> asn
# anime_html --> adns

from requests import get
from re import findall, search

class search_ep(object):

    def __init__(self):
        pass

    def bilibili_anime_search(self):
        print("请问要搜索那部动漫？")
        name = input('>>> ')
        anime_url = 'https://search.bilibili.com/all?keyword='+name
        anlh = get(anime_url)
        anlhm = findall(r"class=\"title\" href.{2,}title=\".{2,20}\"",anlh.text)
        anl = []
        for i in range(len(anlhm)):
            anl.append(search(r'title=\".{2,15}\" lnk',anlhm[i]).group(0)[7:-5])

        print("你要找的是下面哪一个动漫呢？(输入名字前的序号选择)")
        for i in range(len(anl)):
            print(str(i)+"、"+anl[i])
        asn = input(">>> ")
        anime_address_match = search(r"//.{1,}\?",anlhm[int(asn)]) 
        adns = "https:"+anime_address_match.group(0)[:-1]
        return adns,anl[int(asn)]
