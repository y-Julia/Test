
'''
安装playwright 工具做ui自动化。 建议用python 3.9以下的版本。
1.第一步， 安装工具：  pip install  playwright
2.第二步， 安装 playwright 自带的各种浏览器以及工具包(谷歌和火狐)：  playwright  install
3.第三步： 安装playwright 的pytest框架 :  pip  install  pytest-palywright  

palywright 的工具：
一、playwright codegen
1.在dos窗口中，输入  palywright codegen  就会出现一个界面窗口，并且可以进行脚本的录制和编写
2.  playwright codegen   www.baidu.com   ==》打开一个界面窗口，并且同时打开百度
3.  playwright codegen  --viewport-size=800,600  www.baidu.com  ==>指定窗口的大小打开
4.  playwright codegen  --device="iPhone 13" www.baidu.com      ==> 用iphone13打开指定页面
5.  playwright codegen  --save-storage=auth.json  www.jd.com     ==》保存指定网页的cookie信息
6.  playwright codegen  --load-storage=auth.json  www.jd.com     ==》使用之前网页保存的cookie信息进行访问指定网页

二、Trace  Viewer
https://www.baidu.com


发现的问题，好象不能对元素进行锁定拖拽

'''''
from  playwright.sync_api  import  sync_playwright

# 创建浏览器，打开页面
with sync_playwright()  as p:     #  通过with避免打开浏览器报错，导致脚本运行失败
    browser=p.chromium.launch(headless=False,             # 创建一个浏览器对象，headless=False 表示不使用无头模式
                              args=["--start-maximized"], #a rgs=["--start-maximized"] 表示最大化窗口
                              slow_mo=3000)      #规定每个操作停顿3000毫秒
    # 创建一个页面对象, 指定窗口打开的大小.    no_viewport=True 表示使窗口默认的大小失效，从而去执行最大化窗口
    page=browser.new_page(no_viewport=True)
    # page=browser.new_page(viewport={"width":1920,"height":1080}) # 规定打开窗口的页面的大小
    page.goto("https://aspecta.id")  # 访问产品
    title=page.title()  #获取页面标题
    # print(title)

    # 控制浏览器
    # page.get_by_text("")
    # 回退
    page.go_back()
    #前进
    page.go_forward()
    #刷新
    page.reload()
    #关闭浏览器
    browser.close()













