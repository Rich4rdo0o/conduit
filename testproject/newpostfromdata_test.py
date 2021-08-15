from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_new_post_from_data():
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'testuser1'
    email = 'testuser1@example.com'
    pw = 'Abcd123$'
    title = 'test post'
    about = 'life'
    with open('/home/runner/work/conduit/conduit/testproject/send_up_test.txt') as f:
        sending = f.read()

    # TC10 - New post from data
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
    # TC upload data from file
    a_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
    publish_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    a_title.send_keys(title)
    a_about.send_keys(about)
    # cycle for sending serial data ("Ismételt és sorozatos adatbevitel adatforrásból")
    for _ in range(2):
        a_text.send_keys(sending)
        time.sleep(2)
    publish_btn.click()
    time.sleep(3)
    # checking the sent data
    sent = driver.find_element_by_xpath('//p')
    assert sending == sent.text
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()

