from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_new_post():
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'testuser1'
    email = 'testuser1@example.com'
    pw = 'Abcd123$'
    title = 'test post'
    about = 'life'
    text = 'some life changing wisdom'

    # TC06 - New post
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
    # adding new article
    new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    new_article.click()
    time.sleep(3)
    a_title = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
    a_about = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
    a_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
    publish_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    a_title.send_keys(title)
    a_about.send_keys(about)
    a_text.send_keys(text)
    time.sleep(2)
    publish_btn.click()
    time.sleep(3)
    # checking new article
    article_title = driver.find_element_by_xpath('//h1')
    assert article_title.text == 'test post'
    # checking new article on homepage
    home_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
    home_page.click()
    time.sleep(3)
    posted = driver.find_element_by_xpath('//h1[text()="test post"]')
    assert posted.text == 'test post'
    # logout
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()
