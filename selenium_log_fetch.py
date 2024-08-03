from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 设置 Chrome WebDriver 的路径
chrome_driver_path = ""# 请替换成你的 Chrome 驱动程序的路径

options = webdriver.ChromeOptions()
path = Service()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})  # 开启日志性能监听
driver = webdriver.Chrome(service=path, options=options)
driver.get("https://www.enf.com.cn/ea-gruppen?directory=seller&utm_source=ENF&utm_medium=Germany&utm_content=145196&utm_campaign=profiles_seller")
element = (WebDriverWait(driver, 10)
# .until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/table[3]/tbody/tr/td[2]/span'))
#             )
)
            # 触发反爬之后的点击
# element.click()
time.sleep(1)
performance_log = driver.get_log('performance')  # 获取名称为 performance 的日志
for i in range(len(performance_log)):
    message = json.loads(performance_log[i]['message'])
    # print(message,'\n') # 信息查看
    message = message['message']['params']
    print(message, '\n')# 信息查看
    request = message.get('request')
    if (request is None):
        continue
    url = request.get('url')
    if "https://www.enf.com.cn/company_email/" in url: # 指定的请求
        # 如果 URL 中包含指定的子字符串，则执行以下操作，获取响应内容
        detail_response = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
        print(detail_response)
    # else:
    #     print("not:", url)




