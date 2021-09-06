import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select


def collect_proxies():
    driver = webdriver.Chrome(executable_path='chromedriver')
    url = 'https://free-proxy-list.net/'
    driver.get(url)
    proxies = []
    url = 'https://free-proxy-list.net/'
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "proxylisttable")))
    except TimeoutException:
        driver.quit()

    selectXpath = '//*[@id="proxylisttable"]/tfoot/tr/th[7]/select'
    select_https = Select(driver.find_element(By.XPATH, selectXpath))

    #Change the filter to only show https proxies
    select_https.select_by_visible_text('yes')

    nextXpath = '//*[@id="proxylisttable_next"]/a'

    proxy_table_body = driver.find_element(By.XPATH, '//*[@id="proxylisttable"]/tbody')
    for pageNum in range(4):
        rows = proxy_table_body.find_elements(By.CSS_SELECTOR, 'tr')
        for tr in rows:
            td = tr.find_elements(By.CSS_SELECTOR, 'td')
            proxy = f'{td[0].text}:{td[1].text}'
            proxies.append(proxy)
        next_Page = driver.find_element(By.XPATH, nextXpath)
        next_Page.click()



    #webdriver.ActionChains(driver).move_to_element(select_https).click(element).perform()
    return proxies

