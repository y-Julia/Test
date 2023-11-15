'''
css 定位方式比xpath快
'''''

from  playwright.sync_api  import sync_playwright

playwright=sync_playwright().start()

browser=playwright.chromium.launch(headless=False,args=["--start-maximized"],slow_mo=2000)

page=browser.new_page(no_viewport=True)

page.goto("https://www.jd.com")
page.mouse.wheel(1000,1000)

# page.locator('//div[@id="J_feeds"]/div/div/div/h3').scroll_into_view_if_needed()
# # 1.id选择器：  #
# page.locator('#kw').fill("python")  # 输入python
#
#
# # 2.class选择器：  .
# page.locator(".bg s_btn").click()  #点击百度以下
#
# # 3. 标签选择器：
# page.locator("input#kw")
#
# # 4.层级关系定位
# page.locator('div>form>span>input.s_ipt')
#















