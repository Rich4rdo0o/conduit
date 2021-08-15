from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_cookies():
    url = "http://localhost:1667/#/"

    # TC04 - cookies
    driver.get(url)
    time.sleep(4)
    divs = driver.find_elements_by_xpath('//div')
    number_divs = (len(divs))
    accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
    accept.click()
    time.sleep(4)
    # we accepted the cookies that's why there are less divs
    # the browser saves the cookies so it won't pop up the next time we visit the page
    # restarting the chromedriver results a brand new browser stance which means there are cookies again
    new_divs = driver.find_elements_by_xpath('//div')
    assert not number_divs == len(new_divs)
    driver.close()
