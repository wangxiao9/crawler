from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# brower = webdriver.Chrome("chromedriver.exe")
#
# brower.get("https://v.qq.com/channel/net_tv")
#
# content = brower.page_source
# print(content)

def TengXun():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

driver = TengXun()
driver.get("https://v.qq.com/channel/net_tv")
driver.save_screenshot("tenxu.png")