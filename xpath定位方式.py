#coding=utf-8

'''
xpath  ==>xml  path language  ,表示xml文件的路径语言
根据路径来查找元素


'''''

from  playwright.sync_api  import sync_playwright

playwright=sync_playwright().start()  #  直接实例化这个对象，就不用with了

browser=playwright.chromium.launch(headless=False,slow_mo=2000,args=["--start-maximized"])
page=browser.new_page(no_viewport=True)
page.goto("https://www.baidu.com")
'''
xpath的写法规则：
/  ：表示从根节点选取
// : 表示从非根节点选取
*  ：表示任意节点选取
@  : 表示根据属性筛选
text(): 根据文本筛选
and : 关联属性或者连接文本
[]   : 可以放置下标或者属性以及连接文本
.    : 表示选取当前节点
..   : 表示当前节点的父节点
contains： 表示包含，用于模糊匹配
'''

# 1. 单一属性定位：
elem1=page.locator('//span[@name="tj_settingicon"]')
value1=elem1.text_content()
print(value1)

# 2. 多属性定位： 用and 连接

elem2=page.locator('//span[@id="s-usersetting-top"  and @name="tj_settingicon"]')
value2=elem2.text_content()
print(value2)
# 3. 通过父节点定位：
elem3=page.locator('//div[@id="u1"]/span[1]')
value3=elem3.text_content()
print(value3)


# 4.通过下标定位,  找百度页面中通过属性，找到多个元素，再用下标锁定想要的元素
elem4=page.locator('//a[@class="mnav c-font-normal c-color-t"][1]')
value4=elem4.text_content()
print(value4)

# 5.通过. 和.. 来定位
#先找到更多下面的翻译，然后再通过..向上一级进行返回定位
elem5=page.locator('//a[@name="tj_fanyi"]/div/../../../../../a[1]')
value5=elem5.text_content()
print(value5)

# 6.通过文本进行定位
elem6=page.locator('//*[text()="新闻"]')
value6=elem6.text_content()
print(value6)

# 7.模糊匹配  :  //a[contains(属性,匹配的内容)]
elem7=page.locator('//a[contains(text(),"hao")]')
value7=elem7.text_content()
print(value7)












