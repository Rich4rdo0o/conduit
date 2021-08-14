from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True


def test_cookies():
    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "http://localhost:1667/#/"

    # TC04 - cookies
    driver.get(url)
    time.sleep(60)
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


test_cookies()
