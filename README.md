# bilibili_downloador

基于Python编写的下载器。

### 功能

1. 批量下载b站番组计划的动漫



**必须在需要在python3.5以上的使用。**

## 演示





### 安装前准备

> - python3.5
> - you-get
> - chrome浏览器
> - chrome driver

该程序借由you-get完成。

所以在运行前，请确保自己已经安装了you-get

```
pip install you-get
```

另外，由于使用了selenium，需要chrome driver和chrome浏览器，请确保有chrome浏览器，另外[点此下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)chrome driver

windows 下，新建一个命名为chromedriver文件夹，将解压的chromedriver.exe放进文件夹，再配置进path环境变量

Linux下，把下载好的文件放在 /usr/bin 目录下就可以了。

### 安装

linux

```
git clone https://github.com/Adek06/bilibili_downloador.git
```

windows ，[点击这里下载](https://codeload.github.com/Adek06/bilibili_downloador/zip/master)

###  使用

打开文件夹下的start.sh

下载的动漫会在该文件夹下的EP文件夹里，如果没有，在下载的过程中，会自行创建