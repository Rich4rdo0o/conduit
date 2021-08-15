from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_pages():
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'testuser1'
    email = 'testuser1@example.com'
    pw = 'Abcd123$'

    # TC08 - Pages
    # register, home, settings, new article pages already checked in previous testcases
    # login
    sign_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    sign_in.click()
    time.sleep(3)
    email_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    pw_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    email_field.send_keys(email)
    pw_field.send_keys(pw)
    sign_in_btn.click()
    time.sleep(4)
    # checking articles on different pages
    divs1 = driver.find_elements_by_xpath('//div')
    number_divs1 = (len(divs1))
    # print(number_divs1)
    page2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[2]/a')
    page2.click()
    time.sleep(3)
    divs2 = driver.find_elements_by_xpath('//div')
    number_divs2 = (len(divs2))
    # print(number_divs2)
    assert number_divs1 != number_divs2
    # div numbers are not equal on the different pages, means there are different posts
    page1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[1]/a')
    page1.click()
    time.sleep(3)
    # number_divs1 = (len(divs1))
    # print(number_divs1)
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()
