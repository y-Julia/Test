'''
playwright自带的定位方式
'''''


from playwright.sync_api  import sync_playwright

playwright=sync_playwright().start()

browser=playwright.chromium.launch(headless=False,
                                   args=["--start-maximized"],
                                   slow_mo=2000)

page=browser.new_page(no_viewport=True)

page.get_by_text()
page.get_by_label()
page.get_by_placeholder()
page.get_by_role()
page.locator()






















